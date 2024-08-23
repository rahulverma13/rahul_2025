from newspaper import Article
from IPython.display import display, Markdown

# Website that opens a random wikipedia article
randomUrl = "https://en.wikipedia.org/wiki/Special:Random"

while True:
    choice = input("What would you like to do?\n1: Visit and rate a random wikipedia article\n2:View your average rating\n3:Exit this session\n").strip()
    match choice:
        case "1":
            article = Article(randomUrl)
            article.download()
            article.parse

            display(Markdown(article.title))
            display(Markdown(article.text))