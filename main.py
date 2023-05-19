import os

import requests as requests

import func

if __name__ == '__main__':
    api_server = os.environ.get('_API_SERVER')
    pod_url = os.environ.get('_POD_URL')
    left_path = os.environ.get('_LEFT')
    right_path = os.environ.get('_RIGHT')
    uid = os.environ.get('_UID')
    arg = os.environ.get('_ARG')

    ret = func.run(arg)
    if func.check(ret):
        path = left_path
    else:
        path = right_path
    url = api_server + '/' + left_path + '/' + uid
    response = requests.post(url + "/" + uid, data=ret)
    if response.status_code == 200:
        print('Request was successful!')
        print(response.text)
    else:
        print('Request failed with status code:', response.status_code)
    response = requests.delete(pod_url)
