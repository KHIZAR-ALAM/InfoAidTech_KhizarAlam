import requests
import json


API_KEY = '446d55904975607133081c923788bf6b'

def fetch_weather_data(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        print('City not found. Please check the spelling.')
        return None
    else:
        print('Error has occured while fetching data fetching weather data')
        return None

def display_weather_data(weather_data):
    if weather_data:
        print(f'Location: {weather_data["name"]}, {weather_data["sys"]["country"]}')
        print(f'Temperature: {weather_data["main"]["temp"]}°C')
        print(f'Weather: {weather_data["weather"][0]["description"]}')
        print(f'Humidity: {weather_data["main"]["humidity"]}%')
        print(f'Pressure: {weather_data["main"]["pressure"]} hPa')
    else:
        print('NO WEATHER DATA TO DISPLAY1')

def main():
    favorite_locations = {}
    
    while True:
        print('\nWEATHER APP MENU:')
        print('1. Fetch Weather Data')
        print('2. Display Weather Data')
        print('3. Exit')
        
        choice = input('ENTER YOU CHOICE: ')
        
        if choice == '1':
            city_name = input('Enter city name: ').lower()
            weather_data = fetch_weather_data(city_name)
            if weather_data:
                favorite_locations[city_name] = weather_data
                print('Weather data fetched successfully.')
        elif choice == '2':
            city_name = input('Enter city name: ').lower()
            if city_name in favorite_locations:
                display_weather_data(favorite_locations[city_name])
            else:
                print('CITY IS NOT FOUND IN FAVORITES.')
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')


main()
