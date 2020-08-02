import requests, urllib3
import json

# Disable Self-Signed Cert warning for demo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Assign requests.Session instance to session variable
session = requests.Session()

host = '192.168.3.124'

login_url = "https://" + host + "/api/aaaLogin.json"
payload = {
          "aaaUser": {
            "attributes": {
              "name": "admin",
              "pwd": "admin"
               }
            }
          }
# Obtain an authentication cookie
session.post(login_url,json=payload,verify=False)


vpc_url = "https://" + host + "/api/node/mo/sys/vpc/inst/dom.json"

payload = {
  "vpcDom": {
    "attributes": {
      #"autoRecovery": "enabled",
      #"delayRestoreSVI": "333",
      #"excludeSVI": "555",
      #"grcflCnstncyChck": "enabled",
      "id": "10",
      #"peerGw": "enabled",
      #"peerSwitch": "enabled",
      #"rolePrio": "222",
      #"sysMac": "00:03:00:04:00:05",
      #"sysPrio": "111"
    },
    "children": [
      {
        "vpcKeepalive": {
          "attributes": {
                        "destIp": "192.168.3.123",
                        "srcIp": "192.168.3.124",
                        "vrf": "management"
                        }
                        }
}]}}

resp = session.post(vpc_url,json=payload, verify=False)

#查看vpc配置
vpc_url = "https://" + host + "/api/node/mo/sys/vpc/inst/dom.json?rsp-subtree=full"
resp = session.get(vpc_url, verify=False)
resp_json = resp.json()
print(json.dumps(resp_json, indent=4))


