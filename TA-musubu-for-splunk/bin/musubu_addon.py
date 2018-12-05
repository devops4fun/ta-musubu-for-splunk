import sys
import os
import json
import time


dir = os.path.join(util.get_apps_dir(), 'bin', 'ta_musubu_for_splunk')
if not dir in sys.path:
sys.path.append(dir)

# # read the local musubu config file to get api key value
# def get_api_key():
#     musubu_settings_file = 'ta_musubu_for_splunk_settings.conf'
#     musubu_settings_file_fh = op.join(app_root, 'local', musubu_settings_file)
#     if not op.isfile(musubu_settings_file_fh):
#         raise RuntimeError("musubu_settings_file/%s doesn't exist" % musubu_settings_file_fh)
#     musubu_settings_file_fh.open(musubu_settings_file,'r')
#     lines = musubu_settings_file_fh.readlines()
#     for line in lines:
#         line_part = line.split(' ')
#         if line_part[0] == 'api_key':
#             return line_part[2]

import splunk.util as sutil

from splunktaucclib.global_config import GlobalConfig
global_config = GlobalConfig()
settings = global_config.settings.load()

from musubu_logger import *

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        start = time.time()
        print("musubu settings: %s " % settings)

def main():
    pass

if __name__ == "__main__":
    main()
