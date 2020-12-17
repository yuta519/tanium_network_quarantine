# coding: utf-8
import sys

import requests
import json


def parseQuestion(session_id, hostname):
    """Fetch group defined information."""
    url = hostname + '/api/v2/parse_question?json_pretty_print=1'
    payload = {
        'text': 'Get Computer Name contains computer from all machines with Computer Name equals computer'
    }
    headers = {
        'Session': session_id,
        'content-type': "application/json"
    }
    response = requests.post(
        url,
        json.dumps(payload),
        headers=headers,
        verify=False
    )
    if response:
        pass
    else:
        print(response.text)
        sys.exit()
    question_data = response.json()
    group_defined_info = question_data['data'][0]['group']['sub_groups'][0]
    return group_defined_info

def getPackages(session_id, hostname):
    """Fetch quarantine action packages."""
    url = hostname + '/api/v2/packages/by-name/Apply Windows IPsec Quarantine'
    headers = {
        'content-type': 'application/json',
        'Session': session_id
    }
    response = requests.get(url, headers=headers, verify=False)
    packages = response.json()
    return packages['data']['id']

def quarantine(session_id, target_group, source_id, hostname, computer_name):
    """Quarantine execution to target computer."""
    url = hostname + '/api/v2/actions'
    payload = {
        "action_group":{"name":"All computers"},
        "name":"Quarantine ["+computer_name+ "] by AIM" ,
        "target_group": target_group,
        "package_spec":{
            "source_id": source_id
        },
        "expire_seconds":780
    }
    headers = {
        'Content-type': 'application/json',
        'Session': session_id
    }
    response = requests.post(
        url,
        json.dumps(payload),
        headers=headers,
        verify=False
    )
    response = response.json()
    print("実行結果")
    print("ID :  "+str(response['data']['id']))
    print("コンピュータ名 : "+computer_name)
    print("ステータス : 実行中")
    # print("アクション名 :  "+response['data']['name'])
    # print("パッケージ :  "+response['data']['package_spec']['name'])
    # if response['data']['status'] == 'Pending':
    #     print('ステータス : 実行中')
    # else:
    #     print('コマンド実行が失敗しました')