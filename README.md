# Briquettes analysis

Python notebooks to process mass spectrometry searches from the briquettes experiments.
It uses palaeoPSM as python package: https://github.com/ismaRP/palaeoPSM to process Fragpipe PSM data

- `milk_briquettes.ipynb` Process Fragpipe run of milk immersed briquettes samples
- `fish_orthrus_database.ipynb` Creates the initial database for Orthrus and then combines and cleans the
    database from Orthrus part 2
- `orthrus_fish_briquettes.ipynb` Process results from fish briquettes run on Orthrus (casanovo+Sage)
- `fp_fish_briquettes.ipynb` Process results from fish briquettes run on Fragpipe (using Orthrus part 2 database)