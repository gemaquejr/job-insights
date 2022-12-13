from src.pre_built.counter import count_ocurrences


# https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
def test_counter():
    assert count_ocurrences('data/jobs.csv', "Marketing".casefold()) == 1259
