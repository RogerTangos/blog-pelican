AUTHOR = "Albert Carter"
SITENAME = "Albert R Carter"
SITEURL = ""

PATH = "content"
STATIC_PATHS = ["blog/img/", "images"]

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "en"

THEME = "theme"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ('Home', '/'),
    ('About', '/pages/about/'),
    ('Resume', '/pages/resume/'),
    ('Contact', '/pages/contact/')
]

DISPLAY_PAGES_ON_MENU = False
# DISPLAY_CATEGORIES_ON_MENU = False


# Blogroll
LINKS = (
    ("Bank.Green", "https://bank.green.com/"),
    ("Bike Points", "https://bikepoints.org"),
    ("XR Comic Science", "https://xrscience.earth/"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/RogerTangos/"),
    ("LinkedIn", "https://www.linkedin.com/in/albertrcarter/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
