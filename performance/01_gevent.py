# recent Pythons have a green event called gevent
# this can run new threads on our behalf
import gevent
from gevent import socket
# use a list of host URLs to retreive data in a thread-safe way
hosts = ['www.ericsson.com', 'www.neueda.com', 'www.crappytaxidermy.com', 'jsonplaceholder.typicode.com', 'bbc.co.uk']
jobs  = [ gevent.spawn(socket.gethostbyname, host) for host in hosts ]

# start all the threads then join them all
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)