from flask import Flask, request, render_template, jsonify
from math import log10

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/result",methods=['POST'])
def math_ops():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = request.form['num1']
        num2 = request.form['num2']
    
    if ops == 'add':
        r = float(num1) + float(num2)
        result = f"Sum of {num1} and {num2} is : {str(round(r,4))}"
    

    if ops == 'subtract':
        r = float(num1) - float(num2)
        result = f"Difference of {num1} and {num2} is : {str(round(r,4))}"
    

    if ops == 'multiply':
        r = float(num1) * float(num2)
        result = f"Product of {num1} and {num2} is : {str(round(r,4))}"
    

    if ops == 'divide':
        r = float(num1) / float(num2)
        result = f"Division of {num1} and {num2} is : {str(round(r,4))}"
    
    if ops == 'log':
        r = log10(float(num1)) 
        result = f"Log10 of {num1} is : {str(round(r,4))}"

    return render_template('results.html',result=result)

@app.route("/postman_test",methods=['POST'])
def math_ops1():
    if request.method == 'POST':
        ops = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
    
    if ops == 'add':
        r = float(num1) + float(num2)
        result = f"Sum of {num1} and {num2} is : {str(round(r,4))}"
    

    if ops == 'subtract':
        r = float(num1) - float(num2)
        result = f"Difference of {num1} and {num2} is : {str(round(r,4))}"
    

    if ops == 'multiply':
        r = float(num1) * float(num2)
        result = f"Product of {num1} and {num2} is : {str(round(r,4))}"
    

    if ops == 'divide':
        r = float(num1) / float(num2)
        result = f"Division of {num1} and {num2} is : {str(round(r,4))}"
    
    if ops == 'log':
        r = log10(float(num1)) 
        result = f"Log10 of {num1} is : {str(round(r,4))}"

    return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0")
