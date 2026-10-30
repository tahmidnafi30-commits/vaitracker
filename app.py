import os
from flask import Flask, request

app = Flask(__name__)

last_location = {"lat": "22.8456", "lon": "89.5403"}

@app.route('/')
def home():
    return f'''
    <h2>Vai Tracker - LIVE</h2>
    Lat: {last_location["lat"]}<br>
    Lon: {last_location["lon"]}<br>
    <a href="https://www.google.com/maps?q={last_location["lat"]},{last_location["lon"]}" target="_blank">View on Google Maps</a>
    '''

@app.route('/track')
def track():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat and lon:
        last_location["lat"] = lat
        last_location["lon"] = lon
        print(f"New location: {lat}, {lon}")
        return "OK"
    return "Missing lat/lon"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
