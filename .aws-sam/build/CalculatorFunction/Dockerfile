
FROM python:3.12-slim

WORKDIR /app

COPY calculator.py lambda_function.py ./
COPY test_calculator.py test_lambda_function.py ./

CMD ["python", "-m", "unittest", "-v", "test_calculator", "test_lambda_function"]
