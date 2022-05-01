""" This function is use to list all user's in account. """
from ast import Expression
import boto3
from pprint import pprint

session = boto3.session.Session()
client = session.client("iam")
resource = session.resource("iam")

def list_users():
    response = client.list_users().get('Users')
    return response


def main():
    all_users = list_users()
    users = [user['UserName'] for user in all_users]
    pprint(users)

if __name__ == "__main__":
    main()    