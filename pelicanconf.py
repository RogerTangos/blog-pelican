AUTHOR = "Albert R Carter"
SITENAME = "Albert R Carter"
SITEURL = "localhost:8000"
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = "docs/"


PATH = "content"
STATIC_PATHS = ["blog/img/", "images", "theme/static", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}
PAGE_SAVE_AS = "pages/{slug}/index.html"
PAGE_URL = "pages/{slug}/"


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
    ("Home", f"{SITEURL}/"),
    ("About", f"{SITEURL}/pages/about/"),
    ("Resume", f"{SITEURL}/pages/resume/"),
    ("Contact", f"{SITEURL}/pages/contact/"),
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
