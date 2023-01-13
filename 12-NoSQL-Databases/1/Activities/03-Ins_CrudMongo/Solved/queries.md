# Update, Delete and Drop in MongoDB

* Use the travel_db

    ```shell
    db
    use travel_db
    ```

* Insert two countries in Africa

    ```shell
    db.destinations.insertOne({'country': 'Egypt', 'continent': 'Africa', major_cities: ['Cairo', 'Luxor']})
    db.destinations.insertOne({'country': 'Nigeria', 'continent': 'Africa', major_cities: ['Lagos', 'Kano']})
    ```

* Show how to update data using `db.[COLLECTION_NAME].updateOne()`

    ```shell
    db.destinations.updateOne({"country": "Egypt"}, {$set: {"continent": "Antarctica"}})
    ```

    * Note that the above will only update the first entry it matches.

* To update multiple entries, use the `updateMany()` method. The following will update all countries listed as being in Africa to now show Antarctica as their continent

    ```shell
    db.destinations.updateMany({"continent": "Africa"}, {$set: {"continent": "Antarctica"}})
    ```

* Ask the class what they think will happen when you run this command, even though a capital doesn't exist.

    ```shell
    db.destinations.updateOne({"country": "Morocco"}, {$set: {"capital": "Rabat"}})
    ```

* Answer: it will add the capital field to the document and show the field can now be updated with the same command.

    ```shell
    db.destinations.updateOne({"country": "Morocco"}, {$set: {"capital": "RABAT"}})
    ```

* Show how to push to an array with `$push`.

    ```shell
    db.destinations.updateOne({"country": "Morocco"}, {$push: {"major_cities": "Agadir"}})
    ```

* The upsert option updates a document if one exists; it otherwise creates a new document.

    ```shell
    db.destinations.updateOne({'country': 'Canada'}, {$set: {'capital': 'Ottawa'}}, {upsert: true})
    ```

* Delete an entry with `db.[COLLECTION_NAME].deleteOne()`.

    ```shell
    db.destinations.deleteOne({"country": "Morocco"})
    ```

* Empty a collection with `db.[COLLECTION_NAME].deleteMany()`.

    ```shell
    db.destinations.deleteMany({})
    ```

* Drop a collection with `db.[COLLECTION_NAME].drop()`.

    ```shell
    db.destinations.drop()
    ```

* Drop a database

    ```shell
    db.dropDatabase()
    ```
