def test_can_import_queries():
    from src.jobs.job_1 import query_1

    assert query_1 is not None

    from src.jobs.job_2 import query_2

    assert query_2 is not None
