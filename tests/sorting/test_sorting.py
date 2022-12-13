from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 100, "max_salary": 200, "date_posted": "2022-12-11"},
        {"min_salary": 200, "max_salary": 300, "date_posted": "2022-12-12"},
        {"min_salary": 300, "max_salary": 400, "date_posted": "2022-12-13"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 400
