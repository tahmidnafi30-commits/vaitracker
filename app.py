import os
from flask import Flask, request

app = Flask(__name__)

last_location = {"lat": "22.8456", "lon": "89.5403"}
current_jarvis_cmd = {"cmd": ""}

@app.route('/')
def home():
    return f'''
    <h2>Vai Tracker - LIVE</h2>
    Lat: {last_location["lat"]}<br>
    Lon: {last_location["lon"]}<br>
    <a href="https://www.google.com/maps?q={last_location["lat"]},{last_location["lon"]}" target="_blank">View on Google Maps</a>
    <br><br>
    <a href="/jarvis" style="background:cyan;padding:10px;text-decoration:none;color:black;font-weight:bold">OPEN JARVIS PHONE</a>
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

@app.route('/jarvis')
def jarvis_page():
    return """
    <html><body style="background:black;color:white;text-align:center;padding-top:60px">
    <h1 style="color:cyan">JARVIS PHONE</h1>
    <button id="b" style="padding:30px 60px;border-radius:50%;background:cyan;font-size:22px;font-weight:bold">TAP & SPEAK</button>
    <p id="t" style="color:yellow;margin-top:20px"></p>
    <script>
    const b=document.getElementById('b'),t=document.getElementById('t');
    const R=new(window.SpeechRecognition||window.webkitSpeechRecognition)();
    R.lang='en-US';
    b.onclick=()=>{R.start();t.innerText='Listening...';b.style.background='red'};
    R.onresult=(e)=>{let c=e.results[0][0].transcript;t.innerText='You said: '+c;b.style.background='cyan';fetch('/send-command?cmd='+encodeURIComponent(c))}
    </script>
    </body></html>
    """

@app.route('/send-command')
def send_cmd():
    current_jarvis_cmd["cmd"] = request.args.get("cmd","")
    return "OK"

@app.route('/get-command')
def get_cmd():
    return current_jarvis_cmd

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
