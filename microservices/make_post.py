import requests # this can make get, post, put etc. requests

# to make a POST request we pass the data as a payload
# NB no data appears on the URL

def makePost():
    url = 'http://httpbin.org/post' # this is a convenient demo server
    payload = {'item':'bottle', 'price':'123'} # a dict
    try:
        r = requests.post(url, data=payload)
        print(r.text) # we can explore the response
    except Exception as err:
        print(err)

if __name__ == '__main__':
    makePost()