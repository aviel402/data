# זהו הקוד שרץ ב-Render
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def worker_server():
    # השרת הזה קורא את הפרמטרים x, y, z מהכתובת
    x_val = request.args.get('x')
    y_val = request.args.get('y')
    z_val = request.args.get('z')

    # מבצע לוגיקה כלשהי ומחזיר תשובה
    return f"השרת ברנדר קיבל את הערכים: x={x_val}, y={y_val}, z={z_val}"
