# MongoDB Mini-Project Part 1: Import Data from an API

In this activity, you will collect additional data from the Metropolitan Museum of Art API and update the database with the new data.

## Instructions

### Part 1: Connect to the Database

* Import your dependencies: MongoClient from pymongo, pprint from pprint, json, and requests.

* Create an instance of MongoClient.

* Assign the met database to a variable called `db`.

* Assign the artifacts collection to a variable called `artifacts`.

### Part 2: Collect the Data

You have been supplied with a list of ObjectIDs from the Met's API where the departmentId is 5 and the query string is "cave" (https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=5&q=cave).

* Run the code provided to extract the data from the Met's API about each of the artifacts in the `cave_ids` list.

### Part 3: Update the Database

Some of the artifacts collected are already in your database! Starting with one result, you will write code to check the database to see if an artifact is already in the collection. If it's not, you will add it to the database. Then, you will combine your code to loop through your results and only add the artifacts that are not yet in the collection.

Use the following instructions as a guide:

* Choose just one item from the returned data and set it to a variable called `item_to_add`.

    **Hint:** Use the `returned_data_list` and square bracket notation to select a single item from the list.

* Pretty print `item_to_add`.

* Using the `objectID` from `item_to_add`, write a query to check if the item already exists in the artifacts collection.

* Using the above query, write an `if` statement that checks if the result equals `None`.

* Inside your `if` statement:

    * Use `insert_one` to add `item_to_add` to the artifacts collection.

    * Print out the `objectID` when it is added to the collection.

* Combine the above steps to loop through the whole list of data contained in `returned_data_list` only adding to the collection when the artifact does not yet exist in the database. Follow these steps:

    * Loop through `returned_data_list`.

    * Save the data from the list item to the `item_to_add` variable.

    * Check if the artifact already exists in the collection.

    * Inside your `if` statement:

        * Use `insert_one` to add `item_to_add` to the artifacts collection.

        * Print out the `objectID` when it is added to the collection.

## Reference

[The Metropolitan Museum of Art](https://www.metmuseum.org/) (2022). The Metropolitan Museum of Art Collection API https://metmuseum.github.io/. Licenced under the [Creative Commons 0 Licence](https://creativecommons.org/publicdomain/zero/1.0/)<br />
Accessed Oct 3, 2022. Data collected from departmentId=5 ("Arts of Africa, Oceania, and the Americas") and search string "animal".

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.