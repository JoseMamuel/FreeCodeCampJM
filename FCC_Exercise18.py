import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl 

print("* Calling Twitter... ")
url = augment("https://api.twitter.com/1.1/statuses/user_timeline.json", 
              {"screen_name":"drchuck", "count" : "2"})

print(url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print("")
    acct = input("Enter Twitter Account : ")
    if (len(acct) < 1):
        break
    url = twurl.augment(TWITTER_URL,
                        {"screen_name":acct, "count" : "5"})
    print("Retrieving", url)
    conection = urllib.request.urlopen(url, context=ctx)
    data = conection.read().decode()
    headers = dict(conection.getheaders())
    print("Remaining", headers["x-rate-limit-remaining"])
    js = json.loads(data)
    print(json.dumps(js, ident=2))

    for u in js["users"]:
        print(u["screen_name"]
        if "status" not in u:
            print("No Found")
            continue
        s = u["status"],["text"])
        print("", s[:50])


conection = urllib.request.urlopen(url, context=ctx)
data = conection.read()
print(data)
