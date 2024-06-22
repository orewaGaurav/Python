# import requests
# from bs4 import BeautifulSoup
# response = requests.get("https://www.niet.co.in/")
# soup =BeautifulSoup(response.content,'html.parser')
# print(soup) 


# from bs4 import BeautifulSoup
# html_content = '''
# <html>
# <head><title>Example Page</title></head>
# <body>
# <p class="paragraph">This is the first paragraph.</p>
# <p>This is the second paragraph.</p>
# </body>
# </html>
# '''
# soup = BeautifulSoup(html_content, 'html.parser')
# paragraphs = soup.find_all('p')
# print(paragraphs)
# for p in paragraphs:
#     print(p.get_text())

from bs4 import BeautifulSoup
html_content = """
<!DOCTYPE html>
<html>
<head><title>Example Page</title></head>
<body>
<a href="https://example.com/page1" class="link">Page 1</a>
<a href="https://example.com/page2" class="link">Page 2</a>
</body>
</html>
"""
soup = BeautifulSoup(html_content, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link['href'])

