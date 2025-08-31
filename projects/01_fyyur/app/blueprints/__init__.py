# Import all route blueprints
from .show import show_bp
from .artist import artist_bp
from .venue import venue_bp


# Create a list of blueprints to register in the app
blueprints = [show_bp,artist_bp,venue_bp]