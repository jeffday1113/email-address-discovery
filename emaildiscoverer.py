from collections import deque
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from urlparse import urlparse
import re


class EmailDiscoverer(object):

    def __init__(self, domain_name, limit_discovery_distance):
        self.domain_name = domain_name
        self.visited_pages = set()
        self.pages_queue = deque()
        self.pages_queue.append(domain_name)
        self.email_set = set()
        self.limit_discovery_distance = limit_discovery_distance

    def discover_emails(self):
        driver = webdriver.PhantomJS()
        try:
            print "Found these email addresses:"
            counter = 0
            while len(self.pages_queue) > 0:
                current_page = self.pages_queue.popleft()
                #print self.limit_discovery_distance
                #print current_page
                if current_page not in self.visited_pages:
                    self.visited_pages.add(current_page)
                    current_url = driver.current_url
                    driver.get('http://' + current_page)
                    if driver.current_url == current_url:
                        driver.get('http://www.' + current_page)
                    self.check_anchor_tags(driver.find_elements_by_tag_name("a"), counter)
                    self.check_text(driver.find_elements_by_xpath("//*[contains(text(), '@')]"))
                    if counter == 0 and self.limit_discovery_distance:
                        counter += 1
            driver.quit()
        except Exception as e:
            print e
            driver.quit()

    def check_anchor_tags(self, elements, counter):
        for elem in elements:
            try:
                linked_page = elem.get_attribute("href")
            except StaleElementReferenceException:
                continue
            if linked_page:
                if EmailDiscoverer.is_email(linked_page):
                    self.check_email_and_print(linked_page)
                    continue
                if not self.limit_discovery_distance or counter == 0:
                    parsed_url = urlparse(linked_page)
                    if self.sub_domain_boolean(parsed_url.netloc):
                        if EmailDiscoverer.filter_link(linked_page) not in self.visited_pages:
                            self.pages_queue.append(EmailDiscoverer.filter_link(linked_page))

    def check_text(self, elements):
        for elem in elements:
            match = re.search(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', elem.text)
            if match:
                email = match.group(0)
                if email not in self.email_set:
                    print email
                    self.email_set.add(email)

    def check_email_and_print(self, email):
        email = email.replace('mailto:', '')
        if email not in self.email_set:
            print email
            self.email_set.add(email)

    @staticmethod
    def is_email(linked_page):
        return 'mailto' in linked_page

    @staticmethod
    def filter_link(link):
        if 'http://' in link:
            link = link.replace('http://', '')
        elif 'https://' in link:
            link = link.replace('https://', '')
        if 'www.' in link:
            link = link.replace('www.', '')
        if '//' in link:
            link = link.replace('//', '')
        return link

    @staticmethod
    def add_http(domain):
        return 'http://' + domain

    def sub_domain_boolean(self, domain):
        if self.domain_name.startswith('www'):
            return (self.domain_name == domain) or (self.domain_name[self.domain_name.index('.') + 1:] == domain)
        else:
            return self.domain_name in domain
