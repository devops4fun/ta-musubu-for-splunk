# Musubu IP Threat Data for Splunk Overview

Use Musubu’s unique IP & Network cyber threat scoring and profiling API right in your Splunk instance to determine the following for each IP:
* Cyber Threat Score: A 0-100 rating of how much of a cyber threat the IP may be based on the output of our analytics and algorithms.
* Cyber Threat Classification: High-Medium-Nuisance-Low rating of an IPs cyber threat potential for quick identification.
* Blacklist Class: The predominant cyber threat vector seen as associated with the IP address (e.g. Phishing, Ransomware, TOR, etc.).
* Blacklist Count: The number of major IP blacklisting services that have blacklisted the IP address.
* Blacklist Neighbors: The number of other IP addresses in the same subnet that have been blacklisted.
* Blacklist Count: The number of times in the last 90 days the IP address has been blacklisted.

## Musubu IP Threat Data Tooltip in Splunk 

Simply add one or more data sources to the Musubu Add-on and then you will be able to mouse over each IP address to see our threat profiling data. Use it to perform faster threat detection, threat identification, response, and mitigation.

## Custom Command => showipthreatdata 
Leverage the “showipthreatdata” custom command within to add-on to make direct calls to the Musubu API from the Splunk search view. See example below - Musubu results for the specified IP are returned in a Tableview.

*Syntax: | showipthreatdata ipaddress*

To use the Musubu add-on, install from Splunkbase, then:
Purchase a Musubu API “Small Plan” or higher from https://musubu.io/api-pricing/
Once you receive your API Key, respond back to our support@musubu.io alias with your Splunk IP address for whitelisting.
Open the configuration for the Musubu Add-on and set the following configurations:
Step 1. Enter your Unique API Key as shown below and click “Save”
Step 2. Create and configure an input using a sample ipv4 address
Step 3. Verify the input is functional

Step 1. Enter API Key
Step 2. Create and configure an Input. Click “Add” to save the new input.
Step 3. Verify Musubu Input is functional by searching the applicable index.

Details

System requirements:

Splunk version 6.3 or greater
Windows, Linux or Mac OS operating system
Installation

App installation requires admin privileges.

Navigate to "Manage apps" and click "Install app from file"
Upload the app bundle


Troubleshooting
API Key is required
In order to use Musubu’s IP & network cyber threat profiling per IP address in Splunk, you must have a valid Musubu API “Small Plan” subscription or higher: https://musubu.io/api-pricing/

Error Codes

View Musubu for Splunk add-on logs at the following location:
SPLUNK_HOME/system/var/log

Logs files related to the add-on have the following syntax: ta-musubu-for-splunk-somecomponent.log

Errors pertaining to the Musubu custom command “| showipthreatdata ipaddress” will display verbosely in the web console.

Release Notes
Version 1.0.0
December 5, 2018
- Initial Release

BUILT BY
Musubu
CATEGORY & CONTENTS
Categories: Security, Fraud, and Compliance
App Type: App
App Contents: Alert Actions
COMPATIBILITY
Products: Splunk Cloud, Splunk Enterprise
Splunk Versions: 7.1, 7.0, 6.6, 6.5, 6.4, 6.3
Platform: Platform Independent
LICENSING
Musubu API License
SUPPORT
Musubu Supported at support@musubu.io
