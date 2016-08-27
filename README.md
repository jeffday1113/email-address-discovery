# Jeffrey Day Email Address Discovery Coding Challenge

###Code Notes:
* Implemented in Python
* In order to run program , simply run the following: `python email-address-discovery.py <domain_name>`

###Libraries used (outside of standard python libraries):
* Selenium (used a web driver dependent on phantomjs)

###Installation steps for proper setup to run program:

1. Install selenium library using pip (`pip install selenium`)
2. Download phantomjs for the appropriate OS at the following link: http://phantomjs.org/download.html
3. Unzip the file and place it an appropriate file location
4. Add the folder where the phantomjs executable is located to your path variable in your terminal
5. Reload your terminal in order to refresh the path

###Program Design and Library Choices explained:

* These notes may be more than what you require, but I just wanted to explain all the thoughts and choices that went through my mind while working on this coding challenge.
* My intial instinct for solving this problem was to search for anchor tags (`<a>`) within the base html of the initial web page on the domain provided in order to find discoverable pages to search. However, I quickly realized that many links are created using the help of JavaScript, and that getting just the initial html would not necessarily provide all possible links. The best balance of not too large of a library but still powerful enough to execute client side javascript in order to look for discoverable pages seemed to be selenium. Although selenium often uses an actual browser, I decided to use phantomjs in order to avoid the overhead of using an actual browser.
* I tried to do my best to stick to the suggested time limit of 2-4 hours. As a result, once I found a library
