from flask import Flask
import conjugate.IAdjective as IAdjective
import conjugate.NaAdjective as NaAdjective

import json

app = Flask(__name__)


@app.route('/iadj/<adj>')
def iadj_api(adj):
    return json.dumps(IAdjective.create_dictionary(adj), ensure_ascii=False).encode('utf8')

@app.route('/naadj/<adj>')
def naadj_api(adj):
    return json.dumps(NaAdjective.create_dictionary(adj), ensure_ascii=False).encode('utf8')


if __name__ == '__main__':
    app.run()
