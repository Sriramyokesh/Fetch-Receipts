from flask import Flask, jsonify, request
import math
import uuid
app = Flask(__name__)
dictionary = {}

@app.route('/')
def welcome():
    return 'Hello from Sri Ram', 200

@app.route('/receipts/process', methods=['POST'])
def post_receipts():								# POST Responder

	'''
	Process a receipt, calculates points, generate a unique id, store points locally and return the id.
	Doesn't store the receipt details locally, as it would lead to more memory usage. 
	It is assumed that receipt details are stored in another module (of the same application).
	This module is used to calculate and store points. 
	The returned 'id' can be used as a primary key to store the receipt details in another database.
	'''
	
	data = request.json								# Request Data Payload Extraction
	id = uuid.uuid1()								# Unique Id generator based on UUID. Can use company standard methods
	points = 0
	rName = data['retailer']
	total = float(data['total'])
	date = data['purchaseDate']
	day = int(date[-3:])
	time = data['purchaseTime']
	hour = int(time[:2])
	items = data['items']
	
	for i in rName:
		points += 1 if i.isalnum() else 0			# One point for every alphanumeric character in the retailer name
	for i in items:
		points += math.ceil(float(i['price']) * 0.2) if len(i['shortDescription'].strip()) % 3 == 0 else 0	# item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer
	points += 50 if total % 1 == 0 else 0			# 50 points if the total is a round dollar amount with no cents
	points += 25 if total % 0.25 == 0 else 0		# 25 points if the total is a multiple of 0.25
	points += 5 * (len(items)//2)					# 5 points for every two items on the receipt, // operator ensures floor
	points += 10 if hour == 14 or hour == 15 else 0	# 10 points if the time of purchase is after 2:00pm and before 4:00pm
	points += 6 if day % 2 == 1 else 0				# 6 points if the day in the purchase date is odd
	
	global dictionary
	dictionary[str(id)] = points					# Store the points locally
	return jsonify({ 'id': id}), 200

@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
	
	'''
	Used to Process Get Requests
	Checks for the presence of given id
	If present, returns the corresponding number of points for the id
	Else, returns invalid id
	'''
	
	global dictionary
	if id in dictionary:
		return jsonify({ 'points': dictionary[id]}), 200
	return "Invalid ID", 400


if __name__ == "__main__":
    app.run(debug=True)
