from flask import Flask, redirect

app = Flask(__name__)

redirect_route = 'https://us.forums.blizzard.com/en/wow/t/patch-1136-and-naxxramas-release-dates/702176'

@app.route("/")
def landing_page():
    return redirect(redirect_route)