import warnings

warnings.simplefilter('ignore')
from dagster import MultiPartitionsDefinition
from dagster import StaticPartitionsDefinition
from dagster import asset


@asset(
    name='x',
    partitions_def=MultiPartitionsDefinition({
        'x': StaticPartitionsDefinition(['1']),
        'y': StaticPartitionsDefinition(['A'])
    })
)
def _() -> str:
    return 'hi'
