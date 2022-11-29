# Google Complex (Airport)

In this activity, you will create a DataFrame that contains the rating for every international airport in the top 6 metropolitan areas, as rated by Google users.

## Instructions

* Using [05-Stu_Google_Complex/Airport_Ratings.ipynb](Unsolved/Airport_Ratings.ipynb) as a starting point, utilize the Google Geocoding API, the Google Places API, and Python/Jupyter to create a script that lists the "Airport Rating" of the major "International Airport" in each of the top 6 metropolitan areas found in [05-Stu_Google_Complex/Cities.csv](Resources/Cities.csv).

* Your final `ipynb` file should contain each of the following headers:

  * `City`

  * `State`

  * `Lat`

  * `Lng`

  * `Airport Name`

  * `Airport Address`

  * `Airport Rating`

## Hint

* You will need to obtain the `Lat` and `Lng` of each airport before sending it through the Google Places API to obtain the rating.

* When using the Google Places API, make sure to use the term "International Airport" to ensure that the data received is for a major airport in the city and not a regional airport.

* Use a try-except to skip airports that do not have Google user ratings.

## References

Data Source: Google Maps Platform. (2020). Place Types. Places API. [https://developers.google.com/places/supported_types](https://developers.google.com/places/supported_types)

---

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
