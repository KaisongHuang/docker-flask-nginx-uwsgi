from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        url = request.form.get('url')
        username = request.form.get('username')
        password = request.form.get('password')
        # TODO
        if 'add' in request.form:
            print('url:{}, username:{}, password:{}, action:add'.format(url, username, password))
        elif 'delete' in request.form:
            print('url:{}, username:{}, password:{}, action:delete'.format(url, username, password))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)