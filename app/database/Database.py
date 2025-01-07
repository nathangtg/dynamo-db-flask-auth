import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class Database:
    def __init__(self):
        self.dynamodb = None

    def connect(self):
        # Change the Database connection details as per your local or Production setup
        try:
            self.dynamodb = boto3.resource(
                'dynamodb',
                endpoint_url='http://localhost:8566',  
                region_name='us-west-2',
                aws_access_key_id='fakeMyKeyId',
                aws_secret_access_key='fakeSecretAccessKey'
            )
            print("Connected to DynamoDB Local successfully!")
        except (NoCredentialsError, PartialCredentialsError) as e:
            print(f"Failed to connect to DynamoDB: {str(e)}")
        return self.dynamodb

    def get_table(self, table_name):
        if not self.dynamodb:
            raise Exception("Database connection is not established. Call 'connect()' first.")
        return self.dynamodb.Table(table_name)