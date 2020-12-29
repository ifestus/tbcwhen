from flask import Flask, redirect

app = Flask(__name__)

# redirect_route = 'https://us.forums.blizzard.com/en/wow/t/patch-1136-and-naxxramas-release-dates/702176'
redirect_route = 'https://www.warcrafttavern.com/tbc/news/leak-tbc-classic-beta-in-feb-release-in-may/'

@app.route("/")
def landing_page():
    return redirect(redirect_route)