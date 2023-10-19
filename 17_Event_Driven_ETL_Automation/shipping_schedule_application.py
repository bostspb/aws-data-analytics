"""
This lambda function Generates fake shipping data and uploads to the bucket.
"""

import os
import boto3
from botocore.exceptions import ClientError
import logging
import urllib3
import json

http = urllib3.PoolManager()
SUCCESS = "SUCCESS"
FAILED = "FAILED"

import random
import datetime
from faker import Faker
from faker.providers import address, person

fake = Faker()
fake.add_provider(address)
fake.add_provider(person)

# It is a good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')
bucket_name = os.environ['BUCKET_NAME']


def lambda_handler(event, context):
    logger.info(f'event: {event}')
    generate_data(10)


def generate_data(num_records):
    logger.info("Generating data")
    # Call the get_secrets() function to get data from Secrets manager
    faker = Faker()

    # list of fake toll plaza name
    shipping_destination_list = ["serverless_island", "island_city", "machine_learning_island", "architect_city", "data_analytic_hanger", "main_city"]


    fake = Faker()

    for n in range(0, num_records):
        fake_data = {}
        date_obj = datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 1))
        delivery_date = date_obj.strftime("%Y/%m/%d")
        shipping_price = faker.random_int(1000, 10000) / 1.0
        load_details = faker.random_int(1000, 10000)
        shipping_distance = faker.random_int(10, 100)
        shipping_destination = random.choice(shipping_destination_list)
        fake_data["shipping_id"] = fake.random_number(5)
        fake_data["shipping_date"] = delivery_date
        fake_data["customer_name"] = fake.name()
        fake_data["street_address"] = fake.street_address()
        fake_data["destination_city"] = shipping_destination
        fake_data["shipping_cost"] = shipping_price
        fake_data["shipping_distance"] = shipping_distance
        fake_data["quantity"] = load_details
        fake_data = json.dumps(fake_data)
        with open('/tmp/shipping_data.json', 'a') as f_object:
            f_object.write(f"{fake_data}\n")
    print("File has been created.")

    try:
        response = s3.upload_file(
            '/tmp/shipping_data.json',
            Bucket=bucket_name,
            Key=f'shipping_data.json-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")}.json'
        )
        logger.info('File Uploaded Successfully')
    except ClientError as e:
        logging.error(e)
        logger.info('File Not Uploaded')
    else:
        logger.info('empty list')
