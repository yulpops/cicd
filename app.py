from flask import Flask
from flask import request, jsonify,render_template

app = Flask(__name__)
app.debug = True




@app.route('/', methods=['GET'])
def hello():
    return render_template('hello.html')





app.run(port=5000)

if __name__ == '__main__':
    main()
