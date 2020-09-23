from flask import Flask, render_template, request
from calculator import add, subtract, division, multiply

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/home')
def home():
    return "Hello, world!"

@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = add(var_1, var_2)
    elif(operation == 'Subtraction'):
        result = subtract(var_1, var_2)
    elif(operation == 'Multiplication'):
        result = multiply(var_1, var_2)
    elif(operation == 'Division'):
        result = division(var_1, var_2)
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)


if __name__ == '__main__':
    app.run(debug=True)
