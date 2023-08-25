from dagster import AutoMaterializePolicy, asset, AssetKey, DailyPartitionsDefinition, AssetIn


# def process():
#     return "hi"
#
#
# assets = [
#     asset(
#         key_prefix=["x"],
#         name="1",
#         auto_materialize_policy=AutoMaterializePolicy.eager(100),
#     )(process),
#     asset(
#         key_prefix=["y"],
#         name="1",
#         partitions_def=DailyPartitionsDefinition(start_date="2023-08-01", timezone="UTC"),
#         deps=[AssetKey(["x", "1"])],
#         auto_materialize_policy=AutoMaterializePolicy.eager(100),
#     )(process),
#     asset(
#         key_prefix=["x"],
#         name="2",
#         auto_materialize_policy=AutoMaterializePolicy.eager(100),
#     )(process),
#     asset(
#         key_prefix=["y"],
#         name="2",
#         partitions_def=DailyPartitionsDefinition(start_date="2023-07-21", timezone="UTC"),
#         deps=[AssetKey(["x", "2"])],
#         auto_materialize_policy=AutoMaterializePolicy.eager(100),
#     )(process),
# ]
#
# print("*" * 80)
# print(f"loaded {len(assets)} assets")
# print("*" * 80)


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
    # deps=[AssetKey(["x", "1"])],
    ins={"x": AssetIn(key=AssetKey(["x", "1"]))},
)
def y1(x) -> str:
    return x


@asset(
    key_prefix=["x"],
    name="2",
    auto_materialize_policy=AutoMaterializePolicy.eager(100),
)
def x2() -> str:
    return "hi"


@asset(
    key_prefix=["y"],
    name="2",
    auto_materialize_policy=AutoMaterializePolicy.eager(100),
    partitions_def=DailyPartitionsDefinition("2023-07-10"),
    # deps=[AssetKey(["x", "2"])],
    ins={"x": AssetIn(key=AssetKey(["x", "2"]))},
)
def y2(x) -> str:
    return x
