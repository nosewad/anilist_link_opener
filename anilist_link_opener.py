import webbrowser
import sys
import time
import collections


anime_list = []
processed_anime = []


# Asks for file location then translates to a list
with open(input("Enter File location: ")) as file:
    for line in file:
        anime_list.append(line.rstrip("\n"))


while True:
    i = 0
    for anime in anime_list:

        if i == 10:
            user_input = input("Would you like to do another 10? y/n ")
            if user_input == "n":
                sys.exit()
            elif user_input == "y":
                i = 0
            else:
                print("Not a valid response.")

        elif anime in processed_anime:
            # compares anime_list to processed_anime, and if they are the same, script terminates
            if collections.Counter(anime_list) == collections.Counter(processed_anime):
                print("Finished")
                sys.exit()
            else:
                continue

        else:
            # formats anilist.co link
            ani_link = "https://anilist.co/search/anime?search=" + anime

            # opens anilist.co link in browser
            webbrowser.open_new_tab(ani_link)

            processed_anime.append(anime)
            i += 1
            time.sleep(0.25)
