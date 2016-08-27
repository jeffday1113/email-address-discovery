# Jeffrey Day Email Address Discovery Coding Challenge

####Code Notes:
* Implemented in Python.
* In order to run program, simply run the following: `python email-address-discovery.py <domain_name>`
* I added a runtime option called `limit_discovery_distance`. This limits the search for discoverable pages to links only found on the initial input page. I did this because I wasn't entirely sure what "any discoverable page on the website" meant in the instructions. I added this feature to allow for a quick search as well as a very extensive search of a domain's pages. This option is used in the following way: `python email-address-discovery.py <domain_name> --limit_discovery_distance`,
* `emaildiscoverer.py` contains the class and associated methods that perform the domain crawling and email address search initiated by the above mentioned file.

####Libraries used (outside of standard python libraries):
* Selenium (using a web driver dependent on phantomjs)

####Installation setup to run program:

1. Install selenium library using pip (`pip install selenium`).
2. Download phantomjs for your OS at the following link: http://phantomjs.org/download.html.
3. Unzip the file.
4. Add the folder containing the phantomjs executable to your path variable in your terminal.
5. Reload your terminal in order to refresh the path.

####Program Design and Library Choices explained:

* These notes may be more than what is required, but I just wanted to explain all the thoughts and choices that went through my mind while working on this coding challenge.
* My initial instinct for finding discoverable pages was to search for anchor tags (`<a>`) within the base html of the initial web page on the domain provided. However, I quickly realized that many links are created using the help of JavaScript, and that getting just the initial html would not necessarily provide all possible links. I found the best balance of not too heavy of a library, but still powerful enough to execute client side javascript to look for discoverable pages seemed to be selenium. Although selenium often uses an actual browser, I decided to use phantomjs in order to avoid the overhead of using an actual browser.
* I tried to do my best to stick to the suggested time limit of 2-4 hours. As a result, once I found a library that seemed feasible to work with the previously stated javascript limitation, I went with it. However, because selenium does a lot under the hood, the performance of my program with a large number of discoverable pages isn't great.
* One idea I had to increase performance was to store a hashed value of the pages visited in the `visited_pages` set instead of the string itself. This would make the operation of checking to see if a page had been visited yet faster since it's quicker to check hashed numeric values than string values. If I had more time, I would have tried this.
* I initially considered using the Scrapy framework (http://scrapy.org/) to assist with finding discoverable pages in a given domain, but figured that you guys wanted to see the implementation of the functionality of crawling a domain for discoverable pages so I decided against it.
* With regards to crawling all of the pages in a domain, I started my algorithm design based off a breadth first search.
