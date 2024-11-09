import json
from lambda_handler import lambda_handler

def test_lambda_handler_with_all_params():
    event = {
        'queryStringParameters': {
            'cluster': 'my-cluster',
            'service': 'my-service',
            'variable': 'my-variable'
        }
    }
    context = {}  # Mock context
    response = lambda_handler(event, context)
    print("Response with all params:", response)

def test_lambda_handler_with_missing_cluster():
    event = {
        'queryStringParameters': {
            'service': 'my-service',
            'variable': 'my-variable'
        }
    }
    context = {}  # Mock context
    response = lambda_handler(event, context)
    print("Response with missing cluster:", response)

# def test_lambda_handler_with_non_string_params():
#     event = {
#         'queryStringParameters': {
#             'cluster': 123,  # Int instead of string
#             'service': 'my-service',
#             'variable': 'my-variable'
#         }
#     }
#     context = {}  # Mock context
#     response = lambda_handler(event, context)
#     print("Response with non-string cluster:", response)

def test_lambda_handler_with_invalid_event():
    event = {}  # Simulate an invalid event
    context = {}  # Mock context
    response = lambda_handler(event, context)
    print("Response with invalid event:", response)

if __name__ == "__main__":
    test_lambda_handler_with_all_params()
    test_lambda_handler_with_missing_cluster()
    # test_lambda_handler_with_non_string_params()
    test_lambda_handler_with_invalid_event()
