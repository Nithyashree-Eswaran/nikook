from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('guardiana2.html')

@app.route('/after_login')
def hello():
    return render_template('guardiana.html')

@app.route('/chat')
def bot():
    return render_template('chatbot.html')

@app.route('/scan')
def detector():
    return render_template('scanner.html')
@app.route('/guardiana')
def guardiana():
    return render_template('guardiana.html')
@app.route('/gets')
def sign():
    return render_template('signlog.html')
@app.route('/plant')
def type():
    return render_template('plant.html')

if __name__ == '__main__':
    app.run(debug=True)
