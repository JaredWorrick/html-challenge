# Warm-Up Activity

In this activity, you will import the data you will be using for the remainder of this class, and run a few searches to explore the collection. 

## Instructions

* In your Terminal, navigate to the folder where your [artifacts.json](Resources/artifacts.json) file is stored.

* Import the dataset with `mongoimport --type json -d met -c artifacts --drop --jsonArray artifacts.json`

* In Jupyter Notebook, open [WarmUp_Unsolved.ipynb](Unsolved/WarmUp_Unsolved.ipynb) and use the following instructions to check that you created the database correctly, and set your variables:

    * Import MongoClient from PyMongo and pprint from pprint.

    * Create an instance of MongoClient.

    * Confirm that you imported the data correctly by listing your database names.

    * Assign the met database to a variable name.

    * Review the collections in your new database.

    * Use `pprint` and `find_one()` to review a document in the artifacts collection.

    * Assign the artifacts collection to a variable.

* Review the code we have explored previously to find:

    * How many documents have the `culture` "Nayarit" using `count_documents()`

    * How many documents have a height of at least 40cm using `$gte`

* Pretty print the results of a query that:

    * Finds the documents where:

        * The culture is "Nayarit" or "Central American Isthmus" and

        * The height is less than or equal to 40cm

    * Returns only the following fields: "title", "department", "culture", "measurements", and "objectURL"

    * Sorts alphabetically by "title"

    * Limits the results to 5

## Reference

[The Metropolitan Museum of Art](https://www.metmuseum.org/) (2022). The Metropolitan Museum of Art Collection API https://metmuseum.github.io/. Licenced under the [Creative Commons 0 Licence](https://creativecommons.org/publicdomain/zero/1.0/).<br />
Accessed Oct 3, 2022. Data collected from departmentId=5 ("Arts of Africa, Oceania, and the Americas") and search string "animal".

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.