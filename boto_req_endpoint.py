import boto3

import json

endpoint = 'huggingface-pytorch-inference-2021-09-11-07-59-49-021'

runtime = boto3.Session(profile_name='default').client('sagemaker-runtime')


def send_message_for_inference(message):
    payload = '{"inputs": "%s"}' % message
    response = runtime.invoke_endpoint(EndpointName=endpoint, ContentType='application/json', Accept='application/json',
                                       Body=payload)

    # Unpack response
    result = json.loads(response['Body'].read().decode())
    return result

