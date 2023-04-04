from dagster import StaticPartitionsDefinition, asset, AssetIn, StaticPartitionMapping

partition_mapping = None
# partition_mapping = StaticPartitionMapping({'A': 'A', 'B': 'B', 'C': 'C'})


@asset(
    name='y',
    partitions_def=StaticPartitionsDefinition(['A', 'B', 'C']),
    ins={'x': AssetIn('x', partition_mapping=partition_mapping)}
)
def _(x: str) -> str:
    return x
