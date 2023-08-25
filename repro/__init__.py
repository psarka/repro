from dagster import Definitions
from dagster import load_assets_from_package_module

from repro import assets

defs = Definitions(assets=load_assets_from_package_module(assets))
