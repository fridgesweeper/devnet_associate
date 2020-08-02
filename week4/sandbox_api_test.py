import xlwt
import apicem, apicem_config


#获取网络设备的数据
resp = apicem.get(
                  apicem_config.APICEM_IP,
                  apicem_config.VERSION,
                  apicem_config.USERNAME,
                  apicem_config.PASSWORD,
                  api = "network-device"
                  )
resp_json = resp.json()
devices = resp_json["response"]

#将response保存到excel表中
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('network_devices')


#先在第一行写入header
colume = 0
for key in devices[0].keys():
    worksheet.write(0,colume,label = key)
    colume += 1


#从第二行开始写入数据
row = 0
colume = 0
for device in devices:
    row += 1
    for value in devices[row-1].values():
        worksheet.write(row, colume, label=value)
        colume += 1
    colume = 0

workbook.save("device_list.xls")

