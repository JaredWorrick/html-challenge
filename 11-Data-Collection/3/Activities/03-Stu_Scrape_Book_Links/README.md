# Scrape Book Links

In this activity, you'll practice automated scraping on another website that was created specifically for practicing our skills: [Books to Scrape](http://books.toscrape.com/). 

## Inspect the Website

You'll be scraping the links associated with each of the books on this website, so get started by using DevTools to review the details for each book.

* First, open up the website in Chrome and familiarize yourself with the page layout. Where can you find a link to more details about each book?

* Now inspect the element where the additional book details are linked. What class is the link contained within?

## Scrape Book Links from One Page

Now that you know the class you are looking for, you can begin the scraping process. 

* Run the cells to import the necessary libraries and to set up the browser.

* Use the `browser.visit(url)` function to visit the website.

* Create a BeautifulSoup parser to parse the HTML code from the page you visited.

* Use the `find_all` function to locate and store all of the website content associated with the class you previously identified by using DevTools.

* Create a blank list, then use a `for` loop to extract each of the links associated with the books and store them in that list.

* Print the list to confirm that you were successful.

## Scrape Book Links from Multiple Pages

Since you have confirmed that your code works and you are able to scrape the book links, now you can automate the scraping process by scraping multiple website pages.

* Look back at the page, and find the button that allows you to click the next page. How is it labeled?

* Use the label text that you found, the `browser.links.find_by_partial_text` method, and the `click` method to automatically move to the next page. Run your code and use the open browser window to confirm that you successfully advanced to the next page.

* Now use a for loop and the code you wrote for the previous section to scrape the book links from the first three pages of the website. Display your results by printing the page number, followed by the links on that page.

* Congratulations, you have automated the process of scraping multiple website pages! Now end the session by using `browser.quit()`.

- - -

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
