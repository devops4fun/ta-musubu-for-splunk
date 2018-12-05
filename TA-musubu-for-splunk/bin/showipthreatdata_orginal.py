import sys, os
import splunk.Intersplunk as intersplunk #used to get data to splunk
import json
import requests as req
import ta_musubu_for_splunk_declare
from musubu_add_on_logger import setupLogger

dir = os.path.join(os.environ["applications"], 'etc', 'apps', 'TA-musubu-for-splunk', 'bin', 'ta_musubu_for_splunk')

log = setupLogger('showipthreatdata')
log.info("showipthreatdata custom command script has started")
log.info("working directory is: %s" % dir)

# read the local musubu config file to get api key value
def get_api_key():
    musubu_settings_file = os.path.join(os.environ["applications"], 'etc', 'apps', 'TA-musubu-for-splunk', 'local', 'ta_musubu_for_splunk_settings.conf')
    musubu_settings_file_fh = open(musubu_settings_file,'r')
    lines = musubu_settings_file_fh.readlines()
    for line in lines:
        line_part = line.split(' ')
        if line_part[0] == 'api_key':
            return line_part[2]

user_api_key = get_api_key()
if not user_api_key:
    log.info('no api key found')
else:
    log.info('api key => %s' % user_api_key)

def musubu_api_call(RequestURL, parameters):
    try:
        response = req.get(RequestURL, params=parameters)
        if response.status_code != 200:
            print('Status: ', response.status_code, 'Headers: ', response.headers, 'Error Response: ', response.json())
            sys.exit(1)
        data = response.json()
        return json.dumps(data)
    except req.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

def get_ip_threat_data_full(api_key):
    threat_data = []
    opt_ip = '1.0.63.100'
    RequestURL = 'https://api.musubu.io/MusubuAPI/Musubu?'
    parameters = {'IP': opt_ip, 'key': api_key.strip(), 'format': 'json', 'level': 'verbose'}
    ip_threat_data = musubu_api_call(RequestURL, parameters)
    data = json.loads(ip_threat_data)
    for item in data:
        threat_data.append(item)
    return threat_data

musubu_threat_data = get_ip_threat_data_full(user_api_key)

#send results to splunk via intersplunk; catch any exceptions
try:
    intersplunk.outputResults(musubu_threat_data)
except:
    import traceback
    stack =  traceback.format_exc()
    results = splunk.Intersplunk.generateErrorResults("Error : Traceback: " + str(stack))
