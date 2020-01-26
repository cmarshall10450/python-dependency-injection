import requests
import json

class HttpService:
  def __init__(self, config):
    self._config = config or {}

  def set_header(self, header, value):
    if not 'headers' in self._config:
      self._config['headers'] = {}

    self._config['headers'][header] = value
    return self


  def set_headers(self, headers):
    for header in headers:
      for k, v in header.items():
        self.set_header(k, v)
    return self


  def get(self, url):
    response = requests.get(url)
    return response.json()


  def post(self, url, data = None):
    return requests.post(url, data=data)