from flask import Flask, render_template, request
from MyMath import MyMath

app = Flask(__name__)

test = None

@app.route('/')
def index():
    global test
    test = MyMath()
    return render_template('index.html')

# background process happening without any refreshing
@app.route('/background_process/<num>')
def background_process(num):
    global test
    test.num_list.append(float(num))
    return ("nothing")

@app.route('/result')
def data():
    max = test.max()
    avg = test.avg()
    dev = test.std_dev()
    return render_template('result.html', max=max, avg=avg, dev=dev)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)