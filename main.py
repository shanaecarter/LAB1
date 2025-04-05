from flask import Flask, jsonify
import json

app = Flask(__name__) 
# Read data from file and store in global variable data
with open('data.json') as f:
  data = json.load(f)

  # Route for students
  @app.route('/students')
  def get_students():
      pcount = {}
      prefcount = {}
      for student in data:
          programme = student['programme']
          pref = student['pref']

          # Count meal preferences
          if pref in prefcount:
              prefcount[pref] += 1
          else:
              prefcount[pref] = 1

          # Count programmes
          if programme in pcount:
              pcount[programme] += 1
          else:
              pcount[programme] = 1

      # Return both counts as a single response
      return jsonify(pcount, prefcount)

  # Routes for arithmetic operations
  @app.route('/add/<int:a>/<int:b>')
  def add(a, b):
      result = a + b
      return jsonify({"result": result})

  @app.route('/subtract/<int:a>/<int:b>')
  def subtract(a, b):
      result = a - b
      return jsonify({"result": result})

  @app.route('/multiply/<int:a>/<int:b>')
  def multiply(a, b):
      result = a * b
      return jsonify({"result": result})

  @app.route('/divide/<int:a>/<int:b>')
  def divide(a, b):
      if b == 0:
          return jsonify({"error": "Cannot divide by zero"}), 400
      result = a / b
      return jsonify({"result": result})

  # Run the app
  if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
