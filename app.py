from flask import Flask
import utils

# Инициализация приложения
app = Flask(__name__)
candidates = []

# Передача данных для страниц
@app.route('/')
def page_index():
    candidates = utils.get_all()
    return utils.format_candidates(candidates)


@app.route('/candidate/')
def page_candidates():
    return utils.get_all_pk()


@app.route('/candidate/<int:pk>')
def page_candidates_pk(pk):
    candidate = utils.get_by_pk(pk)
    candidate = f'<img src="{candidate["picture"]}">\n' \
                f'{utils.format_candidates([candidate])}'
    return candidate


@app.route('/skills/')
def page_skills():
    return utils.get_all_skills()


@app.route('/skills/<skill>')
def page_skills_skill(skill):
    candidates = utils.get_by_skill(skill)
    return utils.format_candidates(candidates)


# Запуск приложения
if __name__ == "__main__":
    app.run()
