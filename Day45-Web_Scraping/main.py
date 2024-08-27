# Create a .txt file with the top 100 movies
# starting from number 1
# based on Empire Website

from bs4 import BeautifulSoup
import requests

# Website to Scrape
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
movie_webpage = response.text

# Create Soup
soup = BeautifulSoup(movie_webpage, "html.parser")

# Movie titles are h3s, class = "title"
movies = soup.find_all(name="h3", class_="title")

# Split by the existing number structure. ie 1)
# Not all movie titles are in the same format. Movie number 12 is formatted 12:
movies = [movie.getText() for movie in movies]

# Use splice operator to reverse the order of the list
final_movie_list = movies[::-1]

# Write the newly ordered Movie List to a .txt file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    file.write("The 100 Greatest Movies According to Empire Online\n\n")
    for movie in final_movie_list:
        file.write(f"{movie}\n")



