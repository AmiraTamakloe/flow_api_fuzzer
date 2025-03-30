import requests

def post_request(path, object):
    headers = {"Content-Type": "application/json"}
    return requests.post(path, data=object, headers=headers)

def get_request(path):
    headers = {"Content-Type": "application/json"}
    return requests.get(path, headers=headers)

def put_request(path, object):
    headers = {"Content-Type": "application/json"}
    return requests.put(path, data=object, headers=headers)

def delete_request(path):
    headers = {"Content-Type": "application/json"}
    return requests.delete(path, headers=headers)

def patch_request(path, object):
    headers = {"Content-Type": "application/json"}
    return requests.patch(path, data=object, headers=headers)

