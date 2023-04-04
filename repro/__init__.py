from repro import assets

from dagster import Definitions
from dagster import load_assets_from_package_module

defs = Definitions(assets=load_assets_from_package_module(assets))
