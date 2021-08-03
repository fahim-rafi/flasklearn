from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    report = False
    password = request.args.get('password')
    check_upper = any(c.isupper() for c in password)
    check_lower = any(c.islower() for c in password)
    check_num = password[-1].isdigit()
    if check_upper and check_lower and check_num:
        report = True
    
    return render_template('report.html',password=password,report=report, check_upper=check_upper,check_lower=check_lower,check_num=check_num)

if __name__ == '__main__':
    app.run(debug=True)
