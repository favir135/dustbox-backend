from flask import Flask, jsonify

from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

from model import db, AC_Model
load_dotenv()

app = Flask(__name__)

CORS(app, origins=["https://favir135.github.io"])


@app.route('/')
def hello_world():
  return 'Hello, World!'


load_dotenv()

# SQLAlchemy用のDB URI設定
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://postgres.{os.getenv('POOLER_TOKEN')}:{os.getenv('DB_PASSWORD')}"
    f"@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/count", methods=["GET"])
def count():
  counter = AC_Model.query.get(1)

  if counter is None:
    counter = AC_Model(id=1, count=1)  # type: ignore
    db.session.add(counter)
  else:
    counter.count += 1

  db.session.commit()
  return jsonify({"count": counter.count})


if __name__ == "__main__":
  app.run(debug=True)
