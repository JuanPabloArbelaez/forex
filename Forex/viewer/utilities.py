import requests
import json


def get_json_data(url):
    try:
        r = requests.get(url)
        if r.status_code is 200:
            return r.json()
        else:
            return None
    except requests.exceptions.ConnectionError:
        return None


def loop_through_dict(dictionary, added_value):
    for k, v in dictionary.items():
        v = add_value(v, added_value)
        dictionary[k] = v
        dictionary[k] = check_category(k, v)


def add_value(v, added_value):
    print(v)
    v += added_value
    print(v)
    return v


def check_category(k, v):
    if k == 'HKD' or is_even(v):
        v = (v, 'table-danger')
    else: 
        v = (v, None)

    return v


def is_even(number):
    return number % 2 == 0