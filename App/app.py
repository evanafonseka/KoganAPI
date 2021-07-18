from flask import Flask, jsonify
from flask_cors import cross_origin
from main import driver_function, get_urls

app = Flask(__name__)


@app.route("/")
@cross_origin()
def index():
    return get_average_cubic_weight_for("Air Conditioners")


def get_average_cubic_weight_for(category):
    urls = get_urls()
    response = driver_function(urls, category)
    return jsonify({
        f"{category}": f"{response}kg"
    })


@app.route("/<category>")
@cross_origin()
def give_em_the_rest(category):
    return get_average_cubic_weight_for(category)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
