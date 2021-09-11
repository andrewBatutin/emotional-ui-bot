import requests

url = 'https://api.wildwildhack.ai/api/signedurl?extension=jpg'
headers = {"Authorization": "Bearer 211acc3c360b4dccaffefbab0b14d0c4"}
auth_token = '211acc3c360b4dccaffefbab0b14d0c4'
json_headers = {
    'authorization': f'Bearer {auth_token}',
    'content-type': 'application/json',
}

signed_url_first = requests.post(url,json={"extension":"jpg"}, headers=headers).json()
image_url_first = signed_url_first['url']
#"https://storage.googleapis.com/prod-reflect-videos/data/images/f590a9cb-172f-4fb0-8021-914e7afaa48d.jpg?GoogleAccessId=prod-images-admin@reface-prod-stage.iam.gserviceaccount.com&Expires=1631376256&Signature=0WBqKY1pfnU3oPP8AooDiMgmY9VPBi3LBVlrg%2BO9VGnoxytzX87dz%2FPS2mksb5GqHPVzWAsiIQBdGPPE2O1wUjCHOuH8gUpl5spgJnFPZGX2LlYx%2FxDyLcKOHpJ%2BrIcWNdaUMxlz%2B4K%2F2gHyUmd5bh5VdkodlPxmy59P5t3iIC8xBalu8fHxxPNBrftCKiF%2B6giAoe3l39MMkDBGyQi3yKs2xFHVj9pqcgAw0Ja5xcBpqxBAw0xS81L4efl%2Fe%2B1csanIMOvBRuGYiXHkTvhwu%2BRf2oMXr5L%2FPMakO0ElTxpKEH4%2BciIGbX6PrFzVYG4IGhsAsYemJShy5bFbnVRNVw=="
print(image_url_first)

img_put_headers = {
    'content-type': 'image/jpeg',
}

#files = {'media': open('files/photo_2021-09-11_17-53-41.jpg', 'rb')}
with open('/Users/admin/Documents/RF_hckt/t_bot/files/photo_2021-09-11_17-53-41.jpg','rb') as f:
    img_data =f.read()
res = requests.put(image_url_first, headers=img_put_headers, data=img_data)
print(res.url)