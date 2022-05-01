import boto3 
from pprint import pprint
import csv

session = boto3.session.Session()
dynamodb = session.resource(region_name="us-east-1",service_name="dynamodb")


def create_table(table_name, atr_1, atr_2, tags):
    """ This Function is use to create dynamodb table

    Paramter:
    str()table_name: Provide bucket name
    str()atr_1: Name of First Atribute
    str()atr_2: Name of Second attribute
    strs()tags: name of tags

    Return:
    str(): table 

    """
    try:
        response = dynamodb.create_table(
            TableName = table_name,
            KeySchema = [
                {
                    'AttributeName': atr_1,
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': atr_2,
                    'KeyType': 'RANGE'
                }
                ],
                AttributeDefinitions = [
                    {
                        'AttributeName': atr_1,
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': atr_2,
                        'AttributeType': 'S'
                    }
                    ],
                    ProvisionedThroughput={
                        'ReadCapacityUnits':1,
                        'WriteCapacityUnits':1
                    },
                    Tags=[
                        {
                            'Key': 'Name',
                            'Value': tags
                        },
                    ],   
            )          
        return response
    except Exception as e:
        return e
        
'''     
def table_batch():
    tables = list(dynamodb.tables.all())
    table = dynamodb.Table('employee')
    response = tables[1].put_item(
        Item = {
            'Name': 'Koji Bello',
            'Email': 'Kojibello@gmail'
        }
    )
    with table.batch_writer() as batch:
        batch.put_item(Item={"Name": "Luzze John", "Email": "john@handson.cloud", "Department": "IT", "Section": { "QA": "QA-1", "Reporting Line": "L1" } })
        batch.put_item(Item={"Name": "Lugugo Joshua", "Email": "joshua@handson.cloud",
            "Department": "IT", "Section": { "Development": "SD-1", "Reporting Line": "L1" } })
        batch.put_item(Item={"Name": "Robert Nsamba", "Email": "robert@handson.cloud",
            "Department": "IT", "Section": { "PM": "PM-1", "Reporting Line": "L1" } })  
    return batch
'''

def dynamo_batch(dynamodb_table, s3_content):
    """ This Function is used to use to perform batch operations. 
    
    Parameters:
    tables: Table name
    bash_object: bash stript

    Return:
    str():
    """
    with dynamodb_table.batch_writer() as batch:
        # Loop through the JSON objects
        for item in s3_content:
            batch.put_item(Item=item)
    return "DynamoDB put_items completed"            

def get_table_status(table_name):
    """ This Function wait until the table exits"""
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(
        TableName=table_name
    )

    return waiter


def main():
    bucket_name = create_table(table_name="employee", 
                                atr_1="Name", 
                                atr_2="Email", 
                                tags="Employee_Table")

    print(bucket_name)
    # response = table_batch()
    # print(response)
    # return None

if __name__ == '__main__':
    main()