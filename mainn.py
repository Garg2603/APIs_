#First API using Flask

from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while n > 0:
        digit = n % 10
        sum += digit ** order
        n = n // 10
    if sum == copy_n:
        print(f"{copy_n} is an Armstrong number")
        result={
            "Number":n,
            "Armstrong":True,
            "Server IP":"122.14.14.12.1000"
        }
    else:
        print(f"{copy_n} is not an Armstrong number")
        result={
            "Number":n,
            "Armstrong":False,
            "Server IP":"122.14.14.12.1000"
        }
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)
