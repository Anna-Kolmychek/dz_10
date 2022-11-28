import json

def load_candidates(path_to_file):
    """
    Загружает и конвертирует json данные
    :param path_to_file: путь к файлу
    :return: список с данными
    """
    with open(path_to_file, 'r', encoding='utf-8') as candidates_file:
        candidates_data = json.load(candidates_file)

    return candidates_data


def get_all(candidates_data):
    """
    Формирует строку с выборочными данными (имя, позиция, навыки) по всем кандидатам из списка
    :param candidates_data: список кандидатов
    :return: строка для отображения /
    """
    all_candidates = '<pre>'

    for candidate in candidates_data:
        all_candidates += f'\n{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n'

    all_candidates += '</pre>'

    return all_candidates


def get_all_pk(candidates_data):
    """
    Формирует строку со всеми допустимыми значениями pk по всем кандидатам
    :param candidates_data: список с данными по всем кандидатам
    :return: строка для отображения /candidate
    """
    all_pk = []

    for candidate in candidates_data:
        all_pk.append(str(candidate['pk']))

    all_pk = f'<pre>\n' \
            f'Доступна информация по кандидатам со следующими значениями pk: ' \
            f'{", ".join(all_pk)}.\n' \
            f'</pre>'

    return all_pk


def get_by_pk(candidates_data, pk):
    """
    Формирует строку с выборочными данными каднидата (картинка, имя, поцизия навыки) по указанному pk.
    Если такого нет, выводит соответствующее собщение
    :param candidates_data: список с данными по всем кандидатам
    :param pk: выбранный pk
    :return: строка для отображения /candidate/<pk>
    """
    pk_candidate = 'Нет кандидата с таким pk.'
    for candidate in candidates_data:
        if candidate['pk'] == pk:
            pk_candidate = f'<img src="{candidate["picture"]}">\n\n' \
                           f'<pre>\n' \
                           f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n' \
                           f'</pre>'
            break

    return pk_candidate


def get_all_skills(candidates_data):
    """
    Формирует строку со всеми допустимыми значениями навыков
    :param candidates_data: список с данными по всем кандидатам
    :return: строка для отображения /skills
    """
    all_skills = []

    for candidate in candidates_data:
        all_skills.extend(candidate['skills'].split(', '))

    all_skills = set([skill.lower() for skill in all_skills])

    all_skills = '\n'.join(all_skills)
    all_skills = f'<pre>\n' \
            f'Доступны кандидаты со следюущими навыками:\n' \
            f'{all_skills}.\n' \
            f'</pre>'

    print(all_skills)
    return all_skills

def get_by_skill(candidates_data, skill_name):
    """
    Формирует строку с выборочными данными (имя, позиция, навыки) кандидатов, обладающих указанным навыком
    :param candidates_data: список данных по всем кандидатам
    :param skill_name: навык для отбора
    :return: строка для отображения /skills/<skill_name>
    """
    skill_candidates = ''
    skill_name = skill_name.lower().strip()

    for candidate in candidates_data:
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [skill.lower() for skill in candidate_skills]
        if skill_name in candidate_skills:
            skill_candidates += f'\n{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n'

    if skill_candidates == '':
        skill_candidates = 'Нет кандидатов с такими навыками.'

    skill_candidates = f'<pre>{skill_candidates}</pre>'

    return skill_candidates
