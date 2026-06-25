from bs4 import BeautifulSoup

html_content="""
<html>
<head>
    <title>Example Page</title>
</head>
<body>
    <h1>welcome to beautiful soup</h1>
    <p class="intro">beautiful soup makes sore throats feel better</p>
    <div id="content">
        <p>Here are some links:</p>
        <a href="https://learn.digitalschool.tech/login/index.php">Link 1</a>
        <a href="https://learn.digitalschool.tech/login/index.php">Link 2</a>
        <a href="https://learn.digitalschool.tech/login/index.php">Link 3</a>
    </div>
</body>
</html
"""


soup = BeautifulSoup(html_content,'html.parser')

print("Title of the page:" , soup.title.text)

intro_text = soup.find('p', class_='intro').text
print("Intro text:", intro_text)

div_content = soup.find('div', id='content')
links = div_content.find_all('a')
for link in links:
    print("Link:", link['href'])

first_link = soup.find('a')
print("First link text:", first_link.text)
print("Next sibling of the first link:", first_link.next_sibling)

paragraphs = soup.select('div#content p')
for paragraph in paragraphs:
    print("paragraph inside content", paragraph.text)

new_tag = soup.new_tag('b')
new_tag.string = "Important"
soup.h1.append(new_tag)

print("modified h1 tag:", soup.h1)