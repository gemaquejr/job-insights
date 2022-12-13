from typing import List, Dict

from src.insights.jobs import read


def get_unique_industries(path):
    industries = read(path)
    all_industries = set()
    for industry in industries:
        if industry["industry"] != "":
            all_industries.add(industry["industry"])
    return all_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
