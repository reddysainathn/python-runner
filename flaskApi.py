import checkApi
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/all', methods=['GET'])
def all():
    return checkApi.getAllValues()
