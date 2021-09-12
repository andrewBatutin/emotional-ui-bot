import requests

url = 'https://api.wildwildhack.ai/api/signedurl?extension=jpg'
headers = {"Authorization": "Bearer 211acc3c360b4dccaffefbab0b14d0c4"}
auth_token = '211acc3c360b4dccaffefbab0b14d0c4'
json_headers = {
    'authorization': f'Bearer {auth_token}',
    'content-type': 'application/json',
}

signed_url_first = requests.post(url, json={"extension": "jpg"}, headers=headers).json()
image_url_first = signed_url_first['url']
# "https://storage.googleapis.com/prod-reflect-videos/data/images/f590a9cb-172f-4fb0-8021-914e7afaa48d.jpg?GoogleAccessId=prod-images-admin@reface-prod-stage.iam.gserviceaccount.com&Expires=1631376256&Signature=0WBqKY1pfnU3oPP8AooDiMgmY9VPBi3LBVlrg%2BO9VGnoxytzX87dz%2FPS2mksb5GqHPVzWAsiIQBdGPPE2O1wUjCHOuH8gUpl5spgJnFPZGX2LlYx%2FxDyLcKOHpJ%2BrIcWNdaUMxlz%2B4K%2F2gHyUmd5bh5VdkodlPxmy59P5t3iIC8xBalu8fHxxPNBrftCKiF%2B6giAoe3l39MMkDBGyQi3yKs2xFHVj9pqcgAw0Ja5xcBpqxBAw0xS81L4efl%2Fe%2B1csanIMOvBRuGYiXHkTvhwu%2BRf2oMXr5L%2FPMakO0ElTxpKEH4%2BciIGbX6PrFzVYG4IGhsAsYemJShy5bFbnVRNVw=="
print(image_url_first)

img_put_headers = {
    'content-type': 'image/jpeg',
}

# files = {'media': open('files/photo_2021-09-11_17-53-41.jpg', 'rb')}
with open('/Users/admin/Documents/RF_hckt/t_bot/files/photo_2021-09-11_17-53-41.jpg', 'rb') as f:
    img_data = f.read()
res = requests.put(image_url_first, headers=img_put_headers, data=img_data)
img_path = res.url.split('?')[0]

img_put_headers = {
    'Content-Type': 'application/json',
    'accept': 'application/json',
    'authorization': f'Bearer {auth_token}',
}

res = requests.post('https://api.wildwildhack.ai/api/face', headers=img_put_headers, json={
    'path': 'https://storage.googleapis.com/prod-reflect-videos/data/images/81f2f429-2cca-464f-98a4-f5ae2c1e57e0.jpg'})

video_json_headers = {
    'authorization': f'Bearer {auth_token}'
}

signed_video_url_first = requests.post(url, json={"extension": "mp4"}, headers=video_json_headers).json()
video_url_first = signed_video_url_first['url']

print(video_url_first)


video_put_headers = {
    'content-type': 'video/mp4',
}

# files = {'media': open('files/photo_2021-09-11_17-53-41.jpg', 'rb')}
with open('files/IMG_5344.mp4', 'rb') as f:
    video_data = f.read()
    res = requests.put(video_url_first, headers=video_put_headers, data=video_data)
    video_path = res.url.split('?')[0]
    print(video_path)

video_put_headers = {
    'Content-Type': 'application/json',
    'accept': 'application/json',
    'authorization': f'Bearer {auth_token}',
}

res = requests.post('https://api.wildwildhack.ai/api/video', headers=video_put_headers, json={
    'path': 'https://storage.googleapis.com/prod-reflect-videos/data/inputs/b894f8dc-df16-4e24-bf76-63446fb01ebd.mp4'})

print(res)


#wait


res = requests.get('https://api.wildwildhack.ai/api/video/b894f8dc-df16-4e24-bf76-63446fb01ebd', headers=headers)

print(res)

#swap

res = requests.post('https://api.wildwildhack.ai/api/swap-video', headers=headers, json={
    "video_id": "b894f8dc-df16-4e24-bf76-63446fb01ebd",
    "facemapping":{"47f3b946-1358-4e28-b20b-c01e4b84750b":["e7c64439-bc38-4a50-9937-cf0d215e4c69"]}})

print(res)