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
    partitions_def=DailyPartitionsDefinition(start_date="2023-09-20"),
    auto_materialize_policy=AutoMaterializePolicy.eager(3),
)
def no_deps_eager_3() -> None:
    print('hi')


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-09-20"),
    auto_materialize_policy=AutoMaterializePolicy.eager(3),
    ins={
        "self_dep_eager_3": AssetIn(
            key=AssetKey("self_dep_eager_3"),
            partition_mapping=TimeWindowPartitionMapping(start_offset=-1, end_offset=-1),
            dagster_type=Nothing,
        ),
    },
)
def self_dep_eager_3() -> None:
    print('hi')


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-09-20"),
    auto_materialize_policy=AutoMaterializePolicy.eager(3),
    ins={
        "x": AssetIn(
            key=AssetKey("x"),
        ),
    },
)
def upstream_dep_eager_3(x: str) -> None:
    print(x)


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-09-20"),
    auto_materialize_policy=AutoMaterializePolicy.eager(3),
    ins={
        "x": AssetIn(
            key=AssetKey("x"),
        ),
        "self_dep_upstream_dep_eager_3": AssetIn(
            key=AssetKey("self_dep_upstream_dep_eager_3"),
            partition_mapping=TimeWindowPartitionMapping(start_offset=-1, end_offset=-1),
            dagster_type=Nothing,
        ),
    },
)
def self_dep_upstream_dep_eager_3(x: str) -> None:
    print(x)

