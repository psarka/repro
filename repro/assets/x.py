from dagster import StaticPartitionsDefinition, asset


@asset(
    name='x',
    partitions_def=StaticPartitionsDefinition(['1', '2', '3'])
)
def _() -> str:
    return 'hi'
