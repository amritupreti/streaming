import os
from flask import Flask, request


app = Flask(__name__)

try:
    hostname = ''
    with open('/etc/hostname', 'r') as f:
        hostname = f.read().strip()
except:
    pass

@app.route('/')
def index():
    return f'Server {hostname} is running!'

@app.route('/auth', methods=['POST'])
def auth(*args, **kwargs):
    key = request.form.get('key', '')

    if key == 'supersecret':
        return {}, 200
    else:
        return {}, 401
    
@app.route('/normal')
def normal():
    return f'Normal {hostname} is running!'

@app.route('/expensive')
def expensive():
    return f'Expensive {hostname} is running!'

@app.route('/sticky')
def sticky():
    return f'Sticky {hostname} is running!'

@app.route('/admin')
def admin():
    return f'Admin {hostname} is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
