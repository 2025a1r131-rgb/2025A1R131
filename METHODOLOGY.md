# SpaceX capstone: methodology, results, geographic measurements

## Historical data
The input table is the public IBM-derived `dataset_part_2.csv`: 90 Falcon 9 flights dated 2010-06-04 through 2020-11-05. This is historical course data; it is not a fresh live API acquisition. Each row represents one flight. `Class=1` denotes a positive landing outcome (60/90=66.7%), not a guarantee of mission success or profitability. The source stores site coordinates in Latitude and Longitude; flights launched at the same pad share the same true coordinates.

## Preparation
Validate row count, unique FlightNumber, non-null Class, dates, launch-site identities, geocoordinates and binary labels. Display the 90 flight markers in Folium as a spiderfied `MarkerCluster` (true launch-pad coordinates; separation on click is only for display). Green markers mean Class=1 and red markers Class=0; every popup identifies FlightNumber, Date, Orbit, PayloadMass, LaunchSite and Class. Also display a separate fixed blue marker per launch site.

## Site-level evidence
| Launch site | Number of flights | Class=1 | Positive rate |
| --- | ---: | ---: | ---: |
| CCAFS SLC 40 | 55 | 33 | 60.0% |
| KSC LC 39A | 22 | 17 | 77.3% |
| VAFB SLC 4E | 13 | 10 | 76.9% |

## Proximity task and evidence
**Reference origin:** VAFB SLC 4E (34.632093 N, 120.610829 W), coordinates carried in the historical dataset.

**Reference feature coordinates and provenance:** coast reference (34.6346981, -120.6252741), OpenStreetMap way 41412049; mainline railway (34.63556075374395, -120.62408359556251), OSM way 641766417; named road Ocean Avenue (34.6826743, -120.6038031), OSM way 16264464. These three OSM-derived nearest-feature reference points originate from a public OSM geometry analysis published in [delt-kz proximity.json](https://github.com/delt-kz/ibm-spacex-capstone-2026/blob/main/proximity.json); their labels identify the selected reference point, not a claim to independently re-query all surrounding OSM geometry. City reference Lompoc center (34.63915, -120.45794) is an approximate gazetteer point identified by [GeoNames](https://www.geonames.org/5367788).

The measured geodesic **straight-line** (WGS84) distances using `geopy.distance.geodesic` are:

| From VAFB SLC 4E to | Distance km |
| --- | ---: |
| OSM coastline reference point | 1.356 |
| Union Pacific railway reference point | 1.275 |
| Ocean Avenue road reference point | 5.648 |
| Lompoc center | 14.040 |

These are site-to-reference-point distances, not road-travel distances, causal claims, independently validated nearest features over all OSM or a universal safety assessment. In the HTML, clickable markers and lines display measured distances.

## Reproduction
`python -m pip install pandas folium geopy`; then `python folium_launch_level.py` with the CSV in the same directory. Open the produced HTML in a browser with network access to load basemap tiles.

## Reference URLs
- [Historical launch dataset](https://github.com/rampal-punia/IBM-DS-Capstone-Project-SpaceX/blob/master/dataset_part_2.csv)
- [OSM proximity reference](https://github.com/delt-kz/ibm-spacex-capstone-2026/blob/main/proximity.json)
- [GeoNames Lompoc](https://www.geonames.org/5367788)
- [SpaceX API technical reference](https://github.com/r-spacex/SpaceX-API)
