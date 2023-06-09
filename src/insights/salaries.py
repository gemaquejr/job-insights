from typing import Union, List, Dict

from src.insights.jobs import read


# Ajuda da Maria Carolina na mentoria
def get_max_salary(path):
    salaries = read(path)
    all_salaries = set()
    for salary in salaries:
        if salary["max_salary"].isnumeric():
            all_salaries.add(int(salary["max_salary"]))
    return max(all_salaries)


def get_min_salary(path):
    salaries = read(path)
    all_salaries = set()
    for salary in salaries:
        if salary["min_salary"].isnumeric():
            all_salaries.add(int(salary["min_salary"]))
    return min(all_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if (int(job["min_salary"]) > int(job["max_salary"])):
            raise ValueError
        return int(job["max_salary"]) >= int(salary) >= int(job["min_salary"])
    except (ValueError, KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    job_salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_salaries.append(job)
        except ValueError:
            pass
    return job_salaries
