* Open Terminal and navigate to the Resources folder where mechanics.json and customers.csv are stored.

* Import the `mechanics.json` file with the following line in Terminal:

    ```shell
    mongoimport --type json -d autosaurus -c mechanics --drop --jsonArray mechanics.json
    ```

* Import the `customers.csv` file with the following line in Terminal:

    ```shell
    mongoimport --type csv -d autosaurus -c customers --headerline --drop customers.csv
    ```

* Check the contents of the data in Mongo Shell.

* Run `mongo` from the Terminal to launch Mongo.

* Switch to the `autosaurus` database we created with the previous imports:

    ```shell
    use autosaurus
    ```

* Display the list of collections in the database:

    ```shell
    show collections
    ```

* Find one entry in the customers collection:

    ```shell
    db.customers.findOne()
    ```

* Find the documents in the customers collection where the customer has an Acura for their `car_make`:

    ```shell
    db.customers.find({"car_make": "Acura"})
    ```

* Display the mechanics collection using pretty print:

    ```shell
    db.mechanics.find()
    ```

* Find the mechanic in the mechanics collection that specialises in Acuras:

    ```shell
    db.mechanics.find({"car_specialties": "Acura"})
    ```

* Display the mechanics who work 40 hour weeks:

    ```shell
    db.mechanics.find({"wages.weekly_hours": 40})
    ```

* Convert string field `wages.hourly_rate` to a floating point value or "double":

    ```shell
    db.mechanics.updateMany({}, [ {'$set':{ "wages.hourly_rate" : {'$toDouble': "$wages.hourly_rate"}}} ])
    ```
