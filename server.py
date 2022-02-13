from flask import Flask, request, jsonify
from datetime import datetime as dt

app = Flask(__name__)

num_people = 0 
names = []
logs = []

@app.route('/simple_api/getNumPeople',methods = ['GET'])
def getNumPeople():
   return jsonify({"Total people online: ":num_people});

@app.route('/simple_api/getLog',methods = ['GET'])
def getHistory():
   return jsonify(logs);

@app.route('/simple_api/getUserList', methods = ['GET'])
def getUsesrList():
   if logs == []:
      return jsonify("No one is online")
   else:
      return jsonify(names)
   return jsonify(names);

@app.route('/simple_api/login',methods = ['POST'])
def login():
   global num_people
   num_people += 1
   log = request.get_json()
   log["type"] = "login"
   log["time"] = dt.now()
   names.append(log["username"])
   logs.append(log)
   return jsonify("Login Successed!");

@app.route('/simple_api/logout',methods = ['POST'])
def delete():
   global num_people
   num_people -= 1
   log = request.get_json()
   log["type"] = "logout"
   log["time"] = dt.now()
   names.remove(log["username"])
   logs.append(log)
   return jsonify("Logout Successed!");

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8088, debug = True)