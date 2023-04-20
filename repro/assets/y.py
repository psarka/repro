from dagster import StaticPartitionsDefinition, asset, AssetIn


@asset(
    name='y',
    partitions_def=StaticPartitionsDefinition(['A', 'B', 'C']),
    ins={'x': AssetIn('x')}
)
def _(x: str) -> str:
    return x
