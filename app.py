from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Временно заглушка - потом заменим на реальные данные
    students = []
    return render_template('index.html', students=students)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add')
def add_form():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)