from flask import Flask, render_template, request,jsonify
from flask_cors import CORS, cross_origin 
from data import call
app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

#app.config['CORS_HEADERS'] = 'Content-Type'e

#@cross_origin(origin='localhost',headers='Content- Type','Authorization'])

@app.route("/")
def landing_page():
  return render_template('index.html')



@app.route("/user-api/",methods=['GET'])
def user_api():
  args = request.args['ticks']

  print(args, 'LOOK HERE')
  return jsonify(call(str(args)))

@app.route('/blk-api/',methods=['GET'])
def blk_api():
  args = request.args['ticks']
  
  print(args, 'LOOK HERE')
  return jsonify(call(str(args)))
