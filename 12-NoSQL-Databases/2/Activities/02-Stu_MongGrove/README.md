# Mongo Grove

In this activity, you will use Jupyter Notebook to test out code that you could then use to build a command-line interface application for the produce department of a supermarket by using PyMongo to enable Python to interact with MongoDB.

## Instructions

You are the purchaser for the produce department of a large supermarket chain. You decide to use MongoDB to create a database of fruits received from your various suppliers.

* Use PyMongo to create a `fruits_db` database, and a `fruits` collection.

* Insert two documents of fruit shipments received by your supermarket into the `fruits` collection. They should contain the following information: 
    * A vendor with the key, `vendor`
    * The type of fruit with the key, `fruit`
    * The number of cases with the key, `case_quantity`, and the number of cases received as an integer
    * The status of the fruit with the key, `ripeness` on a scale of 1 to 3, where the ratings are: 1 for unripe, 2 for ripe, 3 for over-ripe
    *  The date entered in the database in UTC datetime format with the key `date` 

* Because not every supermarket employee is versed in using MongoDB, create a Python script that asks the user for the above information, then inserts a document into the `fruits` collection.

## Hint

* Consult the [documentation](https://docs.python.org/3/library/datetime.html) on the `datetime` library.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.