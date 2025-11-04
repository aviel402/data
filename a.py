# זהו הקוד שרץ ב-Render
from flask import Flask, request
import requests as r

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def worker_server():
    g = r.get('https://data-hdb0.onrender.com')
    all = request.args if request.method == 'GET' else request.post
    x = all.get('x')
    y = all.get('y')
    z = all.get('z',1)
    if x and y and z:
        with open(x,y) as f:
            kkk="kkk"    
        if y=='w':
            f.write(z)
            f=''
        else:
            f=f.read()
        
        return f"{f}"
@app.route('/FFFFF', methods=['GET','POST'])
def a():
    all = request.args if request.method == 'GET' else request.post
    pas = all.get('pas')
    if pas != 55555666665555588888:
        return 'sss'
