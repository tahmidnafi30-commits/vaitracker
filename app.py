from flask import Flask, request, jsonify
app = Flask(__name__)
latest_location = {"lat": 23.8103, "lon": 90.4125}

@app.route('/update')
def update():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat and lon:
        latest_location["lat"] = lat
        latest_location["lon"] = lon
    return "OK"

@app.route('/')
def home():
    return f'<h1>Vai Tracker Live</h1><p>Lat: {latest_location["lat"]} Lon: {latest_location["lon"]}</p><a href="https://www.google.com/maps?q={latest_location["lat"]},{latest_location["lon"]}" target="_blank">Open Map</a><script>setTimeout(()=>{{location.reload()}},5000)</script>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
