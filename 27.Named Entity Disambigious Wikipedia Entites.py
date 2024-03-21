import wikipediaapi

# Initialize Wikipedia API with a user agent
wiki = wikipediaapi.Wikipedia('en', user_agent="MyWikiBot/1.0 (contact@example.com)")

def disambiguate_entity(entity):
    page = wiki.page(entity)
    if page.exists():
        return page.title, page.fullurl
    else:
        return "Not found", ""

def main():
    sentences = [
        "Apple is a leading tech company.",
        "I love apples as a fruit.",
        "Python is a popular programming language.",
        "The python is a non-venomous snake."
    ]

    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word.istitle():
                title, url = disambiguate_entity(word)
                print(f"{word}: {title} - {url}")
                break  

if __name__ == "__main__":
    main()
