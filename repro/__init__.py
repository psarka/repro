from dagster import Definitions

from repro.assets import xy

defs = Definitions(assets=xy.assets)
