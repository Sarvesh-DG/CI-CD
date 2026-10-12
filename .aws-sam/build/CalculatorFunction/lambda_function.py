
import json
from calculator import add, mul, sub


def lambda_handler(event, context):
    try:
        # Extract the request body from API Gateway
        body = event.get("body")

        if isinstance(body, str):
            data = json.loads(body)
        elif isinstance(body, dict):
            data = body
        else:
            # Support direct Lambda invocation too
            data = event

        operations = {
            "add": add,
            "subtract": sub,
            "multiply": mul,
        }

        operation = data.get("operation")
        a = data.get("a")
        b = data.get("b")

        if operation not in operations:
            raise ValueError(
                "Operation must be add, subtract or multiply"
            )

        if type(a) is not int or type(b) is not int:
            raise ValueError("Inputs must be integers")

        result = operations[operation](a, b)

        return {
            "statusCode": 200,
            "body": json.dumps({"result": result}),
        }

    except (ValueError, TypeError) as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)}),
        }
