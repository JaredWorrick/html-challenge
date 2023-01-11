# Practice Performing an Automated Web Scrape

In this activity, we'll scrape data from a website that was created specifically for practicing our skills: [Quotes to Scrape](http://quotes.toscrape.com/). 

## Instructions

* First, open up [Quotes to Scrape](http://quotes.toscrape.com/) in Chrome and familiarize yourself with the page layout.

* Now let’s use DevTools to review the details of the “Top Ten tags” line. Right-click anywhere on the webpage, and then click Inspect. Note that in the DevTools panel, we can use a shortcut to choose an element on the page instead of searching through the tags. To do so, complete the following steps:

    * Click the “Select an element in the page to inspect it” button (which has an arrow icon and appears on the left side of the panel menu).

    * On the webpage, click the element that you want, like the humor tag. DevTools goes to the line of code where the humor tag is nested.

    * Since we are investigating the “Top Ten tags” heading, click the “Select an element in the page to inspect it” button again and click on the "Top Ten tags" text. In the DevTools panel, notice that our text is nested within the `<h2>Top Ten tags</h2>` heading element. Our shortcut has taken us to the `<h2>` tag holding all the text that we want.

* Now scrape the "Top Ten tags" heading by following these steps:

    * Visit the Quotes to Scrape site by using the `browser.visit(url)` function.

    * Create a BeautifulSoup object to parse the HTML code.

    * Extract and print the title by using the `find` method.

* Next, extract all of the Top Ten tags from the webpage by following these steps:

    * Use DevTools to highlight the `<div>` container that holds all the tags, then identify the two classes associated with this division. 
    
    * You should have found the following two classes: `col-md-4` and `tags-box`. Based on the names, which class do you think is specific to the tags you want to scrape? 

    * Now examine the content of the tags `<div>` element. To do so, in DevTools, expand the `<div class="col-md-4 tags-box">` line. What do you notice about the contents?

    * Hopefully you observed that each of the tags is associated with the class `tag-item`. You can use this information to scrape all of the tags. To do so, first find the element associated with the class `tags-box`, then find all of the elements associated with the class `tag-item`. Once you have done this, print all of the tags.

* Congratulations, you have scraped information from this real website! Now end the session by using `browser.quit()`.

- - -

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

