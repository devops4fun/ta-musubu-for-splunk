import sys, os
import splunk.Intersplunk as intersplunk #used to get data to splunk
import json
import requests as req
# import ta_musubu_for_splunk_declare
# from ta_musubu_for_splunk.ta_musubu_for_splunk_custom_logger import setupLogger

# dir = os.path.join(os.environ["SPLUNK_HOME"], 'etc', 'apps', 'TA-musubu-for-splunk', 'bin', 'ta_musubu_for_splunk')

myip = sys.argv[1]
if not myip:
    results = intersplunk.generateErrorResults("Please inlcude an IPv4 address when running this command")
# read the local musubu config file to get api key value
def get_api_key():
    musubu_settings_file = os.path.join(os.environ["SPLUNK_HOME"], 'etc', 'apps', 'TA-musubu-for-splunk', 'local', 'ta_musubu_for_splunk_settings.conf')
    musubu_settings_file_fh = open(musubu_settings_file,'r')
    lines = musubu_settings_file_fh.readlines()
    for line in lines:
        line_part = line.split(' ')
        if line_part[0] == 'api_key':
            return line_part[2]

user_api_key = get_api_key()

def musubu_api_call(RequestURL, parameters):
    try:
        response = req.get(RequestURL, params=parameters)
        if response.status_code != 200:
            print('Status: ', response.status_code, 'Headers: ', response.headers, 'Error Response: ', response.json())
            sys.exit(1)
        else:
            data = response.json()
            return json.dumps(data, sort_keys=True)
    except req.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

def get_ip_threat_data_full(api_key, myip):
    threat_data = []
    opt_ip = myip
    RequestURL = 'https://api.musubu.io/MusubuAPI/Musubu?'
    parameters = {'IP': opt_ip, 'key': api_key.strip(), 'format': 'json', 'level': 'verbose'}
    ip_threat_data = musubu_api_call(RequestURL, parameters)
    data = json.loads(ip_threat_data)
    threat_data.append(data)
    return threat_data
    # print(type(data))
    #for item in data:
    #     print("key: %s ==> value: %s" % (item, data[item]))

musubu_threat_data = get_ip_threat_data_full(user_api_key, myip)

#send results to splunk via intersplunk; catch any exceptions
try:
    intersplunk.outputResults(musubu_threat_data)
except:
    import traceback
    stack =  traceback.format_exc()
    results = intersplunk.generateErrorResults("Error : Traceback: " + str(stack))
