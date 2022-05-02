
import requests
import requests_cache
import pandas as pd
from operator import itemgetter

requests_cache.install_cache('healthjump_cache',backend='sqlite', expire_after=180)

details = dict(
    {'auth_url' : 'https://api.healthjump.com/authenticate'
        , 'email' : 'sandbox@healthjump.com'
        , 'password' : 'R-%Sx?qP%+RN69CS'
        , 'base_url' : 'https://api.healthjump.com/hjdw/SBOX02/demographic'
        , 'secretkey' : 'yemj6bz8sskxi7wl4r2zk0ao77b2wdpvrceyoe6g'
        , "Authorization" : ''
        , 'Version' : '3.0'
        , 'params' : 'first_name starts with A or B or C'
    }
)

details_list = [(k,v) for k, v in details.items()]
authenticate = dict(itemgetter(1,2)(details_list))
auth_response = requests.post(details['auth_url'], data=authenticate).json()
if auth_response: print('Response: OK')
else: print('Response: None')
details['Authorization'] = 'Bearer {}'.format(auth_response['token'])
details_list = [(k,v) for k, v in details.items()]
demographics = dict(itemgetter(4,5,6,7)(details_list))
get_response = requests.get(details['base_url'],headers=demographics).json()

df = pd.json_normalize(get_response, record_path='data')
abc_df = df[df['first_name'].str.contains('A|B|C')]
print(abc_df)




