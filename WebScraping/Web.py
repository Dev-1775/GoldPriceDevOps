from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    html_tags = soup.find_all('h5')
    for course in html_tags:
        print(course.text)