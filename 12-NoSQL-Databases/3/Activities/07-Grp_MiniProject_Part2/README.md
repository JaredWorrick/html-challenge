# MongoDB Mini-Project Part 2: Aggregation and Analysis

For Part 2 of the mini-project, you will practice building a more complex query and another aggregation pipeline, then normalizing your resulting DataFrame. 

## Instructions

* Run the first two blocks of code to import your dependencies, create an instance of MongoClient, and assign the database and collection to variables.

* Write a query that:

    * Uses `find()` to find documents about artifacts that come from the "Maya" culture and returns the following fields: `accessionNumber`, `accessionYear`, `classification`, `country`, `department`, `measurements.elementMeasurements.Height`, `measurements.elementMeasurements.Width`, `measurements.elementMeasurements.Depth`, `medium`, `title`,`objectURL`.

    * Uses `sort()` to sort by the artifact's height.

    * Uses `limit()` to limit the number of results to 5.

* Convert the results to a Pandas DataFrame and then display the DataFrame.

* Build an aggregation pipeline that:

    * Matches: 

        * Artifacts that have a width greater than or equal to 10cm and less than 50cm

        * Artifacts that have a height greater than or equal to 20cm and less than 60cm

        * Artifacts that have "Sculpture" as part of their classification

    * Counts the artifacts and groups by: classification and then culture

        **Hint:** Set `_id` to a list or a dictionary of the fields that are being grouped on. If you use a dictionary, you will also need to assign names (or keys) for the fields you are selecting.

    * Sorts by count in descending order

* Pretty print the first 10 results of the aggregation pipeline.

* Write code that will extract the fields from `_id` from the aggregation pipeline to create a Pandas DataFrame that will include the following columns: classification, culture, number of artifacts. If necessary, rename and reorder the columns to match.

    > **Note:** There are multiple ways to do this, but the easiest way is to use `pd.json_normalize()`. If you need help using this new Pandas method, [check out the documentation](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html).

## Reference

[The Metropolitan Museum of Art](https://www.metmuseum.org/) (2022). The Metropolitan Museum of Art Collection API https://metmuseum.github.io/. Licenced under the [Creative Commons 0 Licence](https://creativecommons.org/publicdomain/zero/1.0/)<br />
Accessed Oct 3, 2022. Data collected from departmentId=5 ("Arts of Africa, Oceania, and the Americas") and search string "animal".

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.