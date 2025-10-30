# זהו הקוד שרץ ב-Render
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def worker_server():
    # השרת הזה קורא את הפרמטרים x, y, z מהכתובת
    x_val = request.args.get('x','a.txt')
    y_val = request.args.get('y','r')
    z_val = request.args.get('z','a')
    with open(x,y) as f:
        kkk="kkk"    
    if y=='w':
        f.write(z)
    
    
    return f"{f}"
