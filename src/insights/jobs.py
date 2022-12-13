from functools import lru_cache
from typing import List, Dict

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


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
