from flask import Flask, render_template, jsonify

# from data import sigmoid_price



application = Flask(__name__)


@application.route("/")
def index_page():
    return render_template('index.html')


@application.route("/api/v1/get_data", methods=['POST', "GET"])
def api_post_data():
    with open('file.json', "r", encoding='UTF-8') as file:
        content = file.read()
        return jsonify({'data': content})



if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")