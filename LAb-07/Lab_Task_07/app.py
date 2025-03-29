from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "49540f912a974a3ea35202115251803"  
BASE_URL = "http://api.weatherapi.com/v1/current.json"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']  #
        complete_url = f"{BASE_URL}?key={API_KEY}&q={city}"

        # Fetch weather data from the WeatherAPI
        response = requests.get(complete_url)
        data = response.json()

        # Check if the city is valid
        if "error" in data:
            return render_template('index.html', error="City not found!")
        
        # Extract necessary data
        city_name = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]

        return render_template('index.html', city=city_name, country=country,
                               temperature=temperature, condition=condition,
                               humidity=humidity, wind_speed=wind_speed)
    
    return render_template('index.html', error="")

if __name__ == '__main__':
    app.run(debug=True)
