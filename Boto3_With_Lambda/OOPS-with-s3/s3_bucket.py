"""This module provide functions to create, list, delete and view objects in s3. """

import boto3 
from pprint import pprint

session = boto3.session.Session()
resource = session.resource(region_name="us-east-1",service_name="s3")
client = session.client(service_name="s3")

class S3_Buckets(object):
    """ The class is contains s3 objects like. 

        list buckets, Create buckets, delete buckets. 
        list all s3 buckets in this account if exists
    """

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name 
        """ 
        Parameters: 
        str: bucket_name
        """

    def list_buckets(self):
        """ List all s3 buckets in this account. 

        Parameters:
        None
        
        Returns:
        list: The list of all buckets 
        """
        # count = 1
        # buck_dict = {}
        list_of_buckets = client.list_buckets()['Buckets']
        print(list_of_buckets)
        # list_buckets = [buckets['Name'] for buckets in list_of_buckets]
        # for each_times in list_buckets:
        #     buck_dict["bucket_name"+str(count)]= each_times
        #     count +=1    
        # return list_buckets

    def create_bucket(self, bucket_name):
        self.bucket_name = bucket_name
        
        """ Create bucket if not exist. 
        
        Parameters:
        str: Provide a bucket name

        Return:
        str: Create bucket name
        """
        try: 
            if self.bucket_name not in self.list_of_buckets:
                client.create_bucket(
                    Bucket= self.bucket_name
                    )
                return f"Creating bucket with name {self.bucket_name}"
            else:
                return f"bucket with name {self.bucket_name} already exist"
        except Exception as e:       
            print(e)
        return None    
        

def main(): 
    s3_bucket = S3_Buckets('')
    #list_buckets = s3_bucket.list_buckets()
    create_buckets = s3_bucket.create_bucket("ecs.terraform.cluster.terraform")
    print(create_buckets)
    #print(list_buckets)

if __name__ == '__main__':
    main()