# https://github.com/nosewad/anilist_link_opener
import webbrowser
import sys
import time
import collections


anime_list = []
anime_list_copy = []
processed_anime = []


# asks for file location then translates to a list
with open(
    input("Enter file location or type file name if it's in the same directory: ")
) as file:
    for line in file:
        anime_list.append(line.rstrip("\n"))

anime_list_copy = anime_list.copy()

# asks user for batch size
user_number = int(
    input("How many tabs would you like to open at once? 10 - 15 is recommended. ")
)


# asks user if they would like to continue, quits if not
def question():
    user_input = input(f"Would you like to open another {user_number} links? y/n ")

    if user_input == "y" or "Y":
        open_anime()
    elif user_input == "n" or "N":
        sys.exit()
    else:
        print("Invalid response.")


# opens anilist.co link in browser
def open_anime():
    x = 0
    while x <= (user_number - 1):
        ani_link = f"https://anilist.co/search/anime?search={anime_list[0]}"
        webbrowser.open_new_tab(ani_link)
        processed_anime.append(anime_list[0])
        anime_list.pop(0)
        x += 1
        if collections.Counter(processed_anime) == collections.Counter(anime_list_copy):
            print("Finished")
            sys.exit()
        time.sleep(0.25)
    x = 0
    question()


open_anime()
