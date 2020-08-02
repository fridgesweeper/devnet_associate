import requests, urllib3
import json

#Obtain an authentication cookie
def get_login_cookie(host, session, username, password):
    # Disable Self-Signed Cert warning for demo
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    login_url = "https://{}/api/aaaLogin.json".format(host)
    payload = {
          "aaaUser": {
            "attributes": {
              "name": username,
              "pwd": password
               }
            }
          }
    # Obtain an authentication cookie
    print("Excuting POST", login_url)
    resp = session.post(login_url,json=payload,verify=False)
    print("Status Code:", resp.status_code, "\n")


#enable feature
def enable_feature(host, session, feature):
    
    feature_url = "https://{}/api/mo/sys/fm/{}.json".format(host, feature.lower())
    payload = {
                "fm{}".format(feature):{
                    "attributes":{
                            "adminSt":"enabled"
                            }
                    }
                }
    
    print("Excuting POST", feature_url)
    resp = session.post(feature_url, json=payload, verify=False)
    print("Status Code:", resp.status_code, "\n")


# Configure port-channel
def config_pc(host, session, pc_id, member_port):
    pc_url = "https://{}/api/mo/sys/intf.json".format(host)
    payload = {
        "interfaceEntity": {
          "children": [
            {
              "pcAggrIf": {
                "attributes": {
                  "id": pc_id,
                  "isExplicit": "no",
                  "pcMode": "active",
                  "mode": "trunk"
                },
                "children": [
                  {
                    "pcRsMbrIfs": {
                      "attributes": {
                        "isMbrForce": "yes",
                        "tDn": "sys/intf/phys-[{}]".format(member_port)
                      }
                    }
                  }
                ]
              }
            },
            {
              "l1PhysIf": {
                "attributes": {
                  "id": member_port
                }
              }
            }
          ]
        }
      }
    print("Excuting POST", pc_url)
    resp = session.post(pc_url, json=payload, verify=False)
    print("Status Code:", resp.status_code, "\n")
    print("Response:\n", resp.json())
    
# Configure VPC domain
def config_vpc_domain(host, session, vpc_domain_id, source_ip, destination_ip, vrf):
    vpc_url = "https://{}/api/mo/sys/vpc/inst.json".format(host)
    
    payload = {
    "vpcInst": {
    "children": [
      {
        "vpcDom": {
          "attributes": {
            "id": vpc_domain_id,
            "autoRecovery": "enabled",
            "grcflCnstncyChck": "enabled",
            "peerGw": "enabled",
            "peerSwitch": "enabled",
        },
        "children": [
        {"vpcKeepalive":
            {"attributes":
                {"destIp":destination_ip,
                 "srcIp":source_ip,
                 "vrf":vrf
    }}}]}}]}}
    
    print("Excuting POST", vpc_url)
    resp = session.post(vpc_url, json=payload, verify=False)
    print("Status Code:", resp.status_code, "\n")
    print("Response:\n", resp.json())
    

# Configure VPC peer link
def config_vpc_pl(host, session, pl_id):
    vpc_pl_url = "https://{}/api/node/mo/sys/vpc/inst/dom.json".format(host)
    payload = {
      "vpcKeepalive": {
        "children": [
          {
            "vpcPeerLink": {
              "attributes": {
                "id": pl_id
              }
            }
          }
        ]
      }
    }
    
    print("Excuting POST", vpc_pl_url)
    resp = session.post(vpc_pl_url, json=payload, verify=False)
    print("Status Code:", resp.status_code, "\n")
    print("Response:\n", resp.json())
    
session = requests.Session()    
host = '192.168.3.125'
username = "admin"
password = "admin"


#获取登陆的cookie
#get_login_cookie(host, session, username, password)

#启用相关的feature
#enable_feature(host, session, "Lacp")
#enable_feature(host, session, "Vpc")

#创建vpc domain，配置PKL
#config_vpc_domain(host, session, "10", "192.168.3.124", "192.168.3.125", "management")

#创建port channel，并将接口划入
#config_pc(host, session, "po10", "eth1/5")
#config_pc(host, session, "po10", "eth1/6")

#config_pc(host, session, "po30", "eth1/8")
#config_pc(host, session, "po30", "eth1/9")

#配置peerlink
#config_vpc_pl(host, session, "po10")














