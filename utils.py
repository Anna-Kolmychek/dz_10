import json


def load_candidates(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as candidates_file:
        candidates_data = json.load(candidates_file)

    return candidates_data


def get_all(candidates_data):
    all_candidates = '<pre>'

    for candidate in candidates_data:
        all_candidates += f'\n{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n'

    all_candidates += '</pre>'

    return all_candidates


def get_by_pk(candidates_data, pk):
    pk_candidate = 'Нет кандидата с таким pk.'
    for candidate in candidates_data:
        if candidate['pk'] == pk:
            pk_candidate = f'<img src="{candidate["picture"]}">\n\n' \
                           f'<pre>\n' \
                           f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n' \
                           f'</pre>'
            break

    return pk_candidate


def get_by_skill(candidates_data, skill_name):
    skill_candidates = ''
    skill_name = skill_name.lower().strip()

    for candidate in candidates_data:
        if skill_name in candidate['skills'].lower():
            skill_candidates += f'\n{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n'

    if skill_candidates == '':
        skill_candidates = 'Нет кандидатов с такими навыками.'

    skill_candidates = f'<pre>{skill_candidates}</pre>'

    return skill_candidates
