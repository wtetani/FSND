from ..extensions import db
from sqlalchemy.orm import relationship


class Artist(db.Model):
  __tablename__ = 'Artist'
  artist_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  city = db.Column(db.String(120), nullable=False)
  state = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(120), nullable=False)
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  artist_website = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, default=False)
  talent_description = db.Column(db.String(120))
  Venue = relationship('Show', back_populates='Artist')

  def __repr__(self):
    return f'<Artist Name: {self.name}>, Phone: {self.phone}, City: {self.city}, State: {self.state}'