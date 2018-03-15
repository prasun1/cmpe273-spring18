''' In this tutorial I have worked on HTTP methods using Python Flask. I have sent and received JSON objects using HTTP methods. 
Please follow the steps carefully to setup Python Flask and run each command'''


How to Setup

virtualenv my-venv
. my-venv/bin/activate //To activate virtual environment

pip3 install -r requirements.txt // To install Flask directly from requirement file

How to run?

FLASK_APP=hello.py flask run // For Starting the server

GET 

curl -i http://127.0.0.1:5000/lang // for get request. These are readonly requests

POST users

curl -i -X POST http://127.0.0.1:5000/user -d "name=Java"

Response


  
  HTTP/1.0 200 OK
  
  Content-Type: application/json
  
  Content-Length: 180
  
  Server: Werkzeug/0.14.1 Python/3.6.4
  
  Date: Mon, 26 Feb 2018 05:49:16 GMT
  


  {
  
    "languages": [
      {
        "id": 1, 
        "name": "java"    
      }, 
      {
        "id": 2, 
        "name": "prasun" 
      },    
      {
        "id": 3, 
        "name": "saxena"
      }
    ]
    
  }


DELETE users


curl -i -X DELETE http://127.0.0.1:5000/langs/1

HTTP/1.0 200 OK

Content-Type: application/json

Content-Length: 129

Server: Werkzeug/0.14.1 Python/3.6.4

Date: Mon, 26 Feb 2018 05:50:30 GMT




{
  
    "languages": [ 
      {
        "id": 2, 
        "name": "prasun" 
      },    
      {
        "id": 3, 
        "name": "saxena"
      }
    ]
    
  }
  
  
 GET 
curl -i http://127.0.0.1:5000/show/1 // for get request. These are readonly requests(For this to work you have to post data  first)
