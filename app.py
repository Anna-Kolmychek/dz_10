from flask import Flask
from config import PATH_TO_CANDIDATES_FILE
import utils

# Загрузка данных, инициализация приложения
candidates = utils.load_candidates(PATH_TO_CANDIDATES_FILE)
app = Flask(__name__)


# Передача данных для страниц
@app.route('/')
def page_index():
    return utils.get_all(candidates)


@app.route('/candidate/')
def page_candidates():
    return utils.get_all_pk(candidates)


@app.route('/candidate/<int:pk>')
def page_candidates_pk(pk):
    return utils.get_by_pk(candidates, pk)


@app.route('/skills/')
def page_skills():
    return utils.get_all_skills(candidates)


@app.route('/skills/<skill>')
def page_skills_skill(skill):
    return utils.get_by_skill(candidates, skill)


# Запуск приложения
if __name__ == "__main__":
    app.run()
