import json

def lambda_handler(event, context):
    try:
        # Attempt to retrieve query parameters
        
        cluster = event['queryStringParameters']['cluster']
        service = event['queryStringParameters']['service']
        variable = event['queryStringParameters']['variable']
        
        if cluster is None or service is None or variable is None:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Cluster parameter is required'})
            }

        # Simulate further processing with the cluster parameter
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Cluster {cluster} , Service {service} & Variable {variable} processed successfully'})
        }

    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'Missing key: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error', 'message': str(e)})
        }
