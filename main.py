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
    print('INPUTS:')
    print('\t_API_SERVER: ', api_server)
    print('\t_SELF: ', pod_uid)
    print('\t_LEFT: ', left_path)
    print('\t_RIGHT: ', right_path)
    print('\t_UID: ', uid)
    print('\t_ARG: ', arg)

    ret = func.run(arg)
    if func.check(ret):
        path = left_path
    else:
        path = right_path
    next_url = api_server + '/api/funcs/' + left_path + '/' + uid
    response = requests.put(next_url, data=ret)
    if response.status_code == 200:
        print('Call next function was successful!')
        print(response.text)
    else:
        print('Call next function failed with status code:', response.status_code)
    pod_url = api_server + '/api/pods/' + pod_uid
    response = requests.delete(pod_url)
    if response.status_code == 200:
        print('Delete was successful!')
        print(response.text)
    else:
        print('Delete failed with status code:', response.status_code)
