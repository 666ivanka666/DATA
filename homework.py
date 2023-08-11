# Write a program that retrieves data from https://catfact.ninja/fact.
# Retrieved is JSON - print value stored under fact key.


import requests

url = "https://catfact.ninja/fact"

try:
    response = requests.get(url)
    response.raise_for_status()  # Provjera statusnog koda odgovora
    
    try:
        data = response.json()
        fact = data.get('fact')
        if fact:
            print("Cat Fact:", fact)
        else:
            print("No cat fact found in the response.")
    except ValueError:
        print("Could not parse JSON response.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)


# Write a program that uses https://api.nationalize.io to predict nationality of a given name.
# In an endless loop, ask user to enter name (or ENTER/ESC to exit) and use the API to retrieve the nationality data.
# Print most probably nationality ID.
# Example request: https://api.nationalize.io/?name=bruce
# Example response:

# {
#   "country":[
#     {
#       "country_id":"NZ",
#       "probability":0.165
#     },
#     {
#       "country_id":"AU",
#       "probability":0.1
#     },
#     {
#       "country_id":"CA",
#       "probability":0.085
#     },
#     {
#       "country_id":"US",
#       "probability":0.078
#     },
#     {
#       "country_id":"CN",
#       "probability":0.065
#     }
#   ],
#   "name":"bruce"
# }
import requests

base_url = "https://api.nationalize.io/?name="

def get_nationality_data(name):
    url = base_url + name
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check the response status code
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the request:", e)
        return None
    except ValueError:
        print("An error occurred while parsing the response as JSON.")
        return None

while True:
    user_input = input("Enter a name (or press ENTER/ESC to exit): ")
    
    if not user_input:
        print("Thank you for using the program.")
        break
    
    if user_input.lower() == "esc":
        print("Thank you for using the program.")
        break
    
    nationality_data = get_nationality_data(user_input)
    
    if nationality_data is not None:
        try:
            countries = nationality_data.get('country', [])
            if countries:
                most_probable = max(countries, key=lambda x: x['probability'])
                print("Most probable nationality ID:", most_probable['country_id'])
            else:
                print("No nationality data found.")
        except KeyError:
            print("Could not find nationality data.")


# Write a program that saves all the data about a particular country to the JSON file country-output.json.
# Read the country name from an input.
# Use https://restcountries.com API to get data about a country.
# When serializing to JSON, use 2 spaces as indentation.

# Example request: https://restcountries.com/v3.1/name/croatia

import requests
import json

base_url = "https://restcountries.com/v3.1/name/"

def get_country_data(country_name):
    url = base_url + country_name
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check the response status code
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the request:", e)
        return None

while True:
    user_input = input("Enter a country name (or press ENTER to exit): ")
    
    if not user_input:
        print("Thank you for using the program.")
        break
    
    country_data = get_country_data(user_input)
    
    if country_data is not None:
        try:
            output_file_name = "country-output.json"
            with open(output_file_name, "w") as output_file:
                json.dump(country_data, output_file, indent=2)
                print(f"Country data saved to {output_file_name}.")
        except Exception as e:
            print("An error occurred while saving data to JSON:", e)



# Write a function that returns all the languages spoken in a particular country.

# Pass the country name in an input parameter to the function.
# Use https://restcountries.com API to get data about a country.

# Example request: https://restcountries.com/v3.1/name/belgium

# JSON response contains list of countries with data - use the first item.
# Data about laguages is stored in languages key of the item.
# Return list of all the languages.

import requests

base_url = "https://restcountries.com/v3.1/name/"

def get_languages_in_country(country_name):
    url = base_url + country_name
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check the response status code
        data = response.json()
        if isinstance(data, list) and data:
            languages = data[0].get('languages', [])
            return languages
        else:
            print("No data found for the country.")
            return []
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the request:", e)
        return []

while True:
    country_name = input("Enter a country name: ")
    
    if not country_name:
        print("Thank you for using the program.")
        break
    
    languages_spoken = get_languages_in_country(country_name)
    
    if languages_spoken:
        try:
            print("Languages spoken in", country_name + ":")
            for language in languages_spoken:
                print(language)
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("No language data available for", country_name)



# Write a function that retrieves beer data from https://api.punkapi.com
# Data is paged and can be retrieved in page-by-page manner.
# Example: https://api.punkapi.com/v2/beers?page=1&per_page=25
# Function accepts page number and should retrieve 10 beer entries per page.
# Print name and tagline data available for each beer entry, like this:
# [Buzz]: A Real Bitter Experience.
# Protect the request using try/except.

import requests

base_url = "https://api.punkapi.com/v2/beers"

def get_beer_data(page_number):
    params = {
        'page': page_number,
        'per_page': 10
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check the response status code
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the request:", e)
        return []

def print_beer_info(beer):
    try:
        name = beer['name']
        tagline = beer['tagline']
        print(f"[{name}]: {tagline}")
    except KeyError:
        print("Invalid beer data")

page_number = int(input("Enter the page number: "))

beer_data = get_beer_data(page_number)

if beer_data:
    for beer in beer_data:
        print_beer_info(beer)
else:
    print("No beer data available for the specified page.")


# Write a program that for a particular user input retrieves the data about TV shows from https://api.tvmaze.com
# Ask input from the user in an endless loop (ENTER/ESC for exit).
# Example URL: https://api.tvmaze.com/search/shows?q=red%20dwarf
# For each of the data entries retrieved, print the show name and the show rating.
import requests

base_url = "https://api.tvmaze.com/search/shows?q="

def get_show_data(query):
    url = base_url + query
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check the response status code
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the request:", e)
        return []

while True:
    user_input = input("Enter a TV show name (or press ENTER/ESC to exit): ")
    
    if not user_input:
        print("Thank you for using the program.")
        break
    
    if user_input.lower() == "esc":
        print("Thank you for using the program.")
        break
    
    show_data = get_show_data(user_input)
    
    if show_data:
        for entry in show_data:
            try:
                show_name = entry['show']['name']
                show_rating = entry['show']['rating']['average']
                print(f"Show: {show_name}, Rating: {show_rating}")
            except KeyError:
                print("Invalid show data")
            except TypeError:
                print("Invalid show data")
    else:
        print("No show data available for the specified query.")

        

# Write a program that reads your favorite TV show names from text file shows.txt and outputs them sorted by show ratings, descending.
# Use TvMaze API endpoint: https://api.tvmaze.com/search/shows?q={show}
# If multiple shows have been retrieved from the endpoint, use only the first one.



# import os
# import requests

# # Function to fetch show data from TVMaze API
# def get_show_data(show_name):
#     url = f"https://api.tvmaze.com/search/shows?q={show_name}"
#     response = requests.get(url, verify=False)
#     data = response.json()
#     if data:
#         return data[0]['show']
#     return None

# # Read show names from shows.txt
# def read_show_names(filename):
#     with open(filename, 'r') as file:
#         return [line.strip() for line in file]

# # Open shows.txt for viewing
# def open_show_names(filename):
#     with open(filename, 'r') as file:
#         content = file.read()
#         print(content)

# # Main function
# def main():
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     shows_file_path = os.path.join(script_dir, 'shows.txt')

#     # Open and display shows.txt
#     open_show_names(shows_file_path)

#     # Read show names from shows.txt
#     show_names = read_show_names(shows_file_path)
#     shows_with_ratings = []

#     for show_name in show_names:
#         show_data = get_show_data(show_name)
#         if show_data:
#             show_name = show_data['name']
#             show_rating = show_data['rating']['average'] if (show_data.get('rating') and show_data['rating'].get('average')) else 0
#             shows_with_ratings.append((show_name, show_rating))

#     # Sort shows by rating in descending order
#     shows_with_ratings.sort(key=lambda x: x[1], reverse=True)

#     # Print sorted shows with ratings
#     for show, rating in shows_with_ratings:
#         print(f"{show}: {rating}")

# if __name__ == "__main__":
#     main()



import os
import requests

# Funkcija za dohvaćanje podataka o emisiji putem TVMaze API-ja
def get_show_data(show_name):
    url = f"https://api.tvmaze.com/search/shows?q={show_name}"
    response = requests.get(url, verify=False)  # Onemogućava SSL verifikaciju
    data = response.json()
    if data:
        return data[0]['show']
    return None

# Funkcija za čitanje imena emisija iz shows.txt
def read_show_names(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Funkcija za otvaranje shows.txt datoteke radi pregleda
def open_show_names(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

# Funkcija za stvaranje shows.txt datoteke s primjerima emisija
def create_shows_file(filename):
    show_names = [
        "Game of Thrones",
        "Stranger Things",
        "Breaking Bad",
        "The Simpsons",
        "Friends"
    ]

    with open(filename, 'w') as file:
        for show_name in show_names:
            file.write(show_name + '\n')

# Glavna funkcija
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    shows_file_path = os.path.join(script_dir, 'shows.txt')

    # Stvori datoteku shows.txt ako ne postoji
    if not os.path.exists(shows_file_path):
        create_shows_file(shows_file_path)

    # Otvori i prikaži sadržaj shows.txt
    open_show_names(shows_file_path)

    # Dohvati imena emisija iz shows.txt
    show_names = read_show_names(shows_file_path)
    shows_with_ratings = []

    for show_name in show_names:
        show_data = get_show_data(show_name)
        if show_data:
            show_name = show_data['name']
            show_rating = show_data['rating']['average'] if (show_data.get('rating') and show_data['rating'].get('average')) else 0
            shows_with_ratings.append((show_name, show_rating))

    # Sortiraj emisije po ocjeni u silaznom redoslijedu
    shows_with_ratings.sort(key=lambda x: x[1], reverse=True)

    # Ispiši sortirane emisije s ocjenama
    for show, rating in shows_with_ratings:
        print(f"{show}: {rating}")

if __name__ == "__main__":
    main()

