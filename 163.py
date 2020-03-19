#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import hashlib
from datetime import *
import json


username = "1399999999"
password = hashlib.md5(b"123456").hexdigest() 
url = "https://www.xxx.com/ajax/user_login"
form_date = {"username": username, "password": password}
login_response = requests.post(url, data=form_date)
assert login_response.text == "success"
c = login_response.cookies


def make_order():
    global c
    url = "https://www.xxx.com/ajax/create_order/"
    form_date = {"restaurant_id": 11196, "menu_items_total": "12.00",
                 "menu_items_data": "[{'id': 1653196, 'p': '2', 'q':'6'}]", "delivery_fee": "3.00"}
    make_response = requests.post(url, data=form_date, cookies=c)
    res = make_response.text
    id = json.loads(res)["order_id"]
    assert id != ""
    return id


def place_prder(id):
    global c
    global username
    time = datetime.now()+timedelta(hours=1)
    url = "https://www.xxx.com/ajax/place_order/"
    form_date = {"order_id": id, "customer_name": "xxxx", "mobile_number": username, "delivery_address": "xxxxxxx",
                 "preorder": "yes", "preorder_time": time, "pay_type": "cash"}
    place_response = requests.post(url, data=form_date, cookies=c)
    res = place_response.text
    assert res == "success"
    print("订餐成功")


def sms():
    result = ask_sms()
    if result == "{'status': 'ok', 'need_sms': Flase}":
        return
    else:
        requests_sms()
        code = get_sms()
        validate_sms(code)


def ask_sms():
    global c
    global username
    url = "https://www.xxx.com/ajax/is_order_need/"
    form_data = {"mobile": username}
    ask_respone = requests.post(url, data=form_data, cookies=c)
    res = ask_respone.text
    return res

def requests_sms():
    global c
    global username
    url = "https://www.xxx.com/ajax/common_sms_code/"
    form_data = {"mobile": username}
    sms_response = requests.post(url, data=form_data, cookies=c)
    res = sms_response.text
    assert res =="True"


def get_sms():
    global username
    url = "https://www.xxx.com/manager/login.action"
    form_data = {"user": "admin", "pwd": 000000}
    login_response = requests.post(url, data=form_data)
    cookie = login_response.cookies
    url2 = "https://www.xxx.com/manager/smsmanager"
    form_data2 = {"phone": username}
    code_response = requests.post(url2, data=form_data2, cookies=cookie)
    code = code_response.text
    assert code != ""
    return code


def validate_sms(code):
    global c
    global username
    url = "https://www.xxx.com/ajax/calidate_sms_code/"
    form = {"mobile": username, "sms_code": code}
    validate_response = requests.post(url, data=form, cookies=c)
    res = validate_response.text
    assert code == "True"


if __name__ == "__main__":
    id = make_order()
    sms()
    place_prder(id)