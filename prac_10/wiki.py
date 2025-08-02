"""
Wikipedia search interface - user input loop.
"""

def main():
    """Prompt for Wikipedia page titles and echo input until blank."""
    while True:
        title = input("Enter page title: ")
        if not title:
            print("Thank you.")
            break
        print(f"You searched for: {title}")


if __name__ == "__main__":
    main()
