"""
校验一个字符串是不是IPv6地址
"""

def valid_ipv6(ip):
    #用冒号分割字符串
    ip_split = ip.split(":")
    
    #排除少于2个冒号或者多于7个冒号
    if ip.count(":") < 2 or ip.count(":") > 7:
        return "这不是IPv6地址1"
    
    #排除3个及以上连续冒号,如3:::3, 4::::4
    elif ip.count("::") > 1 or ":::" in ip:
        return "这不是IPv6地址2"
              
    #排除不使用压缩法时，地址长度不够
    elif ip.count("::") == 0 and len(ip_split) != 8:
        return "这不是IPv6地址3"

    #排除:2::
    elif ip_split[0] == "" and ip_split[1] != "":
        return "这不是IPv6地址4"
    
    #排除::2:    
    elif ip_split[-1] == "" and ip_split[-2] != "":
        return "这不是IPv6地址5"
    
    
    else:
        #排除非16进制字符串
        try:
            str2dec = [int(value,16) for value in ip_split if value != '']
        except ValueError:
            return "这不是16进制字符串"     
    
        #判断分割的每一部分的值是否在IPv6范围内
        if any(value > 65535 for value in str2dec):
            return "这不是IPv6地址6"            
        elif any(value < 0 for value in str2dec):
            return "这不是IPv6地址7"
    
        else:
            return "这是IPv6地址"
