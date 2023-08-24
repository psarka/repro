from dagster import (
    DailyPartitionsDefinition,
    AssetIn,
    AssetKey,
    TimeWindowPartitionMapping,
    Nothing,
    AutoMaterializePolicy,
    asset,
)


@asset(
    name="y",
    partitions_def=DailyPartitionsDefinition(start_date="2023-08-01"),
    # deps=[AssetKey(['x'])],  # it also does not work when dep(ending) on x
    auto_materialize_policy=AutoMaterializePolicy.eager(1000),
    ins={
        "x": AssetIn(
            key=AssetKey("x"),
        ),
        "y": AssetIn(
            key=AssetKey("y"),
            partition_mapping=TimeWindowPartitionMapping(start_offset=-1, end_offset=-1),
            dagster_type=Nothing,
        ),
    },
)
def y(x: str) -> None:
    print(x)
