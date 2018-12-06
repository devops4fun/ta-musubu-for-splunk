
# encoding = utf-8

import os
import sys
import time
import datetime
import json

'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating the modular input.

# For advanced users, if you want to create single instance mod input, uncomment this method.
def use_single_instance_mode():
    return True
'''
def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    #ip = definition.parameters.get('ip', None)
    pass


''' Data Collection Logic'''
def collect_events(helper, ew):
    helper.log_info("musubu data collection has initialized")
    opt_ip = helper.get_arg('ip')
    global_api_key = helper.get_global_setting("api_key")
    url = 'https://api.musubu.io/MusubuAPI/Musubu?'
    method = 'GET'
    params = {'IP': opt_ip, 'key': global_api_key, 'format': 'json', 'level': 'verbose'}
    helper.log_info(global_api_key)
    # The following examples send rest requests to some endpoint.
    response = helper.send_http_request(url, method, parameters=params)
    r_data = response.json()
    event_data = json.dumps(r_data, sort_keys=True, indent=4)

    r_status = response.status_code
    if r_status == 200:
        helper.log_info("musubu api call made successfully...payload below")
        helper.log_info(r_data)

    def write_api_key_to_tooltip_file(old_string, new_string):
        filename = os.path.join(os.environ["SPLUNK_HOME"], 'etc', 'apps', 'TA-musubu-for-splunk', 'appserver', 'static', 'musubu_tooltip.js')
        with open(filename) as f:
            s = f.read()
            if old_string not in s:
                helper.log_info("Oops! Unable to locate %s in %s" %(old_string, filename))
                helper.log_info("global API Key was not written to the tooltip")
            else:
                # Safely write the changed content, if found in the file
                with open(filename, 'w') as f:
                    helper.log_info("Writing global API Key to tooltip file: %s" % filename)
                    s = s.replace(old_string, new_string)
                    f.write(s)
                    
    write_api_key_to_tooltip_file('placeholder', global_api_key)

    musubu_checkpoint_file = os.path.join(os.environ["SPLUNK_HOME"], 'etc', 'apps', 'TA-musubu-for-splunk', 'bin', 'musubu_checkpoint', 'musubu_checkpoint_file.txt')
    helper.log_info(musubu_checkpoint_file)

    def write_event(data):
        event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=data, unbroken=True, done=True)
        ew.write_event(event)
        helper.log_info("musubu_api_data event written successfully!")

    def checkpoint(musubu_checkpoint_file, opt_ip):
        with open(musubu_checkpoint_file, 'r') as file:
            ip_list = file.read().splitlines()
            return(opt_ip in ip_list)

    def write_to_checkpoint_file(musubu_checkpoint_file, opt_ip):
        with open(musubu_checkpoint_file, 'a') as file:
            file.writelines(opt_ip + '\n')

    def stream_to_splunk(musubu_checkpoint_file, data):
        for item in data:
            if checkpoint(musubu_checkpoint_file, str(data['ipaddress'])):
                continue
            else:
                write_to_checkpoint_file(musubu_checkpoint_file, str(data['ipaddress']))
                write_event(json.dumps(data))

    stream_to_splunk(musubu_checkpoint_file, r_data)

    '''
    """Implement your data collection logic here"""

    # The following examples get the arguments of this input.
    # Note, for single instance mod input, args will be returned as a dict.
    # For multi instance mod input, args will be returned as a single value.
    opt_ip = helper.get_arg('ip')
    # In single instance mode, to get arguments of a particular input, use
    opt_ip = helper.get_arg('ip', stanza_name)

    # get input type
    helper.get_input_type()

    # The following examples get input stanzas.
    # get all detailed input stanzas
    helper.get_input_stanza()
    # get specific input stanza with stanza name
    helper.get_input_stanza(stanza_name)
    # get all stanza names
    helper.get_input_stanza_names()

    # The following examples get options from setup page configuration.
    # get the loglevel from the setup page
    loglevel = helper.get_log_level()
    # get proxy setting configuration
    proxy_settings = helper.get_proxy()
    # get account credentials as dictionary
    account = helper.get_user_credential_by_username("username")
    account = helper.get_user_credential_by_id("account id")
    # get global variable configuration
    global_api_key = helper.get_global_setting("api_key")

    # The following examples show usage of logging related helper functions.
    # write to the log for this modular input using configured global log level or INFO as default
    helper.log("log message")
    # write to the log using specified log level
    helper.log_debug("log message")
    helper.log_info("log message")
    helper.log_warning("log message")
    helper.log_error("log message")
    helper.log_critical("log message")
    # set the log level for this modular input
    # (log_level can be "debug", "info", "warning", "error" or "critical", case insensitive)
    helper.set_log_level(log_level)

    # The following examples send rest requests to some endpoint.
    response = helper.send_http_request(url, method, parameters=None, payload=None,
                                        headers=None, cookies=None, verify=True, cert=None,
                                        timeout=None, use_proxy=True)
    # get the response headers
    r_headers = response.headers
    # get the response body as text
    r_text = response.text
    # get response body as json. If the body text is not a json string, raise a ValueError
    r_json = response.json()
    # get response cookies
    r_cookies = response.cookies
    # get redirect history
    historical_responses = response.history
    # get response status code
    r_status = response.status_code
    # check the response status, if the status is not sucessful, raise requests.HTTPError
    response.raise_for_status()

    # To create a splunk event
    helper.new_event(data, time=None, host=None, index=None, source=None, sourcetype=None, done=True, unbroken=True)


    # The following example writes a random number as an event. (Multi Instance Mode)
    # Use this code template by default.
    import random
    data = str(random.randint(0,100))
    event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=data)
    ew.write_event(event)

    # The following example writes a random number as an event for each input config. (Single Instance Mode)
    # For advanced users, if you want to create single instance mod input, please use this code template.
    # Also, you need to uncomment use_single_instance_mode() above.
    import random
    input_type = helper.get_input_type()
    for stanza_name in helper.get_input_stanza_names():
        data = str(random.randint(0,100))
        event = helper.new_event(source=input_type, index=helper.get_output_index(stanza_name), sourcetype=helper.get_sourcetype(stanza_name), data=data)
        ew.write_event(event)
    '''
