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
current_jarvis_cmd = {"cmd": ""}

@app.route('/jarvis')
def jarvis_page():
    return """<h1 style="text-align:center">JARVIS PHONE</h1><button id="b" style="display:block;margin:50px auto;padding:40px;border-radius:50%">TAP & SPEAK</button><p id="t" style="text-align:center"></p><script>const b=document.getElementById('b'),t=document.getElementById('t');const R=new(window.SpeechRecognition||window.webkitSpeechRecognition)();R.lang='en-US';b.onclick=()=>{R.start();t.innerText='Listening...'};R.onresult=(e)=>{let c=e.results[0][0].transcript;t.innerText=c;fetch('/send-command?cmd='+encodeURIComponent(c))}</script>"""

@app.route('/send-command')
def send_cmd():
    current_jarvis_cmd["cmd"]=request.args.get("cmd","")
    return "OK"

@app.route('/get-command')
def get_cmd():
    return current_jarvis_cmd
