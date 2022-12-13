from functools import lru_cache

import csv


@lru_cache
def read(path):
    with open(path, encoding='utf-8') as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_results = list(jobs_reader)
        return jobs_results


def get_unique_job_types(path):
    jobs = read(path)
    all_jobs = set()
    for job in jobs:
        all_jobs.add(job["job_type"])
    return all_jobs


def filter_by_job_type(jobs, job_type):
    list_of_job_types = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_of_job_types.append(job)
    return list_of_job_types
