from flask import Flask, request, render_template

app = Flask(__name__)  # creating the Flask class object


# --------------------------------------------------------

@app.route('/')  # decorator defines the
def home():
    return "<h1>hello, this is our first flask website</h1>"


# ---------------------------------------------------------------

@app.route('/msg')  # decorator defines the
def welcome():
    return render_template('welcome.html')  # jinja2


# --------------------------------------------------------

@app.route('/welcome/<name>')  # decorator defines the
def wel(name):
    return render_template('hello.html', name=name)  # jinja2-passing parameter to template


# ----------------------------------------
@app.route('/name')
def print_name():
    return '<h1> Abhinav </h1>'


# -------------------------------------------------------
@app.route('/user-data', methods=['POST', 'GET'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        result = '''
                <h4>First name:{}</h4>
                <h4>last name:{}</h4>
        
        '''
        return result.format(first_name, last_name)


# -----------------------------------------------------------
@app.route('/user')
def user_form():
    return render_template("form.html")


# ---------------------------------------------------
if __name__ == '__main__':
    app.run()
