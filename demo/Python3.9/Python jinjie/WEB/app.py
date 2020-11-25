from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
            <p><input name="username"/></p>
            <p><input name="password" type="password"/></p>
            <p><button type="submit">login</button><p>
    </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] != '' and request.form['password'] != '':
        return "<h3>Hello, "+request.form["username"]+"</h3>"
    return '<h3>username and password is None</h3>'

if __name__=="__main__":
    app.run()
