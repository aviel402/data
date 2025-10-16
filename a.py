from flask import Flask

app = Flask(__name__)

# נקודת הקצה הראשית. תפקידה להשאיר את השרת ער ולאשר שהוא פועל.
@app.route('/',methods=[GET,POST])
def main_route():
    if not x:
        return 'read="אנא הקש מספר" x,,,'
