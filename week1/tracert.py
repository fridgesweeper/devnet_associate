
cmd = input("d:\python_work>")

result = """
  1     1 ms     1 ms     1 ms  192.168.3.1
  2     2 ms     1 ms     1 ms  192.168.1.1
  3     4 ms     3 ms     2 ms  10.70.0.1
  4     5 ms     4 ms     3 ms  125.34.174.221
  5    12 ms     6 ms     6 ms  124.65.194.189
  6   224 ms    37 ms     *     219.158.15.34
  7    93 ms    89 ms   100 ms  219.158.24.126
  8    61 ms    66 ms    77 ms  219.158.98.94
  9   215 ms   238 ms   254 ms  219.158.96.234
 10   239 ms   214 ms   204 ms  173.205.56.181
 11   248 ms   229 ms   220 ms  89.149.128.174
 12   220 ms   205 ms     *     69.174.7.78
 13   244 ms   229 ms   197 ms  1.1.1.1

跟踪完成。
"""

if 'tracert' in cmd:
    ip = cmd.split()[2]
    print("\n通过最多 30 个跃点跟踪到 {} 的路由\n".format(ip))
    print(result)
else:
    print("这个程序只能traceroute")





