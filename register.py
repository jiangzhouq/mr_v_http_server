import web
import json
import MySQLdb
import random
import os

urls = (
    '/', 'index'
)

def createPort():
	db = MySQLdb.connect(host="localhost",user="root",passwd="biu1biu2biu3",db="mr_v",charset="utf8")
        cursor = db.cursor()
#  	portNum = random.randint(4000, 10000)
	portNum = 38
	sqlPortSearch = "SELECT * FROM user \
	       WHERE port = '%d'" % (portNum)
	try:
		cursor.execute(sqlPortSearch)
		print cursor
		results = cursor.fetchall()
		print results
		if(len(results) > 0):
			print "port repeated", portNum
#			createPort()
		else:
			print "port create ok", portNum
			return portNum
	except:
		print "cursor execute failed"
	return 0
class index:
	def POST(self):
		i = web.input()
		data=web.data()
		d1 = json.dumps(i,sort_keys=True,indent=4)
		decodejson = json.loads(d1)
		print decodejson['name']
		pyDict = {'one':1,'two':2}
                web.header('Content-Type', 'application/json')
                print 'GET returned'
                return json.dumps(pyDict)


	def GET(action):
		i = web.input()
		data = web.data()
		act = i.get("action")
		email = i.get("email")
		name = i.get("name")
		pw = i.get("pw")
		code = i.get("code")

		if int(act) == 1:
			db = MySQLdb.connect(host="localhost",user="root",passwd="biu1biu2biu3",db="mr_v",charset="utf8")
			cursor = db.cursor()
			num = createPort()
			sql = "INSERT INTO user(name, \
			       pw, email, code, port) \
			       VALUES ('%s', '%s', '%s', '%s' ,'%d')" % \
			       (name ,pw ,email ,code, num)
			try:
			   cursor.execute(sql)
			   db.commit()
			   print "insert successfully : name :", name, "pw:", pw, "email:", email, "code", code, "port:" , num
			except:
			   db.rollback()
			   print "insert failed: name :", name, "pw:", pw, "email:", email, "code", code, " port:", num
			db.close()

			fo = open("/etc/shadowsocks/" + name + ".json", "wb")
			fo.write("{\n\t\"server\":\"106.186.22.172\",\n\t\"server_port\":"+ str(num) +",\n\t\"password\":\""+ pw +"\",\n\t\"timeout\":300,\n\t\"method\":\"rc4-md5\"\n}")
			fo.close()
			os.system("ss-server -c /etc/shadowsocks/" + name + ".json" + " -f ~/pid/" + name + ".pid")
			print "action = 1"
		elif int(act) == 2:
			arr=[]
			n = cursor.execute("select * from category")
			arr = list(cursor.fetchall())
			dict1 = {"category":arr}
			return json.dumps(dict1,sort_keys=True)
			print "action = 2"
		elif int(act) == 3:
			arr = []
			n = cursor.execute("select * from  pics")
			arr = list(cursor.fetchall())
			dict1 = {"pics":arr}
			return json.dumps(dict1,sort_keys=True)
			print "action = 3"
		else:
			print "else"
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
