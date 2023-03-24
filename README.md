# Experimental Warning Repro

## Linux

Install:

    pip install dagster==1.1.21 dagit

run:

    dagster dev

## Windows

    mamba install "dagster==1.1.21" dagit

run:

    PYTHONLEGACYWINDOWSSTDIO=utf8 dagster dev

## Repro

Click "refresh assets" button in the UI.