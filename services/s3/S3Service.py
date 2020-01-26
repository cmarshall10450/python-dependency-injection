import boto3
from base64 import b64encode

class S3Service:
  def __init__(self, config):
    self._config = config
    self.client = boto3.client("s3")
    self.resource = boto3.resource("s3")
    self.bucket = self.resource.Bucket(self._config['bucket'])


  def copy_from_local(self, src, dest):
    return self.bucket.upload_file(src, dest)

  
  def copy_from_local_binary(self, src, dest):
    with open(src, 'rb') as data:
      return self.bucket.upload_fileobj(data, dest)
  
  
  def copy_from_bytes(self, dest, data):
    bytes = data.encode("utf-8")
    return self.bucket.put_object(Key=dest, Body=bytes)