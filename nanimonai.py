from flask import Flask
import conjugate.IAdjective as IAdjective
import conjugate.NaAdjective as NaAdjective
import conjugate.IchidanVerb as IchidanVerb
import conjugate.GodanVerb as GodanVerb
import edict.edict_reader as edict
import utils.charset_utility as charset
import service.service_paths as paths
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
        return paths.get_i_adjective_json(conjugateable), 200

    if conjugateable[-1:] == 'な':
        print(conjugateable + ' is an な adjective')
        return paths.get_na_adjective_json(conjugateable), 200

    json_verb_table = paths.get_verb_json(conjugateable)
    if json_verb_table is None:
        return '', 404
    else:
        return json_verb_table


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
