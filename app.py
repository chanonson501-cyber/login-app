from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # เปลี่ยนให้เรียกใช้งานไฟล์หลักของคุณ (เช่น main.html)
    return render_template('main.html')

@app.route('/reference')
def reference():
    return render_template('reference.html')

if __name__ == '__main__':
    app.run(debug=True)