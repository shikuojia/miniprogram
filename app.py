from flask import Flask,escape,url_for
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index page'

@app.route('/login')
def login():
    return 'login flask page'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username = 'lei'))

# if __name__ == '__main__':
#     app.run(port=5005)

