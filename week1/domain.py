def ping():
    global ip
    ip -= 1
    print(ip)
    
ip = 2
ping()
print(ip)
