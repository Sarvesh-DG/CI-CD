
import json
import unittest
from lambda_function import lambda_handler


class TestLambdaFunction(unittest.TestCase):

    def test_addition(self):
        event = {
            "body": json.dumps({
                "operation": "add",
                "a": 10,
                "b": 5
            })
        }

        response = lambda_handler(event, None)

        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(json.loads(response["body"])["result"], 15)

    def test_subtraction(self):
        event = {
            "body": json.dumps({
                "operation": "subtract",
                "a": 10,
                "b": 5
            })
        }

        response = lambda_handler(event, None)

        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(json.loads(response["body"])["result"], 5)

    def test_multiplication(self):
        event = {
            "body": json.dumps({
                "operation": "multiply",
                "a": 10,
                "b": 5
            })
        }

        response = lambda_handler(event, None)

        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(json.loads(response["body"])["result"], 50)

    def test_invalid_operation(self):
        event = {
            "body": json.dumps({
                "operation": "divide",
                "a": 10,
                "b": 5
            })
        }

        response = lambda_handler(event, None)

        self.assertEqual(response["statusCode"], 400)


if __name__ == "__main__":
    unittest.main()
