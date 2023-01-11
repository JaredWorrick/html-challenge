# Mars Facts Scrape

In this activity, you'll practice scraping data that was stored in a table on a website.

## Instructions

* First, open up the [Mars Facts](https://static.bc-edx.com/data/web/mars_facts/index.html/) website in Chrome and become familiar with the layout.

* You'll scrape the data from the table labeled "Mars Planet Profile." Use Chrome DevTools to inspect that element. What is the class of the table you want to scrape?

* Now that you know the class you are looking for, begin the scraping process by importing the necessary libraries and setting up Splinter.

* First, use Splinter to visit the Mars Facts site and collect the html.

* Create a BeautifulSoup parser to parse the html from the website.

* Scrape and store the table by using the `find` method alongside the class you identified by using Chrome DevTools.

    <details>

    <summary>Hint
    </summary>
    Your `find` function should have two parameters: `'table'` and `class_='table-striped'`).

    </details>
    <br>

* Now store the table information in a dictionary by following these steps:

    * Create an empty dictionary.
    
    * Use the `find_all` method to store all the rows of the table in a variable.
    
    * Use a `for` loop to iterate through each of the rows in the table.
    
    * For each row in the table, use the `find` method to extract the text for each header and to extract the text for the data associated with that header.
    
    * Add the extracted header and associated data in the dictionary, with the header as the key and the data as the value.

    <details>

    <summary>Hint
    </summary>
    You can find all the rows by using `find_all('tr')`. For each row, use row.find('th').text to extract the header text.

    </details>
    <br>
    
* Display your scraped table dictionary to confirm the process was successful.

* Quit your browsing session.

- - -

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.