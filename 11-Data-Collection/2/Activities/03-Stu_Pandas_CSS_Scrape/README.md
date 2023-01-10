# Pandas Scrape

In this activity, you will use BeautifulSoup to extract information from a simplified version of the official Pandas website.

## Instructions

* Follow these steps to set up for web scraping:

  * Create a new Jupyter notebook and import BeautifulSoup.
  
  * Copy and paste the code of the provided HTML file into a Python string.

  * Create an instance of BeautifulSoup to parse the HTML.

* Use BeautifulSoup to retrieve the following:

  * The **text** of all `h3`-level headers.

  * The text and URLs of only the first section ("Getting Started"). Use the `id` of this section to scrape the data.

  * **All** URLs on the page.

## Bonus

* Each subsection on the page consists of a header, e.g. "Getting Started" and links. Write Python code to automate the collection of headers and link URLs in a logical structure. Below is an example of what you might end up with.

  ```python
  {'Getting Started': ['https://pandas.pydata.org/getting_started.html',
    'https://pandas.pydata.org/docs/getting_started/index.html'],
  'Documentation': ['https://pandas.pydata.org/docs/user_guide/index.html',
    'https://pandas.pydata.org/docs/reference/index.html',
    'https://pandas.pydata.org/docs/development/index.html'],
  'The pandas Community': ['https://pandas.pydata.org/about/index.html',
    'https://stackoverflow.com/questions/tagged/pandas',
    'https://pandas.pydata.org/community/ecosystem.html']}
  ```

* The above data structure is a dictionary. Each key in the dictionary corresponds to a section title, and each dictionary value is a list of the URLs in that section.

- - -

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.


© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.