import os

import requests as requests
from flask import Flask, request

import func


class Func:
    def __init__(self):
        self.api_server = os.environ.get('_API_SERVER')
        self.left_path = os.environ.get('_LEFT')
        self.right_path = os.environ.get('_RIGHT')

        print('INPUTS:')
        print('\t_API_SERVER: ', self.api_server)
        print('\t_LEFT: ', self.left_path)
        print('\t_RIGHT: ', self.right_path)

    def run(self, arg, uid):
        ret = func.run(arg)
        if func.check(ret):
            path = self.left_path
        else:
            path = self.right_path
        next_url = self.api_server + '/api/funcs/' + path + '/' + uid
        return next_url, ret

    def post_result(self, tup):
        response = requests.put(tup[0], data=tup[1])
        if response.status_code == 200:
            print('Call next function was successful!')
            print(response.text)
        else:
            print('Call next function failed with status code:', response.status_code)


def get_arg_from_env():
    return os.environ.get('_ARG')


app = Flask(__name__)
f = Func()


@app.route('/<uid>', methods=['POST'])
def user_info(uid):
    raw_data = request.data.decode()

    f.post_result(f.run(raw_data, uid))
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
