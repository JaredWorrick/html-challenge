# Hot Airport Reviews

In this activity, you will create a heatmap based on airport ratings.

## Instructions

* If you haven't already, navigate to your [Google Developers Console](https://console.developers.google.com/), and enable the __Maps JavaScript API__.

* Install `gmaps`.

* If it's not already running, start your virtual environment.

  * On Windows, `activate PythonData`.

  * On Mac, `source activate PythonData`.

* Then, from the command line, run `conda install -c conda-forge gmaps`.

* Using the starter notebook and the airport CSV in the Resources folder, create a ratings heatmap of the airports across the country.

  * Use the latitude and longitude to place the airport

  * Use the rating to weight the heatmap.

  * Be sure to handle `NaN` values and data type in your airport ratings.

  * Refer to the [Gmaps documentation](http://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html#heatmaps) for instructions on implementing heatmaps.

  * The following image captures the airport ratings heatmap:

  ![Airport Heatmap](Images/08-Airport_Heatmap.png)

## Bonus

* Explore the [documentation](http://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html#base-maps) to plot the map using two other map types, as captured in the following images:

  ![Hybrid Map](Images/08-Hybrid_Map.png)

  ![Terrain Map](Images/08-Terrain_Map.png)

## References

Google Maps Platform. (2020). Place Types. Places API. [https://developers.google.com/places/supported_types](https://developers.google.com/places/supported_types)

---

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.