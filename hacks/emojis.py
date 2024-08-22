# Note: pip install emoji required
from emoji import emojize as em

name = input("What is your name?\n")

print(em(f"Why hello there dear {name}! It is nice to meet you :thumbs_up: :grinning_face:"))
