#!/usr/bin/env python

import json
import requests
from requests.auth import HTTPBasicAuth
from time import sleep

TOWER_IP='10.42.0.42'
USERNAME='admin'
PASSWORD='kXtKsGuyjajh'
JOB_TEMPLATE_ID='46'


NEXUS_REPO_URL='http://54.169.3.13:8081/repository/demo'
STAGE='sit'

URL='http://' + TOWER_IP + '/api/v1/job_templates/' + JOB_TEMPLATE_ID + '/launch/'
payload = {'extra_vars': 'nexus_repo_url: '+ NEXUS_REPO_URL + ' \nstage: ' + STAGE}

headers = {'Content-type': 'application/json'}
r = requests.post(URL, 
                    data=json.dumps(payload),
                    headers=headers,
                    auth=HTTPBasicAuth(USERNAME, PASSWORD))
job_url = 'http://' + TOWER_IP + r.json()['url']

print job_url

while True:

    r = requests.get(job_url,
                        auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()

    status = r['status']
    print 'Job Status: ' + status

    if status in ['successful', 'failed']:
        break
    else:
        sleep(5)


