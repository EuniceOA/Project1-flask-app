from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():
    name = "Eunice Olajumoke"

    local_time = datetime.now(
        pytz.timezone("America/Vancouver")
    ).strftime("%Y-%m-%d %H:%M:%S")

    favorite_movies = [
        "The Pursuit of Happiness",
        "Hidden Figures",
        "King of boys",
        "Saworoide'"
    ]

    return f"""
    <h1>{name}</h1>
    <p><strong>Local Time:</strong> {local_time}</p>
    <h3>Favorite Movies:</h3>
    <ul>
        {''.join(f'<li>{movie}</li>' for movie in favorite_movies)}
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
