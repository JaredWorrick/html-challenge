# Create a GardenDB

In this activity, you will gain further practice with CRUD operations in MongoDB by creating a database centered around gardening.

## Instructions

* Create a new database called `gardenDB` using the mongo shell.

* Create a collection called `plants` that contains the following:
  * A string field for `plantName`
  * An integer field for `yearsGrowing`
  * A Boolean field for `stillAlive`
  * An array of strings called `PlantNutrition` to store information about how best to keep the plant alive

* Insert three new documents into the collection. You can be creative with what you put in here and have some fun with it. Getting some practice using the commands is more important than accuracy of information.

* Update the `yearsGrowing` fields for your documents so that they are one greater than their original values.

* Update the `stillAlive` value for one of the documents so that it is now `false`.

* Add a new value into the `plantNutrition` array for one of the documents.

* Find the plant in the collection that isn't alive and delete it from the collection.

* Drop the `plants` collection.

* Delete the `gardenDB` database

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.