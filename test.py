# coding: utf-8

import os

import boto3
import pytest

dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ['DYNAMODB_ENDPOINT_URL'])


@pytest.fixture(scope='session', autouse=True)
def dynamodb_table():
    table = dynamodb.create_table(
                TableName='serverless-awsome-test', KeySchema=[{
                    'AttributeName': 'foo', 'KeyType': 'HASH',
                }], AttributeDefinitions=[{
                    'AttributeName': 'foo', 'AttributeType': 'S'
                }], ProvisionedThroughput={
                    'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10
                })
    yield table
    table.delete()


def test_dynamodb_get_set_item(dynamodb_table):
    dynamodb_table.put_item(Item={'foo': 'bar'})
    res = dynamodb_table.get_item(Key={'foo': 'bar'})
    assert 'Item' in res
