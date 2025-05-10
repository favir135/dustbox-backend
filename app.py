from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, World!'


db = SQLAlchemy()


class AccessCounter(db.Model):
  __tablename__ = 'access_counter'

  id = db.Column(db.Integer, primary_key=True)
  count = db.Column(db.Integer, nullable=False, default=0)


load_dotenv()

app = Flask(__name__)

# SQLAlchemy用のDB URI設定
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/count", methods=["GET"])
def count():
  counter = AccessCounter.query.get(1)

  if counter is None:
    counter = AccessCounter(id=1, count=1)  # type: ignore
    db.session.add(counter)
  else:
    counter.count += 1

  db.session.commit()
  return jsonify({"count": counter.count})


if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)
