# flask
# https://flask.palletsprojects.com/en/2.0.x/quickstart/
from flask import Flask, render_template

app = Flask(
    __name__
)

@app.route("/api/people/<id>")
def get_person_by_id(id):
    """
    This API route should return a JSON object that
    represents the person with a given <id>.
    JSON info:
        https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON
    Python & JSON:
        https://docs.python.org/3/library/json.html
    """
    return {}


@app.route("/")
def presentation():
    """
    This route is the final project and will be test
    of all previously learned skills.
    """
    
    return render_template("")