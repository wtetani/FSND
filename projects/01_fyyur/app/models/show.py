from ..extensions import db
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class Show(db.Model):
  __tablename__ = 'show'  
  venue_id = db.Column(ForeignKey('venue.venue_id'), primary_key=True)
  artist_id = db.Column(ForeignKey('artist.artist_id'), primary_key=True)
  start_time = db.Column(db.DateTime(timezone=True), nullable=False)
  end_time = db.Column(db.DateTime(timezone=True), nullable=False)
  artists = relationship('Artist', back_populates='venues')
  venues = relationship('Venue', back_populates='artists')

  def __repr__(self):
    return f'<Show Venue: {self.Venue}, Artist: {self.Artist}, Start-time: {self.start_time}, End-time:{self.end_time}>'