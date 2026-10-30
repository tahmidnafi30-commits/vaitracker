from flask import Flask, request

app = Flask(__name__)

# last location save korar jonno
last_location = {"lat": "22.8456", "lon": "89.5403"} # default Khulna

@app.route('/')
def home():
    return f'''
    <h2>Vai Tracker Live</h2>
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
        return "OK"
    return "Missing lat/lon"

if __name__ == '__main__':
    app.run()
