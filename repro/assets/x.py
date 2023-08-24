import time

from dagster import (
    asset,
    MultiPartitionsDefinition,
    StaticPartitionsDefinition,
    DailyPartitionsDefinition,
    AssetExecutionContext,
)


@asset(
    name="x",
    partitions_def=MultiPartitionsDefinition(
        {
            "date": DailyPartitionsDefinition("2023-08-01", "2023-08-10"),
            "level": StaticPartitionsDefinition([f"{i}" for i in range(10)]),
        }
    ),
)
def x(context: AssetExecutionContext) -> str:
    level = context.partition_key.keys_by_dimension["level"]
    # if level in {"1", "2", "3", "4"}:
    #     raise ValueError
    # if level in {"5", "6", "7", "8"}:
    #     return "ok"
    # else:
    while True:
        time.sleep(1)
