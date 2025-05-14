from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AC_Model(db.Model):
  __tablename__ = 'access_counter_dev'

  id = db.Column(db.Integer, primary_key=True)
  count = db.Column(db.Integer, nullable=False, default=0)
