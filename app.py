from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import json
from scraper import print_headlines


app = FlaskAPI(__name__)

# "https://flask-headlines-api.herokuapp.com/headlines"

message = print_headlines()

# message = [

# "Daily Mirror: UK's coronavirus death toll rises by smallest amount since lockdown began - with 160 more patients killed taking total to 34,796It's the lowest daily rise since March 24 - the day after Boris Johnson ordered Brits to stay home",
# "The Grauniad: London care homes report possible fresh outbreaks",
# "The Times: Anyone aged over 5 with symptoms can have test",
# "The Daily Express: Barnier explodes: EU chief 'never looked so angry' as UK savages 'unreasonable' bloc",
# "The Independent: Raab says UK closer to easing lockdown further but nation told it may have to ‘live with virus for years’",
# "The Financial Times: Germany and France unite in call for €500bn Europe recovery fund",
# "The Telegraph: Coronavirus vaccine in first human trial shows signs of creating immunity",
# "Daily Mail: Britain announces lowest daily coronavirus death total since startof lockdown as health chiefs reveal 160 more victims - taking official death toll to 34,796"
# ]

@app.route("/headlines", methods=['GET'])
def notes_list():
   
    # note = str("hello, world! this is james speaking")
    note = message
    note_json = json.dumps(note)

    return note_json, status.HTTP_201_CREATED

if __name__ == "__main__":
    app.run(debug=True)