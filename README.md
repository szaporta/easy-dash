# easy-dash
This tool will easily allow you to copy a Dashboard (Screen OR Time!) with an easy command

You'll need (from each account):

1. Source account:
   1. API key
   1. APP key

2. Destination account:
   1. API key
   1. APP key

3. Dashboard ID of the dash you wish to copy

## Executing script
You can look at the help docs:
```
$ python easy_dash.py -h
usage: easy_dash.py [-h] [--srcapikey SRCAPIKEY] [--srcappkey SRCAPPKEY]
                    [--dstapikey DSTAPIKEY] [--dstappkey DSTAPPKEY]
                    [--dash DASH]

optional arguments:
  -h, --help            show this help message and exit
  --srcapikey SRCAPIKEY
                        Enter the source API key
  --srcappkey SRCAPPKEY
                        Enter the source APP key
  --dstapikey DSTAPIKEY
                        Enter the destination API key
  --dstappkey DSTAPPKEY
                        Enter the destination APP key
  --dash DASH           ID of the dashboard you want to clone ex: 442-3kr-k68
```

To copy a dashboard from your source account to the destination account:
```
$ python easy_dash.py --dash <DASHBOARD_ID> --srcapikey <API_KEY> --srcappkey <APP_KEY --dstapikey <API_KEY_2> --dstappkey <APP_KEY_2>
```
