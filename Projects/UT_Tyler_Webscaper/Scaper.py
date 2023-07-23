from urllib.request import urlopen
from bs4 import BeautifulSoup

import time
import re

# Return the soup of any url
def soupify(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")
    return soup

# Subject catalog url
subjects_url = r'https://uttyler.smartcatalogiq.com/en/2022-2023/catalog/courses/'
subjects_soup = soupify(subjects_url)

sub_list = []

# Gather all subjects
for div in subjects_soup.findAll('li'):
    link_content = div.find('a').contents[0]
    if re.search(r'[A-Z]{4}', link_content):
        link_content = link_content.lower()
        link_content = link_content.split(' - ')
        link_content[1] = link_content[1].replace(' ', '-')
        sub_list.append(link_content)

courses = []

for subject in sub_list:
    subject_url = f'https://uttyler.smartcatalogiq.com/en/2022-2023/catalog/courses/{subject[0]}-{subject[1]}/'
    subject_soup = soupify(subject_url)

    parent_list = subject_soup.find('ul', {'class': 'sc-child-item-links'})
    list_children = parent_list.findChildren()
    for child in list_children:
        course = child.text
        course_code = subject[0]
        course_num = re.findall(r'[0-9]{4}-?([0-9]{4})?', course)
        course_name = re.findall(r'-?[A-Z][a-z]|[a-z]-? ?', course)[0]
        print(course_num)

        courses.append({'course_code': course_code,
                        'course_num': course_num,
                        'course_name': course_name})
    # print(courses)
    time.sleep(100)






url = r'https://uttyler.smartcatalogiq.com/en/2022-2023/catalog/courses/math-mathematics/3000/math-3345/'

# page = urlopen(url)

# html_bytes = page.read()
# html = html_bytes.decode("utf-8")

# html_soup = BeautifulSoup(html, "html.parser")

# print(html_soup.get_text())

