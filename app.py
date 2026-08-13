from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# กำหนด Username และ Password สำหรับล็อกอิน
USERNAME_DB = "ploy"
PASSWORD_DB = "ploy"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USERNAME_DB and password == PASSWORD_DB:
            return redirect(url_for('dashboard'))
        else:
            error = "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง!"
            
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)