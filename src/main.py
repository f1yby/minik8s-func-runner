import os

import requests as requests

import func


class Func:
    def __init__(self):
        self.api_server = os.environ.get('_API_SERVER')
        self.pod_uid = os.environ.get('_SELF')
        self.left_path = os.environ.get('_LEFT')
        self.right_path = os.environ.get('_RIGHT')
        self.uid = os.environ.get('_UID')

        print('INPUTS:')
        print('\t_API_SERVER: ', self.api_server)
        print('\t_SELF: ', self.pod_uid)
        print('\t_LEFT: ', self.left_path)
        print('\t_RIGHT: ', self.right_path)
        print('\t_UID: ', self.uid)

    def run(self, arg):
        ret = func.run(arg)
        if func.check(ret):
            path = self.left_path
        else:
            path = self.right_path
        next_url = self.api_server + '/api/funcs/' + path + '/' + self.uid
        return next_url, ret

    def post_result(self, tup):
        response = requests.put(tup[0], data=tup[1])
        if response.status_code == 200:
            print('Call next function was successful!')
            print(response.text)
        else:
            print('Call next function failed with status code:', response.status_code)
        pod_url = self.api_server + '/api/pods/' + self.pod_uid
        response = requests.delete(pod_url)
        if response.status_code == 200:
            print('Delete was successful!')
            print(response.text)
        else:
            print('Delete failed with status code:', response.status_code)


def get_arg_from_env():
    return os.environ.get('_ARG')


if __name__ == '__main__':
    f = Func()

    f.post_result(f.run(get_arg_from_env()))
