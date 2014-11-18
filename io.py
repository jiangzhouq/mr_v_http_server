#!/usr/bin/python
fo = open("/etc/shadowsocks/foo.json", "wb")
str1 = "pwpwpw"
num = "8888"
fo.write("{\n\t\"server\":\"106.186.22.172\",\n\t\"server_port\":"+ num +",\n\t\"password\":\""+ str1 +"\",\n\t\"timeout\":300,\n\t\"method\":\"rc4-md5\"\n}")
fo.close()
