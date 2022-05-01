from os import path
from urllib import response
import boto3 
from pprint import pprint
import csv, json
import pandas as pd 
import pytz
import io
from pandas import util
import numpy as np
import create_dynamodb
from decimal import Decimal

session = boto3.session.Session()
resource = session.resource(region_name="us-east-1",service_name="s3")
client = session.client(service_name="s3")
acount_id = session.client('sts')
dynamodb = session.resource(region_name="us-east-1",service_name="dynamodb")
print(dir(dynamodb))
def list_buckets():
    """ This function is to List all buckets. """
    count = 1
    buck_dict = {}
    list_of_buckets = client.list_buckets()['Buckets']
    buckets_name = [buckets['Name'] for buckets in list_of_buckets]
    for each_times in buckets_name:
        buck_dict["bucket_name"+str(count)]= each_times
        count +=1    
    return buckets_name

def list_object(buckets_name, key):
    """ This function is use to list object in a bucket. 
    """
    buckets = list_buckets()
    response = client.get_object(Bucket=buckets_name, Key= key)['Body']
    return list(response)    

def create_bucket(bucket_name):
    """ Create bucket if not exist. 
    
    Parameter:
    str(): bucket_name, NAME of the bucket that would be created
    Return:
    None
    """
    buckets = list_buckets()
    try: 
        if bucket_name not in buckets:
            response = client.create_bucket(
                Bucket=bucket_name
                )
            return f"Creating bucket with name {bucket_name}", response
        else:
            return f"bucket with name {bucket_name} already exist"
    except Exception as e:
        return None      


def delete_bucket(delete_bucket):
    """ Delete bucket if exits and bucket is empty. """
    response = acount_id.get_caller_identity()
    acount = response.get('Account')
    buckets = list_buckets()
    try:
        if delete_bucket in buckets:
            response = client.delete_bucket(
                Bucket=delete_bucket
                )
        else:
            return f"bucket name {delete_bucket} doesn't exist in the list"
    except Exception as e:
        return e    
    return response 


def get_object(bucket_name, path):
    """ This Function is used to list objects from s3 buckect.

    Parameter:
    str():  bucket_name, The name of the bucket where you want to view it's content. 
    str():  path, This is key of the bucket.
    
    """
    bucket_content = client.get_object(Bucket=bucket_name, Key=path)['Body'].read()

    return bucket_content

def dynamoput_item(table,bash_object):
    """ This Function is used to use to perform put operations to dynamo table. 
    
    Parameters:
    tables: Table name
    bash_object: bash stript

    Return:
    str():
    """
    table.put_item(Item=bash_object)

def main():
    """ Calling all functions. """
    json_objects = get_object(bucket_name='dynamo-to-lambda-csv', path="test.json")

    """ Create Dynamodb table. 
    Import the create_table() function from create_dynamodb modules

    Parameter:
    it accept 4 parameters:
    str()table_name: Provide bucket name
    str()atr_1: Name of First Atribute
    str()atr_2: Name of Second attribute
    strs()tags: name of tags
    """
    table = create_dynamodb.create_table(
        table_name='register',
        atr_1='Name',
        atr_2='Email',
        tags="Batch_Data"
    )

    create_dynamodb.create_table(
        table_name='Sales',
        atr_1='Order ID',
        atr_2='Product',
        tags="Sales_April_2019"
    )
 
    """ Batch write to dynamodb """
    csv_object = get_object(bucket_name='dynamo-to-lambda-csv', path='koji-info.csv')
    df = pd.read_csv(io.BytesIO(csv_object))
    table_name = dynamodb.Table('register')   
    with table_name.batch_writer() as batch:
        for i, row in df.iterrows():
           batch.put_item(Item=row.to_dict())
    print("DynamoDB put_items completed")  

    """ Batch write to dynamodb  for the sales table"""
    salse_object = get_object(bucket_name='dynamo-to-lambda-csv', path='Sales_April_2019.csv')
    df_salse = pd.read_csv(io.BytesIO(salse_object))
    table_name_salse = dynamodb.Table('Sales')   
    with table_name_salse.batch_writer() as batch:
        for i, row in df_salse.iterrows():
            decimal = row.to_dict()['Price Each']
            #decimal_value = json.loads(json.dumps(decimal), parse_float=Decimal)
            #decimal_value['Price Each']
            db_data = json.loads(json.dumps(decimal), parse_float=Decimal)
            batch.put_item(Item=db_data)
    print("DynamoDB put_items completed for salse")    
            
   
    # """ Batch writer object called. """
    # batch_writer = get_object(list_of_buckets='dynamo-to-lambda-csv', path='batch_write.json')
    # list_of_batch = json.loads(batch_writer)

    # response = dynamo_batch(table, list_of_batch)
    # print(response)
    
    
if __name__ == '__main__':
    main()

# Fshsh#$&vafs
# 12407819253Bk$