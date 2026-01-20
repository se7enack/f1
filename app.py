from flask import Flask, render_template
from f1_schedule import get_f1_schedule #nate, this is the local file in this dir (f1_schedule.py)
app = Flask(__name__)

@app.route("/")
def schedule():
    races = get_f1_schedule(2026)
    return render_template("schedule.html", races=races)

if __name__ == "__main__":
    app.run(debug=True)
