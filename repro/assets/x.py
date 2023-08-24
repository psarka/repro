from dagster import AutoMaterializePolicy, asset


@asset(
    name='x',
    auto_materialize_policy=AutoMaterializePolicy.eager(1000),
)
def x() -> str:
    return 'hi'
