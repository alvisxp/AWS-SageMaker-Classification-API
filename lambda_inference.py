import boto3
import json
import ast

def lambda_handler(event, context):

    runtime_client = boto3.client('runtime.sagemaker')
    
    endpoint_name = 'xgboost-2024-01-21-18-14-32-040'
    
    sample = '{},{},{},{}'.format(ast.literal_eval(event['body'])['x1'],
                                    ast.literal_eval(event['body'])['x2'],
                                    ast.literal_eval(event['body'])['x3'],
                                    ast.literal_eval(event['body'])['x4'])
    
    response = runtime_client.invoke_endpoint(EndpointName=endpoint_name, 
                                                ContentType= 'text/csv', 
                                                Body=sample)
                                                
    result = int(float(response['Body'].read().decode('ascii')))
    
    if (result == 0):
        result = 'Iris-setosa'
    elif (result == 1):
        result = 'Iris-versicolor'
    elif (result == 2):
        result = 'Iris-virginica'
    
    print(result)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps({'prediction': result})
    }
