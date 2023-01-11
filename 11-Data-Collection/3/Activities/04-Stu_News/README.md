# News Scraping

* In this activity, you will scrape news summaries across multiple pages from the Global Voices news [site](https://globalvoices.org/page/2/).

## Instructions

* Open page 2 of [Global Voices news](https://globalvoices.org/page/2/). Use DevTools to identify the elements that contain the data you need to scrape.

* Within your Jupyter notebook, use Splinter to click on any popup or lightbox to make it disappear.

* Create an empty list to store your article summaries.

* Create a function that will perform your web scraping. The function should perform the following tasks:

  * Collect the HTML from the browser.

  * Parse the HTML and save it as a Beautiful Soup object.

  * On any given page, scrape the **title** and the **date** of each article.

    > **Note:** The date is in the format `DD _MM YYYY`. See if you can strip the underscore before you save the date.

  * For each article summary, the title and the date should be structured as a dictionary. All dictionaries should be contained in a Python list.

* Create a `for` loop that will:

  * Call your web scraping function to scrape the article summaries on a page.
  
  * Click the button to go to the next page of older articles.
  
  * Repeat the process for a total of five pages.

* Import the scraped data (a list of dictionaries) into a Pandas dataframe. Using Python, Pandas, or both, convert the dates into a usable datetime type.

* Remember that you should begin on page 2, and move on to older stories.

* Below is an abbreviated example of what your scraped data might look like.

  ```python
  [{'header': 'Portugal: Human rights activist fighting racism wins international award',
    'date': '29 _12 2021'},
  {'header': 'Where is Qatari human rights defender Noof Al-Maadeed?',
    'date': '29 _12 2021'}]
  ```

## Hint

* Consider using Pandas' [`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html) method to convert the dates.

## Reference

[Global Voices](https://globalvoices.org) is a news website that releases its content under a Creative Commons license ([CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)). This means you are free to scrape the content and redistribute it, as long as you give credit to the source (provide attribution).

- - -

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
