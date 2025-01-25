To compile static content and then serve it:
```
pelican -r -l
pelican content; pelican --listen
```

pelican content -s publishconf.py; git add docs; gcm "publish"; gp

to build for remote:

```
make publish; git add .; git commit -m "publish"; gp
```