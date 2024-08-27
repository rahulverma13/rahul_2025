import requests
from bs4 import BeautifulSoup
import emoji

def get_rating_emoji(avg_rating):
    if avg_rating >= 4.5:
        return emoji.emojize(":grinning_face_with_smiling_eyes: Excellent")
    elif avg_rating >= 3.5:
        return emoji.emojize(":slightly_smiling_face: Good")
    elif avg_rating >= 2.5:
        return emoji.emojize(":neutral_face: Average")
    elif avg_rating >= 1.5:
        return emoji.emojize(":worried_face: Poor")
    else:
        return emoji.emojize(":angry_face: Terrible")

# Function to fetch a random Wikipedia article
def fetch_article():
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', {'id': 'firstHeading'}).text
        paragraphs = soup.find_all('p')
        content = "\n".join([para.text for para in paragraphs])
        return title, content
    else:
        return None, None

def run():
    ratings = []
    while True:
        choice = input("What would you like to do?\n1: Visit and rate a random Wikipedia article\n2: View your average rating\n3: Exit this session\n").strip()
        if choice == "1":
            title, content = fetch_article()
            if title and content:
                print(f"\nTitle: {title}\n")
                print(content[:4000]) 
                rating = input("\nRate this article (1 to 5): ").strip()
                try:
                    rating = int(rating)
                    if 1 <= rating <= 5:
                        ratings.append(rating)
                        print(f"Thank you for rating! Your rating: {rating}")
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
        elif choice == "2":
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                emoji_rating = get_rating_emoji(avg_rating)
                print(f"Average rating: {avg_rating:.2f} {emoji_rating}")
            else:
                print("No ratings available.")
        elif choice == "3":
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                emoji_rating = get_rating_emoji(avg_rating)
                print(f"Exiting session. Your average rating was: {avg_rating:.2f} {emoji_rating}")
            else:
                print("Exiting session. No ratings were provided.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
run()
