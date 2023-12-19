from flask import Flask

app = Flask(__name__)  # __name__ is the name of the current file, if it 

@app.route('/') # route is the path of the url
def hello_world():
    return 'Hello Isuru!'

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
  app.run(host='0.0.0.0.0', debug=True)