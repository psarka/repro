# Automaterialization run crash repro

Install:

    pip install dagster==1.4.9 dagster-webserver==1.4.9

run:

    dagster dev

1. Enable automaterialization in the UI.
2. When first run (for asset x_1) is complete, uncomment the second pair of assets and save the file.
3. Observe failed run for asset y_1.