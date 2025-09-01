from ..extensions import db
from sqlalchemy.orm import relationship

class Venue(db.Model):
  __tablename__ = 'venue'
  venue_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  city = db.Column(db.String(120), nullable=False)
  state = db.Column(db.String(120), nullable=False) 
  address = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(120), nullable=False)
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))

  # TODO: implement any missing fields, as a database migration using Flask-Migrate
  venue_website = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, default=False)
  talent_description = db.Column(db.String(120))
  artists = relationship('Show', back_populates='venues')

  def __repr__(self):
    return f'<Venue: {self.name}, Phone: {self.phone}, City: {self.city}, State: {self.state}>'