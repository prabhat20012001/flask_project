from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['POST'])
def form():
    name = request.form.get('name')
    weight = float(request.form.get('weight'))
    height = float(request.form.get('height'))
    age = int(request.form.get('age'))
    # bmi= float((weight)/(height)(height))
    
    # Add your logic here to calculate BMI or any other necessary calculations
    # Then return a response to the user with the appropriate information

    return f"Name: {name}, Weight: {weight}, Height: {height}, Age: {age}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)