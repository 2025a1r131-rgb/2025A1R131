# SpaceX Falcon 9 historical landing-outcome capstone

This branch contains an **independent historical analysis** using the public IBM course-derived Falcon 9 records. It is not presented as a learner's previously completed Coursera lab work.

## Scope
- 90 Falcon 9 launch records dated 2010-06-04 to 2020-11-05.
- Landing outcome proxy: 60 records with `Class=1`, 30 with `Class=0`.
- Launch sites: CCAFS SLC 40 (55 records), KSC LC 39A (22), VAFB SLC 4E (13).
- Geospatial analysis: 90 individual color-coded Folium markers grouped by a MarkerCluster, site-level popups, and measured distances from VAFB SLC 4E to published geographic reference coordinates.

## Methodology and reproducibility
See [METHODOLOGY.md](METHODOLOGY.md) for data provenance, population definitions, procedures, distance calculations, and limitations.
See [folium_launch_level.py](folium_launch_level.py) for executable Folium logic.
Historical data source: [dataset_part_2.csv](dataset_part_2.csv), originally published by [rampal-punia](https://github.com/rampal-punia/IBM-DS-Capstone-Project-SpaceX/blob/master/dataset_part_2.csv).

### Reproduce
```bash
pip install pandas folium geopy
python folium_launch_level.py
```
The script writes `SpaceX_90_Launches_Folium.html`. Open the HTML in a browser with an internet connection for OpenStreetMap basemap tiles.

## Geographic reference data
VAFB SLC-4E coordinates: (34.632093, -120.610829). Published OpenStreetMap feature reference points were obtained from a [public OSM-proximity extract](https://github.com/delt-kz/ibm-spacex-capstone-2026/blob/main/proximity.json); the distance calculation is performed by the project script, with the coordinate source and OSM way ID shown for each feature. Lompoc coordinates are from [GeoNames](https://www.geonames.org/5367788).

All reported distances are **geodesic straight-line site-to-reference-point distances**, not distances by road; proximity patterns do not establish causal effects on launch outcomes.
