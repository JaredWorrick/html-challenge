# Stack Scrape

In this activity, you will scrape Stack Overflow's Python page and store the results in a Python list of dictionaries.


## Instructions

You may create a new Jupyter Notebook or use the [unsolved notebook](Unsolved/stack_overflow_unsolved.ipynb) as your guide.

Visit [Stack Overflow's Python page](https://stackoverflow.com/questions/tagged/python?sort=MostVotes&edited=true) with Splinter's automated browser. Scrape information from all the questions on the first page. For each question, use BeautifulSoup to scrape the following pieces of information:

* The summary (e.g. 'What does the "yield" keyword do?' for the first question)

* The number of votes for that question

* The excerpt (the longer text below the summary)

As you scrape, use Chrome's DevTools to identify elements and their CSS selectors, which you will then use in BeautifulSoup.

Next, organize your information into a Python list of dictionaries. That is, information from each question will be organized into a dictionary like the below, and a list will contain all these dictionaries.

```python
{'summary': 'What does the "yield" keyword do?',
  'votes': '11692',
  'excerpt': "What is the use of the yield keyword in Python? What does it do?\nFor example, I'm trying to understand this code1:\ndef _get_child_candidates(self, distance, min_dist, max_dist):\n    if self._leftchild ..."}
```

Don't forget to close your automated browser!

## Reference

[Stack Overflow](https://stackoverflow.com) [user contributions](https://stackoverflow.com/help/licensing) are licensed under a [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) license.

- - -

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

