import os

import requests as requests

import func

if __name__ == '__main__':
    api_server = os.environ.get('_API_SERVER')
    pod_uid = os.environ.get('_SELF')
    left_path = os.environ.get('_LEFT')
    right_path = os.environ.get('_RIGHT')
    uid = os.environ.get('_UID')
    arg = os.environ.get('_ARG')

    ret = func.run(arg)
    if func.check(ret):
        path = left_path
    else:
        path = right_path
    next_url = api_server + '/api/funcs/' + left_path + '/' + uid
    response = requests.put(next_url, data=ret)
    if response.status_code == 200:
        print('Request was successful!')
        print(response.text)
    else:
        print('Request failed with status code:', response.status_code)
    pod_url = api_server + '/api/pods/' + pod_uid
    response = requests.delete(pod_url)
