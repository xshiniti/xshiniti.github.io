import requests
from urllib.parse import urlencode

APP_ID = '9708d34a960548109649a54b402f2581'
AUTH_URL = 'https://oauth.yandex.ru/authorize'

auth_data = {
  'response_type' : 'token',
  'client_id' : 'APP_ID'
}

print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = 'AQAAAAAggdZNAATpjpe6VuT8QUowrfREWoOiZug'

# class which define user - params = 'token'
class YaMetrikaUser :
  
  def __init__(self, token):
    self.token = token
  
  
  def get_counter(self):
    headers = {
      'Authorization' : 'OAuth {}'.format(self, token)
    }
  response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', header=headers)
  return [c['id']] for c in response.json()['counters']]
  
  
  
# first_user = YaMetrikaUser(AQAAAAAggdZNAATpjpe6VuT8QUowrfREWoOiZug)
# counter = first_user.get_counter()
# print(counter)

class Counter :
  
  def __init__(self, counter_id, token):
    self.counter_id = counter_id
    self.token = token
    
    
  def get_visits(self):
    params = {
      'id' : 'self.counter_id',
      'metrics' : 'ym:s:visits'
    }
    headers = {
      'Authorization' : 'OAuth {}'.format(self.token)
    }
    response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params, header=headers)
    return response.json()['data'][0]['metrics'][0]
     
     
  def get_views(self):
    params = {
      'id' : 'self.counter_id',
      'metrics' : 'ym:s:pageviews'
    }
    headers = {
    'Authorization' : 'OAuth {}'.format(self.token)
    }
    response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params, header=headers)
    return response.json()['data'][0]['metrics'][0]
    
    
    def get_users(self):
    params = {
      'id' : 'self.counter_id',
      'metrics' : 'ym:s:users'
    }
    headers = {
    'Authorization' : 'OAuth {}'.format(self.token)
    }
    response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params, header=headers)
    return response.json()['data'][0]['metrics'][0]