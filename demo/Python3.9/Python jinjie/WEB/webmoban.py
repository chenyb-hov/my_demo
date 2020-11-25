from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username != '' and password != '':
        return render_template('signin-ok.html', username=username, data_list=[i for i in range(1,10)])
    return render_template('form.html', message='the username and password is not None')

if __name__=='__main__':
    app.run()