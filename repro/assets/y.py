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
    partitions_def=DailyPartitionsDefinition(start_date="2023-08-01"),
    auto_materialize_policy=AutoMaterializePolicy.eager(1),
)
def no_deps_eager_1() -> None:
    print('hi')


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-08-01"),
    auto_materialize_policy=AutoMaterializePolicy.eager(100),
)
def no_deps_eager_100() -> None:
    print('hi')


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-08-01"),
    auto_materialize_policy=AutoMaterializePolicy.eager(1),
    ins={
        "self_dep_eager_1": AssetIn(
            key=AssetKey("self_dep_eager_1"),
            partition_mapping=TimeWindowPartitionMapping(start_offset=-1, end_offset=-1),
            dagster_type=Nothing,
        ),
    },
)
def self_dep_eager_1() -> None:
    print('hi')


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-08-01"),
    auto_materialize_policy=AutoMaterializePolicy.eager(100),
    ins={
        "self_dep_eager_100": AssetIn(
            key=AssetKey("self_dep_eager_100"),
            partition_mapping=TimeWindowPartitionMapping(start_offset=-1, end_offset=-1),
            dagster_type=Nothing,
        ),
    },
)
def self_dep_eager_100() -> None:
    print('hi')


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-08-01"),
    auto_materialize_policy=AutoMaterializePolicy.eager(1),
    ins={
        "x": AssetIn(
            key=AssetKey("x"),
        ),
    },
)
def upstream_dep_eager_1(x: str) -> None:
    print(x)


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-08-01"),
    auto_materialize_policy=AutoMaterializePolicy.eager(100),
    ins={
        "x": AssetIn(
            key=AssetKey("x"),
        ),
    },
)
def upstream_dep_eager_100(x: str) -> None:
    print(x)


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-08-01"),
    auto_materialize_policy=AutoMaterializePolicy.eager(1),
    ins={
        "x": AssetIn(
            key=AssetKey("x"),
        ),
        "self_dep_upstream_dep_eager_1": AssetIn(
            key=AssetKey("self_dep_upstream_dep_eager_1"),
            partition_mapping=TimeWindowPartitionMapping(start_offset=-1, end_offset=-1),
            dagster_type=Nothing,
        ),
    },
)
def self_dep_upstream_dep_eager_1(x: str) -> None:
    print(x)


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-08-01"),
    auto_materialize_policy=AutoMaterializePolicy.eager(100),
    ins={
        "x": AssetIn(
            key=AssetKey("x"),
        ),
        "self_dep_upstream_dep_eager_100": AssetIn(
            key=AssetKey("self_dep_upstream_dep_eager_100"),
            partition_mapping=TimeWindowPartitionMapping(start_offset=-1, end_offset=-1),
            dagster_type=Nothing,
        ),
    },
)
def self_dep_upstream_dep_eager_100(x: str) -> None:
    print(x)
