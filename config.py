"""Falsk Config"""

"""
ASSETS_DEBUG: We're bound to screw up a style or JS function
every now and then, which sometimes doesn't become obvious until
we build our bundles and try to use our app. If we set this variable
to True, Flask-Assets won't bundle our static files while we're
running Flask in debug mode.
This is useful for troubleshooting styles or JavaScript gone wrong.
"""
ASSETS_DEBUG = False

"""
ASSETS_AUTO_BUILD: A flag to tell Flask to build our bundles of assets
when Flask starts up automatically. We generally want to set this to
be True, unless you'd prefer only to build assets with some external
force (AKA: you're annoying).
"""
ASSETS_AUTO_BUILD = True