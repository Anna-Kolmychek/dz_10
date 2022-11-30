import json
from config import PATH_TO_CANDIDATES_FILE


def load_json(path_to_file: str) -> list[dict]:
    """
    Загружает и конвертирует json данные
    :param path_to_file: путь к файлу
    :return: список с данными
    """
    with open(path_to_file, 'r', encoding='utf-8') as candidates_file:
        candidates = json.load(candidates_file)

    return candidates


def format_candidates(candidates: list[dict]) -> str:
    """
    Формирует строку для вывода
    :param candidates: список кандидатов
    :return: строка html для передачи
    """
    result = '<pre>'
    for candidate in candidates:
        result += f'\n{candidate["name"]}\n' \
                  f'{candidate["position"]}\n' \
                  f'{candidate["skills"]}\n'
    result += '</pre>'

    return result


def get_all() -> list[dict]:
    """
    Получает список всех кандидатов
    :return: список с данными по кандидатам
    """
    return load_json(PATH_TO_CANDIDATES_FILE)


def get_all_pk() -> str:
    """
    Формирует строку со всеми допустимыми значениями pk по всем кандидатам
    :return: строка для отображения /candidate
    """
    candidates = load_json(PATH_TO_CANDIDATES_FILE)
    all_pk = []

    for candidate in candidates:
        all_pk.append(str(candidate['pk']))

    all_pk = f'<pre>\n' \
             f'Доступна информация по кандидатам со следующими значениями pk: ' \
             f'{", ".join(all_pk)}.\n' \
             f'</pre>'

    return all_pk


def get_by_pk(pk: str) -> dict | None:
    """
    Выбирает кандидатов с указанным pk
    :param pk: выбранный pk
    :return: информация по кандидату
    """
    candidates = load_json(PATH_TO_CANDIDATES_FILE)

    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate

    return None


def get_all_skills() -> str:
    """
    Формирует строку со всеми допустимыми значениями навыков
    :return: строка для отображения /skills
    """
    candidates = load_json(PATH_TO_CANDIDATES_FILE)
    all_skills = []

    for candidate in candidates:
        all_skills.extend(candidate['skills'].lower().split(', '))

    all_skills = '\n'.join(set(all_skills))
    all_skills = f'<pre>\n' \
                 f'Доступны кандидаты со следюущими навыками:\n' \
                 f'{all_skills}\n' \
                 f'</pre>'

    return all_skills


def get_by_skill(skill_name: str) -> list[dict]:
    """
    Формирует список кандидатов, у которых есть указанный навык
    :param skill_name: навык для отбора
    :return: список с данными по кандидатам с указанным навыком
    """
    candidates = load_json(PATH_TO_CANDIDATES_FILE)
    candidates_with_skill = []
    skill_name = skill_name.lower().strip()

    for candidate in candidates:
        if skill_name in candidate['skills'].lower().split(', '):
            candidates_with_skill.append(candidate)

    return candidates_with_skill
