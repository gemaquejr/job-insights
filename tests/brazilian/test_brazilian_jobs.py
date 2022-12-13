from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    translated = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert "title" in translated[0]
