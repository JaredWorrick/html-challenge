# Import, Update, and Explore

* Write a command that imports the data from [annual_aqi_by_county_2022.csv](../Resources/annual_aqi_by_county_2022.csv) to a database called `epa` and a collection called `annual_aqi_by_county`. If the collection already exists, drop the collection.

    ```
    mongoimport --type csv -d epa -c annual_aqi_by_county --headerline --drop annual_aqi_by_county_2022.csv
    ```

* Write a command that imports the data from [ohio_daily_records_2022.json](../Resources/ohio_daily_records_2022.json) to a database called `epa` and a collection called `ohio_daily_records`. If the collection already exists, drop the collection.

    ```
    mongoimport --type json -d epa -c ohio_daily_records --drop --jsonArray ohio_daily_records_2022.json
    ```

* Write a command that imports the data from [ohio_jan_2022.json](../Resources/ohio_jan_2022.json) to a database called `epa` and a collection called `ohio_air`. If the collection already exists, drop the collection.

    ```
    mongoimport --type json -d epa -c ohio_air --drop --jsonArray ohio_jan_2022.json
    ```

* Write a command that imports the data from [ohio_feb_2022.json](../Resources/ohio_feb_2022.json) to a database called `epa` and a collection called `ohio_air`. **Note:** This is the same collection used in the previous import so be sure not to drop the collection in advance.

    ```
    mongoimport --type json -d epa -c ohio_air --jsonArray ohio_feb_2022.json
    ```

* Use the `epa` database.

    ```
    use epa
    ```

* Show all the collections in the `epa` database.

    ```shell
    show collections
    ```

    This should display the following output:

    ```text
    annual_aqi_by_county
    ohio_air
    ohio_daily_records
    ```

* Verify that there is data in each of the 3 collections (`ohio_daily_records`, `annual_aqi_by_county`, and `ohio_air`) by using `findOne()` to display an entry.

    ```shell
    db.ohio_daily_records.findOne()
    db.annual_aqi_by_county.findOne()
    db.ohio_air.findOne()
    ```

* Verify that there is data from January 2022 in the `ohio_air` collection by seaching on the `date_local` field.

    ```shell
    db.ohio_air.findOne({"date_local": "2022-01-01"})
    ```

* Verify that there is data from February 2022 in the `ohio_air` collection by seaching on the `date_local` field.

    ```shell
    db.ohio_air.findOne({"date_local": "2022-02-01"})
    ```

* Update the `DAILY_AQI_VALUE` nested under `CO` in the `ohio_daily_records` collection to change the string values to integers.

    ```shell
    db.ohio_daily_records.updateMany({}, [ {'$set':{ "CO.DAILY_AQI_VALUE" : {'$toInt': "$CO.DAILY_AQI_VALUE"}}} ])
    ```

* Update the `PERCENT_COMPLETE` nested under `CO` in the `ohio_daily_records` collection to change the string values to doubles.

    ```shell
    db.ohio_daily_records.updateMany({}, [ {'$set':{ "CO.PERCENT_COMPLETE" : {'$toDouble': "$CO.PERCENT_COMPLETE"}}} ])
    ```

* Find a record in the `ohio_daily_records` collection where `CO.UNITS` matches "ppm" and `NO2.UNITS` matches "ppb"

    ```shell
    db.ohio_daily_records.findOne({"CO.UNITS": "ppm","NO2.UNITS": "ppb"})
    ```

