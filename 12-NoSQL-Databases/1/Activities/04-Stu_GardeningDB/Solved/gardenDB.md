# Create a Garden Database

* Create a new database called `gardenDB` using the mongo shell.

    ```
    use gardenDB
    ```

* Create a collection called `plants` with a string field for `plantName`, an integer field for `yearsGrowing`, a boolean field for `stillAlive`, and an array of strings for `plantNutrition`.


* Insert three new documents into the collection. Be creative and have some fun with the documents that you add.

    ```
    db.plants.insertOne({"plantName":"Fuschia", "yearsGrowing":10, "stillAlive": true, "plantNutrition":["nitrogen", "sulfur", "calcium", "potassium"]})

    db.plants.insertOne({"plantName":"Watermelon", "yearsGrowing":2, "stillAlive": true, "plantNutrition":["nitrogen based fertilizer at onset", "phosphorus and potassium fertilizer when flowering"]})

    db.plants.insertOne({"plantName":"Avocado", "yearsGrowing":12, "stillAlive": true, "plantNutrition":["nitrogen", "zinc"]})
    ```

* Update the `yearsGrowing` fields for your documents so that they are one greater than their original values.

    ```
    db.plants.updateOne({"plantName":"Fuschia"},{$set:{"yearsGrowing":11}})
    db.plants.updateOne({"plantName":"Watermelon"},{$set:{"yearsGrowing":3}})
    db.plants.updateOne({"plantName":"Avocado"},{$set:{"yearsGrowing":13}})
    ```

* We can actually also use `updateMany()` to update all documents at once if we want to update them the same way. The following will have the same effect as updating each document individually as we did above:

    ```
    db.plants.updateMany({},{$inc: {"yearsGrowing": 1}})
    ```

    [MongoDB documentation on `$inc`](https://www.mongodb.com/docs/manual/reference/operator/update/inc/)

* Update the `stillAlive` value for one of the documents so that it is now `false`.

    ```
    db.plants.update({"plantName":"Fuschia"},{$set:{"stillAlive": false}})
    ```

* Add a new value into the `plantNutrition` array for one of the documents.

    ```
    db.plants.update({"plantName":"Watermelon"},{$push:{"plantNutrition":"1-2in water per week"}})
    ```

* Find the plant in the collection that isn't alive and remove it from the collection.

    ```
    db.plants.deleteOne({"stillAlive":false})
    ```

* Drop the `plants` collection

    ```shell
    db.plants.drop()
    ```

* Delete the `gardenDB` database

    ```shell
    db.dropDatabase()
    ```