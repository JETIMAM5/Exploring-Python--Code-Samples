import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
whole_page = response.text
soup = BeautifulSoup(whole_page, "html.parser")
movies = [movie.getText() for movie in soup.find_all("h3", class_="title")]

with open("movies.txt", "w", encoding="utf-8") as movies_file:
    for movie in movies[::-1]:
        movies_file.write(movie + "\n")



