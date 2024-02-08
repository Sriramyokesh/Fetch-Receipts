from flask import Flask, jsonify, request
import math
import uuid
app = Flask(__name__)
dictionary = {}

@app.route('/')
def welcome():
    return 'Hello from Sri Ram', 200

@app.route('/receipts/process', methods=['POST'])
def post_receipts():
	data = request.json
	id = uuid.uuid1()
	points = 0
	rName = data['retailer']
	total = float(data['total'])
	date = data['purchaseDate']
	day = int(date[-3:])
	time = data['purchaseTime']
	hour = int(time[:2])
	items = data['items']
	for i in rName:
		points += 1 if i.isalnum() else 0
	for i in items:
		points += math.ceil(float(i['price']) * 0.2) if len(i['shortDescription'].strip()) % 3 == 0 else 0
		print(points)
	global dictionary
	points += 50 if total % 1 == 0 else 0
	points += 25 if total % 0.25 == 0 else 0
	points += 5 * (len(items)//2)
	points += 10 if hour == 14 or hour == 15 else 0
	points += 6 if day % 2 == 1 else 0
	dictionary[str(id)] = points
	return jsonify({ 'id': id}), 200

@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
	global dictionary
	if id in dictionary:
		return jsonify({ 'points': dictionary[id]}), 200
	return "Invalid ID, 400"


if __name__ == "__main__":
    app.run(debug=True)