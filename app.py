# pylint: disable = import-error, invalid-envvar-default, unused-import
""" File to run heroku app """

import random
import os
import flask # type: ignore

from data import get_data, get_wiki_link

app = flask.Flask(__name__)

#Hard coded favorite movies list:
    #Tarzan and Jane: Phil Collins is a beast
    #Pokemon: Mewtwo Strikes back: The scene where Pikachu and all the other pokemon cry (⋟﹏⋞)
    #Doctor Strange: I watched it atleast 6 times
fav_movie_ids = [10228, 566525, 284052]


@app.route("/")
def index():
    """ function to render index.html """
    title, tagline, genres, img_url= get_data(random.choice(fav_movie_ids))
    wiki_url = get_wiki_link(title)
    return flask.render_template("index.html", title=title, tagline=tagline,
    genres=genres, img_url=img_url, wiki_url=wiki_url, num_genres=len(genres))

app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8080)),
    debug=True
)