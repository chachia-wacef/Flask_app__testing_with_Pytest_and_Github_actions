from flask import Flask,render_template
import socket

app = Flask(__name__)

@app.route("/")
def index():
    print('Flask app default page is called')
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')
    
@app.route("/page2")
def index():
    print('Flask app second page is called')
    try:
        return render_template('page2.html')
    except:
        return render_template('error.html')


if __name__ == "__main__":
    print('Flask app is running')
    app.run(host='0.0.0.0', port=8080)
