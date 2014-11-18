import web
import json
import MySQLdb

urls = (
    '/', 'index'
)

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
		conn = MySQLdb.connect(host="localhost",user="root",passwd="biu1biu2biu3",db="tdp",charset="utf8")
		cursor = conn.cursor()
		if int(act) == 1:
#		first = page_collection.find().sort("ctime", pymongo.DESCENDING)[0]
#		date = date_collection.find().sort("time", pymongo.DESCENDING)[0]
#		for i in pic_collection.find().sort("category", pymongo.DESCENDING):
#			arr.append({"mode":i.get('mode'), "category":i.get('category'), "name":i.get('name'), "url":i.get('url'),"istitle":i.get('istitle')})
#		dict1 = {"page":{"name":first.get('name'), "url":first.get('url'), "ctime":first.get('ctime')},"pics":arr,"date":{"time":date.get('time')}}
#		print dict1
#		return json.dumps(dict1,sort_keys=True)
			arr =[]
			n = cursor.execute("select * from time")
			arr = list(cursor.fetchall())
			dict1 = {"time":arr}
			return json.dumps(dict1,sort_keys=True)
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
