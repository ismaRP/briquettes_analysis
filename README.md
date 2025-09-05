# Briquettes analysis

Python notebooks to process mass spectrometry searches from the ceramic briquettes experiments.

RAW MS data and Orthrus and Fragpipe MS search results are available on Zenodo: https://doi.org/10.5281/zenodo.15105348

It uses palaeoPSM as python package: https://github.com/ismaRP/palaeoPSM to process Fragpipe PSM data

Files:
- `milk_briquettes.ipynb` Processes Fragpipe run of milk immersed briquettes samples
- `fish_orthrus_database.ipynb` Creates initial database for Orthrus and then combines and cleans the
    database from Orthrus part 2
- `orthrus_fish_briquettes.ipynb` Processes results from fish briquettes run on Orthrus (casanovo+Sage)
- `fp_fish_briquettes.ipynb` Processes results from fish briquettes run on Fragpipe (using Orthrus part 2 database)

