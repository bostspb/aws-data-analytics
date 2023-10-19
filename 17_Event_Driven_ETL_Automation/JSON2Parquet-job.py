import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://<Enter-Your-Landing-Bucket-Name>/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Apply Mapping
ApplyMapping_node = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("shipping_id", "int", "shipping_id", "int"),
        ("shipping_date", "string", "shipping_date", "string"),
        ("customer_name", "string", "customer_name", "string"),
        ("street_address", "string", "street_address", "string"),
        ("destination_city", "string", "destination_city", "string"),
        ("shipping_cost", "double", "shipping_cost", "double"),
        ("shipping_distance", "double", "shipping_distance", "double"),
        ("quantity", "double", "quantity", "double"),
        ("product_id", "int", "product_id", "int"),
    ],
    transformation_ctx="ApplyMapping_node",
)

# Script generated for node Amazon S3
AmazonS3_node = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://<Enter-Your-Staging-Bucket-Name>/transformed_data/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node",
)

job.commit()
