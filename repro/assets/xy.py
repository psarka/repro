from datetime import datetime
from datetime import timedelta
import random
import string

from dagster import (
    asset,
    AssetKey,
    DailyPartitionsDefinition,
    AssetIn,
    TimeWindowPartitionMapping,
    Nothing,
)


def process():
    return "hi"


assets = []

for i in range(1000):
    name = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    start_date = (datetime(2023, 8, 22) - timedelta(days=random.randint(0, 365))).date()
    offset = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}"

    assets.append(
        asset(
            key_prefix=["initial_run"],
            name=name,
        )(process)
    )

    assets.append(
        asset(
            key_prefix=["daily_run"],
            name=name,
            partitions_def=DailyPartitionsDefinition(
                start_date=str(start_date),
                timezone="UTC",
                hour_offset=int(offset[:2]),
                minute_offset=int(offset[3:]),
            ),
            deps=[AssetKey(["initial_run", name])],
            ins={
                "_": AssetIn(
                    key=AssetKey(["daily_run", name]),
                    partition_mapping=TimeWindowPartitionMapping(start_offset=-1, end_offset=-1),
                    dagster_type=Nothing,
                ),
            },
        )(process)
    )
