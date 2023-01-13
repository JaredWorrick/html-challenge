# Import, Update, and Explore

In this activity, you will practice importing data from your Terminal, updating data types, and exploring data in the Mongo Shell.

## Instructions

* Write a command that imports the data from [annual_aqi_by_county_2022.csv](Resources/annual_aqi_by_county_2022.csv) to a database called `epa` and a collection called `annual_aqi_by_county`. If the collection already exists, drop the collection.

* Write a command that imports the data from [ohio_daily_records_2022.json](Resources/ohio_daily_records_2022.json) to a database called `epa` and a collection called `ohio_daily_records`. If the collection already exists, drop the collection.

* Write a command that imports the data from [ohio_jan_2022.json](Resources/ohio_jan_2022.json) to a database called `epa` and a collection called `ohio_air`. If the collection already exists, drop the collection.

* Write a command that imports the data from [ohio_feb_2022.json](Resources/ohio_feb_2022.json) to a database called `epa` and a collection called `ohio_air`. **Note:** This is the same collection used in the previous import so be sure not to drop the collection in advance.

* Run `mongo` or `mongosh` from your Terminal and verify that your files imported correctly by writing commands to do the following:

  * Use the `epa` database.

  * Show all the collections in the `epa` database.

  * Verify that there is data in each of the 3 collections (`ohio_daily_records`, `annual_aqi_by_county`, and `ohio_air`) by using `findOne()` to display an entry.

  * Verify that there is data from January 2022 in the `ohio_air` collection by searching on the `date_local` field.

  * Verify that there is data from February 2022 in the `ohio_air` collection by searching on the `date_local` field.

* Update the `DAILY_AQI_VALUE` nested under `CO` in the `ohio_daily_records` collection to change the string values to integers.

* Update the `PERCENT_COMPLETE` nested under `CO` in the `ohio_daily_records` collection to change the string values to doubles.

* Find a record in the `ohio_daily_records` collection where `CO.UNITS` matches "ppm" and `NO2.UNITS` matches "ppb". This will help us find sites that recorded values for carbon monoxide and nitrogen dioxide.

## Hints

* Dates for the `ohio_air` collection use the YYYY-MM-DD format.

* Nested records use dot notation.

* Remember to use square brackets as part of your query when changing the data type of a field. Your `updateMany()` query should use the following convention: `updateMany({}, [ {'$set': "field_name": {'$toDataType': "$field_name"}} ])`.

## References

`ohio_daily_records_2022.json`: United States Environmental Protection Agency. 2022. *Download daily data*. Settings: Year "2022", Geographic Area "Ohio", and Pollutants "CO", "NO2", and "SO2". Available: https://www.epa.gov/outdoor-air-quality-data/download-daily-data [2022, October 14].

`annual_aqi_by_county_2022.csv`: United States Environmental Protection Agency. 2022. *Pre-generated data files*. Annual AQI by county 2022. Available: https://aqs.epa.gov/aqsweb/airdata/download_files.html [2022, October 6]. 

`ohio_jan_2022.json` and `ohio_feb_2022.json`: United States Environmental Protection Agency. 2022. *Air Quality System (AQS) API*. Available: https://aqs.epa.gov/aqsweb/documents/data_api.html [2022, October 6]. 

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.