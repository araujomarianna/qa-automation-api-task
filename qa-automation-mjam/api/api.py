import requests
import json


def get_response(params={}, token=True):
    """
    This function gets the api response

    :param params: It receives the key and value to complete the api uri
    :type params: dict
    :param token: Authorization token
    :type token: bool
    :return: It returns a response object
    :rtype: requests.models.Response
    """
    url = "https://www.mjam.net/api/v3/restaurants/search/?"
    for param in params:
        url += "{}={}&".format(param, params[param])
    header = {}
    if token:
        header['Authorization'] = 'Token 9d5cae911bedd4bfa2831684896ffcfa716a3bce'
    response = requests.get(url, headers=header)
    return response


def get_response_data(params={}, token=True):
    """
    This function converts a json in a python object

    :param params: It receives the key and value to complete the api uri
    :type params: dict
    :param token: Authorization token
    :type token: bool
    :return: It returns a dict with the api content
    :rtype: dict
    """
    return json.loads(get_response(params, token).content)


def get_all_restaurant_info(data, info):
    """
    This function gets an info for all restaurants

    :param data: It's an API response data
    :type data: dict
    :param info: It receives a restaurant key value
    :type info: str
    :return: It returns a generator containing all the restaurants info
    :rtype: generator
    """
    for restaurant in data['restaurants']:
        yield restaurant[info]


def get_total(data):
    """
    This function returns the total number of restaurants
    :param data: API response data
    :type data: dict
    :return: It returns the total number of restaurants
    :rtype: int
    """
    return data['total']
