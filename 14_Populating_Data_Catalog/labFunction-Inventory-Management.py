from faker import Faker
import random
from faker.providers import currency, barcode

import logging
import boto3
from botocore.exceptions import ClientError
import os

import pandas as pd
from collections import defaultdict

# Need to update the environment variable in the Lambda function with your input S3 bucket
inputBucket = os.environ['input_bucket']

def lambda_handler(event, context):
    generate_data()
    upload_file(file_name='/tmp/inventory.csv',bucket=inputBucket)

def generate_data():
    fake = Faker()
    fake.add_provider(currency)

# Use Faker to generate updated inventory data. Add two new columns (product city and product country)
    fake_data = defaultdict(list)
    for _ in range(1000):
        fake_data["Product_id"].append(random.randint(0, 10000))
        fake_data["Product_stock"].append(random.randint(1, 1000))
        fake_data["Product_barcode"].append(fake.ean(length=8))
        fake_data["Product_city"].append(fake.city())
        fake_data["Product_country"].append(fake.country())

    df_fake_data = pd.DataFrame(fake_data)

    print(df_fake_data.head())

# Remove the first column index data
    df_fake_data.to_csv("/tmp/inventory.csv",index=False)

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True