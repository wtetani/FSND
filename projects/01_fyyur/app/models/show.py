from ..extensions import db
from sqlalchemy.orm import relationship


class Show(db.Model):
  __tablename__ = 'Musical Show'  
  venue_id = db.Column(db.Integer, db.ForeignKey('venue_id'), nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist_id'), nullable=False)
  start_time = db.Column(db.DateTime(timezone=True), nullable=False)
  end_time = db.Column(db.DateTime(timezone=True), nullable=False)
  Artist = relationship('Artist', back_populates='Venue')
  Venue = relationship('Venue', back_populates='Artist')

  def __repr__(self):
    return f'<Show Venue: {self.Venue}, Artist: {self.Artist}, Start-time: {self.start_time}, End-time:{self.end_time}>'