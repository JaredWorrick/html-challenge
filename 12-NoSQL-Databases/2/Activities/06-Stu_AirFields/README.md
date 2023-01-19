# Air Fields

In this activity, you will practice selecting specific fields from a Mongo database using PyMongo.

## Instructions

Though you will be using data that you previously imported at the end of the last class, please follow the instructions at the top of the Jupyter Notebook to import the data again, as you will have an opportunity to update the data types using PyMongo.

1. Use the following commands to import these files to a Mongo database:

    ```text
    mongoimport --type csv -d epa -c annual_aqi_by_county --headerline --drop annual_aqi_by_county_2022.csv
    mongoimport --type json -d epa -c ohio_daily_records --drop --jsonArray ohio_daily_records_2022.json
    mongoimport --type json -d epa -c ohio_air --drop --jsonArray ohio_jan_2022.json
    mongoimport --type json -d epa -c ohio_air --jsonArray ohio_feb_2022.json
    ```

2. Run the first six cells to connect to the `epa` database and assign each collection to a variable. If you run into any errors, make sure that you have properly imported the data from your [Resources](Resources) folder.

3. Display the total number of documents in the `annual_aqi_by_county` collection using `count_documents()`.

4. Create a query that finds the documents that have a "parameter" of "Sulfur dioxide" in the `ohio_air` collection and print the number of results using `count_documents()`.

5. Pretty print just the first result from the previous "Sulfur dioxide" query using list indexing.

6. Select only the `parameter`, `units_of_measure`, `observation_count`, `date_local`, `local_site_name`, `site_address`, `city`, and `county` fields from the `ohio_air` collection and use pretty print to print the first two results.

7. Select every field from the `ohio_daily_records` collection **except** the `COUNTY_CODE` and `STATE_CODE` fields and use pretty print to print the first two results.

8. In the `ohio_daily_records` collection, change the data types of the following fields:

    * `CO.PERCENT_COMPLETE` should be converted to a double.

    * `CO.DAILY_AQI_VALUE` should be converted to an integer.

    **Note:** You can do this in a single `update_many()` query, but you may prefer to update them separately.

9. Create a query that finds the documents in the `ohio_daily_records` collection where `CO.UNITS` matches "ppm" and `NO2.UNITS` matches "ppb", and select only the following fields: `CBSA_NAME`, `COUNTY`, `Site Name`, `Date`, `CO`, `NO2`, and `SO2`. Use pretty print to print the first two results.

10. Create a query that finds the documents where the `State` is "Ohio" in the `annual_aqi_by_county` collection and returns only the `County`, `State`, `Days with AQI`, and `Max AQI` fields. Use pretty print to print the first four results.

## References

`ohio_daily_records_2022.json`: United States Environmental Protection Agency. 2022. *Download daily data*. Settings: Year "2022", Geographic Area "Ohio", and Pollutants "CO", "NO2", and "SO2". Available: https://www.epa.gov/outdoor-air-quality-data/download-daily-data [2022, October 14].

`annual_aqi_by_county_2022.csv`: United States Environmental Protection Agency. 2022. *Pre-generated data files*. Annual AQI by county 2022. Available: https://aqs.epa.gov/aqsweb/airdata/download_files.html [2022, October 6]. 

`ohio_jan_2022.json` and `ohio_feb_2022.json`: United States Environmental Protection Agency. 2022. *Air Quality System (AQS) API*. Available: https://aqs.epa.gov/aqsweb/documents/data_api.html [2022, October 6]. 

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.