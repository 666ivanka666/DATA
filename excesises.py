# Use get() function of requests module to retrieve HTML data located on URL https://www.google.com. Print first 80 characters of the response text.

# HINT: Use get() function of requests module to retrieve HTML code from the server behing the given address.
# Example: response = requests.get('https://www.google.com/')

# When request finishes, get() function will return the response object with text property where the response HTML can be read from.
# Example: response.text

# HTTP METODE:
# GET -> dohvat
# PUT -> ažuriranje, update
# DELETE -> brisanje
# POST -> kreiranje

# MOST COMMON RESPONSE STATUS CODE:
# 200 - OK
# 400 - Bad request
# 401 - Unauthorized
# 403 - forbbiden
# 500 - internal server error

import requests

response = requests.get('https://www.google.com')

print(response.text[0:80])

# Improve the Example 1 in a way that you check for the status_code of the response.
# The response should return status code 200 if succesful. Try modifying URL in order for the request to fail.

# Also, improve the example to print headers dictionary of the response, header by header in a loop. 
# There is also reason member with the readable status text that corresponds to status code.

import requests

try:
  response = requests.get('https://www.google.com')

  status_code = response.status_code
  headers = response.headers
  text = response.text

  if status_code == 200:
    print('successful')

  for key in headers:
    print(f"{key} = {headers[key]}")

  # print(text) # Objascniti scope varijabli
except Exception as e:
  print('PUKNUO TI JE URL, ZATO STO JE KRIVI URL')

print("Continue")


# Improve the last example to handle errors using a common error handling technique - try/except.

# HINT: to use try/except, make sure that when the request is executed you call response.raise_for_status() method. 
# If there is a problem (error codes 4xx and 5xx), this method will raise an exception and your try/except block will be able to handle errors.
# Specifically, if HTTP request fails, HTTPError will be raised.

import requests
from requests.models import HTTPError

try:
  response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=45.79&longitude=15.96&current_weather=true&hourly=relativehumidity_2m')
  # response = requests.get('https://weatherdbi.herokuapp.com/data/weather/Zagreb')
  response.raise_for_status()

  print(response.text)

except HTTPError as http_error:
  print(http_error)
except Exception as e:
  print('PUKNUO TI JE URL, ZATO STO JE KRIVI URL')



# Create the program that uses restcountries API to retrieve data about the specific country.

# Base service URL: https://restcountries.com/v3.1/name/
# Example country URL: https://restcountries.com/v3.1/name/croatia
# Response: list of matching countries (e.g. https://restcountries.com/v3.1/name/hr matches multiple countries)

# User can input a country name, part of country name or just ENTER to exit.
# Data about matching countries will be retrieved - just print first 200 characters of it.



import requests

base_url = "https://restcountries.com/v3.1/name/"

def get_country_data(country_name):
    url = base_url + country_name
    try:
        response = requests.get(url)
        response.raise_for_status()  # Provjera statusnog koda odgovora
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the request:", e)
        return None

while True:
    user_input = input("Unesite ime države (ili pritisnite ENTER za izlaz): ")
    
    if not user_input:
        print("Hvala što ste koristili program.")
        break
    
    country_data = get_country_data(user_input)
    
    if country_data is not None:
        try:
            print("Podaci o prvoj državi:")
            print(country_data[0])
        except (IndexError, KeyError):
            print("Nema dostupnih podataka o državi.")




# Improve the last example in order to treat the response as JSON, parse that JSON and print some data that is part of that JSON structure.
# HINT: To parse the response as JSON, call response.json() method.

# Returned JSON data is a list of matching country data. Each item of the list holds one country data, and it is a dictionary, 
# which means that JSON response is a list of dictionaries.

# Example:
#   data = response.json()

#   for state in data:
#     # print state data

# In each dictionary entry there is part of the country data (e.g. key capital is for country capital).
# Show data for keys cca3 and capital.
# Example: state['cca3'].

# Also, data for key name is itself a dictionary - show data under common key of that dictionary.
# Example: state['name']['common'].

import requests

base_url = "https://restcountries.com/v3.1/name/"

def get_country_data(country_name):
    url = base_url + country_name
    try:
        response = requests.get(url)
        response.raise_for_status()  # Provjera statusnog koda odgovora
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Došlo je do greške prilikom slanja zahtjeva:", e)
        return None

while True:
    user_input = input("Unesite ime države (ili pritisnite ENTER za izlaz): ")
    
    if not user_input:
        print("Hvala na korištenju programa.")
        break
    
    country_data = get_country_data(user_input)
    
    if country_data is not None:
        for country in country_data:
            try:
                cca3 = country['cca3']
                print("Kod države (cca3):", cca3)
            except KeyError:
                print("Nema podataka o kodu države.")
            
            try:
                capital = country['capital'][0]
                print("Glavni grad:", capital)
            except KeyError:
                print("Nema podataka o glavnom gradu.")
            
            try:
                common_name = country['translations']['zho']['common']
                print("zho ime:", common_name)
            except KeyError:
                print("Nema podataka o zho imenu.")
            
            print("---------------------")
