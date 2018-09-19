from flask import Flask, render_template
import pymongo
import scrape_mars
from bson.json_util import dumps

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
client = pymongo.MongoClient('localhost', 27017)
db = client.mars_db
collection = db.mars_data

@app.route("/")
def home():
    mars = collection.find_one()
    return  render_template('index.html', mars_dict=mars)

@app.route("/scrape")
def scrape():
    db.collection.remove({})
    mars = scrape_mars.scrape()
    db.collection.insert_one(mars)
    return  render_template('index.html', mars_dict=mars)

if __name__ == "__main__":
    app.run(debug=True)