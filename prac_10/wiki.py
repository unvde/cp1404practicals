"""
Wikipedia search interface - user input loop.
"""

import wikipedia

def main():
    """Prompt for Wikipedia page titles and display basic info."""
    while True:
        title = input("Enter page title: ")
        if not title:
            print("Thank you.")
            break
        page = wikipedia.page(title)
        print(page.title)
        print(page.summary)
        print(page.url)

if __name__ == "__main__":
    main()
