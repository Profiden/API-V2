from flask import Flask

app = Flask(__name__)
url = "http://localhost:5000/"
endpoints = {
    'users': url + "users",
    'login': url + "login?username='name'pass='password'}",
    'signup': url + 'register?data=userdata',
    'forgot': url + 'forgot?email=email'


}
@app.route('/')
def hello():
    return endpoints
@app.rout('/users')
if __name__ == '__main__':
    # By default, Flask runs on port 5000
    port = 5000
    app.run(debug=True, port=port)
    print(f"API is running on port {port}")
