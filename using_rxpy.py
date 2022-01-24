# here we make use of the reactive extensions for python (RxPY)
# may need to pip isntall rx
from itsdangerous import json
import requests # make sure you pip install requests
import rx
import json
from rx import operators as op

# we will be accessing an API end-point at http:/jsonplaceholder.typicode.com/users
# here is a function to filter the returned data by 'starts with...'
def filterNames(x, l):
    if x['name'].startswith(l):
        return x['name'] # we have a match, so return this item
    else:
        return '' # no match

def main():
    # ask the user which letter to match
    letter = input('starts with...?')
    # fetch all the users from the API end-point
    content = requests.get('http://jsonplaceholder.typicode.com/users')
    # convert from JSON to Python structure
    y = json.loads(content.text) # we now have a dict
    # we need an observable
    source = rx.from_(y) # note the trailing underscore
    # make use of this observable
    case1 = source.pipe( # this will async wait for the data to be ready
        op.filter( lambda c:filterNames(c, letter) ),
        op.map( lambda a:a['name'] ) # or 'email' etc.
    )
    # now we subscribe to the observable
    # NB there may be many subscribers
    case1.subscribe(
        # we can implement next, error and complete handlers
        on_next      = lambda i: print('Received {}'.format(i)),
        on_error     = lambda e: print('Received Error {}'.format(e)),
        on_completed = lambda: print('All done')
    )

if __name__ == '__main__':
    main()