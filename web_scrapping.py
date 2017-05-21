'''
Created on 21-May-2017

@author: mahesh
'''

import requests
from bs4 import BeautifulSoup

def get_page(website_url):
    '''
    Reads the Website url and raises exception if page does not exists
    :param website_url:
    '''
    page = requests.get(website_url, headers={'User-Agent': 'Mozilla/5.0'})
    if page.status_code != 200:
        raise Exception("Page not found")
    return page.status_code, page


def extract_elements_from_list(book_categories_element):
    '''
    Extract book categories list
    :param book_categories_element:
    '''
    result = []
    category_list_elements = BeautifulSoup(str(book_categories_element.contents[1]), 'html.parser').findAll("li")
    if category_list_elements is not None and len(category_list_elements) > 0:
        element_list = BeautifulSoup(str(category_list_elements[0]), 'html.parser').findAll("li")
        total_elements = len(element_list)
        if total_elements > 1:
            for count in range(1, total_elements):
                result.append(element_list[count].text.replace("\n", "").replace(" ", ""))
    return result


def get_all_book_categories(soup):
    '''
    Reads book categories div element
    :param soup:
    '''
    book_categories_elements = soup.findAll("div", {"class": "side_categories"})
    if book_categories_elements is not None and len(book_categories_elements) > 0 :
        return extract_elements_from_list(book_categories_elements[0])
    return None


if __name__ =="__main__":
    status_code, page = get_page("http://books.toscrape.com/")
    soup = BeautifulSoup(str(page.content), 'html.parser')
    book_categories = get_all_book_categories(soup)
    print book_categories
