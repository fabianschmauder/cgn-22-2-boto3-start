import boto3
client = boto3.client('s3')

def upload_file_to_every_bucket(filename):
    for bucket in client.list_buckets()["Buckets"]:
        client.put_object(Bucket= bucket["Name"], Body= filename, Key=filename )

upload_file_to_every_bucket("some-test-file.json")