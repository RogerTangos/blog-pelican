# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://rogertangos.github.io/blog-pelican"
RELATIVE_URLS = False  # Ensure absolute URLs for production

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = "docs/"

MENUITEMS = [
    ("Home", f"{SITEURL}/"),
    ("About", f"{SITEURL}/pages/about/"),
    ("Resume", f"{SITEURL}/pages/resume/"),
    ("Contact", f"{SITEURL}/pages/contact/"),
]

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
