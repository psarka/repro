from dagster import StaticPartitionsDefinition, asset


@asset(
    name='x',
    partitions_def=StaticPartitionsDefinition([str(i) for i in range(1_000)])
)
def _() -> str:
    return 'hi'
