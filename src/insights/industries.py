from src.insights.jobs import read


def get_unique_industries(path):
    industries = read(path)
    all_industries = set()
    for industry in industries:
        if industry["industry"] != "":
            all_industries.add(industry["industry"])
    return all_industries


def filter_by_industry(jobs, industry):
    list_of_job_types = []
    for job in jobs:
        if job["industry"] == industry:
            list_of_job_types.append(job)
    return list_of_job_types
