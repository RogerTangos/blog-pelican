To compile static content and then serve it:
```
pelican -r -l
pelican content; pelican --listen
```

pelican content -s publishconf.py; cp -r output/* docs/; git add docs; gcm "update publishconfig"; gp