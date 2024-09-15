import requests
import json
import boto3
from datetime import datetime
from collections import Counter
import os

# URLs for ECS services
ecs_urls = {
    "V1": os.environ.get('ECS_V1_URL', 'http://34.238.117.55/predict'),
    "tweet": os.environ.get('ECS_TWEET_URL', 'http://44.220.193.162/predict'),
    "abs": os.environ.get('ECS_ABS_URL', 'http://54.158.213.252/predict'),
    "gpt2": os.environ.get('ECS_GPT2_URL', 'http://52.23.156.75/predict'),
    "wiki": os.environ.get('ECS_WIKI_URL', 'http://3.239.12.255/predict')
}

# Initialize DynamoDB resources
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MugcV2Database')

def get_prediction(url, text):
    try:
        response = requests.post(url=url, json={"text": text})
        prediction_dict = response.json()
        return 'Machine' if prediction_dict["Label"] == '1' else 'Human'
    except Exception as e:
        return str(e)

def lambda_handler(event, context):
    try:
        text = event.get('base')
        
        # Get predictions from all models
        predictionV1 = get_prediction(ecs_urls["V1"], text)
        predictiontweet = get_prediction(ecs_urls["tweet"], text)
        predictiongpt2 = get_prediction(ecs_urls["gpt2"], text)
        predictionabs = get_prediction(ecs_urls["abs"], text)
        predictionwiki = get_prediction(ecs_urls["wiki"], text)
        
        # Gather predictions into a list for majority voting
        listpred = [predictionV1, predictiontweet, predictiongpt2, predictionabs, predictionwiki]
        counter = Counter(listpred)
        final_prediction = counter.most_common(1)[0][0]
        
        # Record current time
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write result to the database (preserve the original item structure)
        table.put_item(
            Item={
                'ID': str(int(datetime.now().timestamp() * 1000)),
                'predictionV1': predictionV1,
                'predictiontweet': predictiontweet,
                'predictiongpt2': predictiongpt2,
                'predictionabs': predictionabs,
                'predictionwiki': predictionwiki,
                'prediction': final_prediction,
                'UploadTime(UTC)': now,
                'text': text
            }
        )

        # Return the prediction result
        return {
            'statusCode': 200,
            'body': json.dumps(final_prediction)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
