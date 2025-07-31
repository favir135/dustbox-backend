from flask import Flask, jsonify

from flask import Flask
from flask_cors import CORS
import os


from model import session_class, AC_Model

app = Flask(__name__)
CORS(app, origins=["https://favir135.github.io"])


@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route("/count", methods=["GET"])
def count():
  session = session_class()
  counter = session.query(AC_Model).get(1)

  if counter is None:
    counter = AC_Model(id=1, count=1)  # type: ignore
    session.add(counter)
  else:
    counter.count += 1

  session.commit()
  count = counter.count
  session.close()
  return jsonify({"count": count})


if __name__ == "__main__":
  app.run(debug=True)
