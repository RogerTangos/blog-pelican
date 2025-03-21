To compile static content and then serve it:
```
pelican -r -l
pelican content; pelican --listen
```


to build for remote:

```
pelican content -s publishconf.py; git add docs; gcm "update page"; gp
```


Note: Sometimes the repo deletes the docs/CNAME file. 

DO NOT USE `make publish`, since it seems to not properly incorporate SITEURL when generating menu pages.