# -*- coding: utf-8 -*- 
import requests
import json

mURL2="http://api.thingspeak.com"
mURL="http://your-dns.com"
mAPI_KEY="your-KEY"

#http_func
class http_funcClass:

	def __init__(self):
		print ""

	def get_reqString(self, sReqParam, iType):
		ret=""
		if (iType==1):
			sParam ="/tst/ghome/wt-api.php?key=" + mAPI_KEY
			sParam+= sReqParam
			sUrl= mURL + sParam
			ret=sUrl
		if (iType==2):
			# sParam ="/update?key=" + mAPI_KEY
			sParam ="/update?key=" + mAPI_KEY
			sParam+= sReqParam
			sUrl= mURL2 + sParam
			ret=sUrl
		return ret
		
#	def send_push(self, sReqParam ):
	def send_push(self, sReqParam , iType):
		#sRet=""
		if (len(sReqParam ) < 1):
			print("Error, aReq.len=" + str(len(sReqParam ) ))
			return
		sUrl =self.get_reqString(sReqParam, iType)
#		sParam ="/update?key=" + mAPI_KEY
#		sUrl= mURL + sParam
		print("sUrl="+ sUrl )
		try:
#			r = requests.get(sUrl ,  timeout=30)
			r = requests.get(sUrl ,  timeout=10 )
			print r.status_code
			sText= r.text
			print sText
		except:
			print "Error, send_push"
			raise
		finally:
			print "End , send_push"
		return
		
