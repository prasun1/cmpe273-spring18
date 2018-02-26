from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

languages = []
id = 0
@app.route('/')
def hello():
   return "Hello World"


@app.route('/users',methods=['POST'])
def new_users():
   name = request.form['name']
   return "hello{}!".format(name)  


@app.route('/getmore',methods=['GET'])
def test():
    return jsonify({'message': 'It works'})

@app.route('/lang',methods=['GET'])
def returnAll():
     return jsonify({'languages':languages})
     

@app.route('/user',methods=['POST'])
def addOne():
     global id
     id = id+1
     language = {
                'id':id,
                'name':request.form['name']
                }
     languages.append(language)
     return jsonify({'languages' : languages})
     
@app.route('/langs/<id>',methods=['DELETE'])
def remove(id):
    print(languages[id])
    for i in range(len(languages)):
        if int(languages[i]['id']) == int(id):
                languages.pop(i)
    return jsonify({'languages':languages})