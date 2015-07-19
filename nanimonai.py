from flask import Flask
import conjugate.IAdjective as IAdjective
import conjugate.NaAdjective as NaAdjective
import conjugate.IchidanVerb as IchidanVerb
import conjugate.GodanVerb as GodanVerb
import edict.edict_reader as edict
import os

import json

app = Flask(__name__)

@app.route('/')
def none():
    return 'Test', 200


@app.route('/default/<conjugateable>')
def conjugate(conjugateable):

    if conjugateable[-1:] == 'い':
        print(conjugateable + ' is an い adjective')
        return json.dumps(IAdjective.create_dictionary(conjugateable), ensure_ascii=False).encode('utf8'), 200

    if conjugateable[-1:] == 'な':
        print(conjugateable + ' is an な adjective')
        return json.dumps(IAdjective.create_dictionary(conjugateable), ensure_ascii=False).encode('utf8'), 200

    entry = edict.dict[conjugateable]
    if entry is None:
        return '', 404
    parts_of_speech = entry.get_part_of_speech()
    for pos in parts_of_speech:
        if 'Ichidan verb' == pos:
            print(conjugateable + ' is an　一段 verb')
            return json.dumps(IchidanVerb.create_dictionary(conjugateable), ensure_ascii=False).encode('utf8'), 200
        if 'verb' in pos:  # If we get past ichidan and it's still a verb then it's godan
            print(conjugateable + ' is an　五段 verb')
            return json.dumps(GodanVerb.create_dictionary(conjugateable), ensure_ascii=False).encode('utf8'), 200
    return '', 404


@app.route('/iadj/<adj>')
def iadj_api(adj):
    return json.dumps(IAdjective.create_dictionary(adj), ensure_ascii=False).encode('utf8'), 200

@app.route('/naadj/<adj>')
def naadj_api(adj):
    return json.dumps(NaAdjective.create_dictionary(adj), ensure_ascii=False).encode('utf8'), 200


@app.route('/ichidan/<ichidan>')
def ichidan_api(ichidan):
    return json.dumps(IchidanVerb.create_dictionary(ichidan), ensure_ascii=False).encode('utf8'), 200

@app.route('/godan/<godan>')
def godan_api(godan):
    return json.dumps(GodanVerb.create_dictionary(godan), ensure_ascii=False).encode('utf8'), 200


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))  # Change working directory to current directory
    edict.load()  # Loading the edict into memory takes a while but is only done once
    app.run()