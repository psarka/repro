from dagster import AutoMaterializePolicy, asset, AssetKey, DailyPartitionsDefinition, AssetIn


@asset(
    key_prefix=["x"],
    name="1",
    auto_materialize_policy=AutoMaterializePolicy.eager(100),
)
def x1() -> str:
    return "hi"


@asset(
    key_prefix=["y"],
    name="1",
    auto_materialize_policy=AutoMaterializePolicy.eager(100),
    partitions_def=DailyPartitionsDefinition("2023-08-01"),
    ins={"x": AssetIn(key=AssetKey(["x", "1"]))},
)
def y1(x) -> str:
    return x


# @asset(
#     key_prefix=["x"],
#     name="2",
#     auto_materialize_policy=AutoMaterializePolicy.eager(100),
# )
# def x2() -> str:
#     return "hi"
#
#
# @asset(
#     key_prefix=["y"],
#     name="2",
#     auto_materialize_policy=AutoMaterializePolicy.eager(100),
#     partitions_def=DailyPartitionsDefinition("2023-07-10"),
#     ins={"x": AssetIn(key=AssetKey(["x", "2"]))},
# )
# def y2(x) -> str:
#     return x
