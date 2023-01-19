import random
import flask
from flask import request
import json

app = flask.Flask(__name__)

rows = json.load(open("dadjokes.json", 'r', encoding='utf-8'))

@app.route('/', methods=['GET'])
def home():
    ret={'success': True, 'message':'This is the home page'}
    return json.dumps(ret), 200, {"Content Type":'application/json'}

@app.route('/random', methods=['GET'])
def randomjoke():
    random_number = random.randint(0, len(rows)-1)
    ret=rows[random_number]
    return json.dumps(ret), 200, {"Content Type":'application/json'}

@app.route('/joke', methods=['GET'])
def specificjoke():
    if 'id' in request.args:
        for x in rows:
            value_list=[]
            for value in x.values():
                value_list.append(value)
            if request.args['id']==value_list[0]:
                return json.dumps(x), 200, {"Content Type":'application/json'}
        return(err_404(404))
    else:
        return(err_404(404))

@app.errorhandler(404)
def err_404(e):
    return "Couldn't find page", 404


app.run(host='127.0.0.1', port=3001)
