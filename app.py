from flask import Flask

app = Flask (__name__)

@app.route('/')
def home ():
    return "Welcome to Flask Home"

@app.route ('/page1')
def page1():
    return "Welcome to Flask Page1"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)