from flask import Flask
import conjugate.IAdjective as IAdjective
import conjugate.NaAdjective as NaAdjective
import conjugate.IchidanVerb as IchidanVerb

import json

app = Flask(__name__)

@app.route('/')
def none():
    return 'Test', 200


@app.route('/iadj/<adj>')
def iadj_api(adj):

    if IAdjective.is_exception(adj):
        adj = IAdjective.fix_exception(adj)

    return json.dumps(IAdjective.create_dictionary(adj), ensure_ascii=False).encode('utf8'), 200

@app.route('/naadj/<adj>')
def naadj_api(adj):
    return json.dumps(NaAdjective.create_dictionary(adj), ensure_ascii=False).encode('utf8'), 200


@app.route('/ichidan/<ichidan>')
def ichidan_api(ichidan):
    return json.dumps(IchidanVerb.create_dictionary(ichidan), ensure_ascii=False).encode('utf8'), 200


if __name__ == '__main__':
    app.run()
