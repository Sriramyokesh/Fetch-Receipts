import requests
import json

from post_payload import post1, post2

POST_ENDPOINT = "http://127.0.0.1:5000/receipts/process"
GET_ENDPOINT = "http://127.0.0.1:5000/receipts/{0}/points"
post_res1 = {'id': 'float.inf'}
post_res2 = {'id': 'float.inf'}

try: 
	post_res1 = requests.post(url=POST_ENDPOINT, data=json.dumps(post1), headers = {"Content-Type": "application/json"})
	post_res2 = requests.post(url=POST_ENDPOINT, data=json.dumps(post2), headers = {"Content-Type": "application/json"})
except Exception as e:
	print('Error posting receipts' + str(e))

try:
	points1 = requests.get(url=GET_ENDPOINT.format(post_res1.json()['id']), headers = {"Content-Type": "application/json"})
	points2 = requests.get(url=GET_ENDPOINT.format(post_res2.json()['id']), headers = {"Content-Type": "application/json"})
	print(points1.text)
	print(points2.text)
except Exception as e:
	print('Error posting receipts' + str(e))
