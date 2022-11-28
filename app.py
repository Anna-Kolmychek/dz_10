from flask import Flask
from config import PATH_TO_CANDIDATES_FILE
import utils

candidates = utils.load_candidates(PATH_TO_CANDIDATES_FILE)
app = Flask(__name__)


@app.route('/')
def page_index():
    return utils.get_all(candidates)


@app.route('/candidate/<int:pk>')
def page_candidates(pk):
    return utils.get_by_pk(candidates, pk)


@app.route('/skills/<skill>')
def page_skill(skill):
    return utils.get_by_skill(candidates, skill)


if __name__ == "__main__":
    app.run()
