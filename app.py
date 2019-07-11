from flask import Flask, redirect, render_template, request
import os

app = Flask(__name__)

def recursive_fib(n):
    n = int(n)
    if (n <= 1):  
       return 1  
    else:  
       return (recursive_fib(n-1) + recursive_fib(n-2))  

@app.route('/fib/<int:n>')
def index(n):
    return str(recursive_fib(n))

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)