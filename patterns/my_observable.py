# the Observer pattern is very fashinable currently
# we create an observable then subscribe to it for notifications
class NewsPublisher(): # this is our observable
    def __init__(self):
        self.__subscribers = [] # an empty list - no subscribers to begin with
        self.__latestNews = None
    def attach(self, new_sub):
        self.__subscribers.append(new_sub)
    def detach(self):
        self.__subscribers.pop() # remove the most recent subscriber
    def subscribers(self):
        # iterate over a;; current subscribers
        return [type(x).__name__ for x in self.__subscribers]
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()
    def addNews(self, news):
        self.__latestNews = news
    def getNews(self):
        return 'News: {}'.format(self.__latestNews)

# declare some subscribers to our observable
class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print( type(self).__name__, self.publisher.getNews() )
class PrintSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print( type(self).__name__, self.publisher.getNews() )
class MediaSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print( type(self).__name__, self.publisher.getNews() )

if __name__ == '__main__':
    news_publisher = NewsPublisher()
    # iterate over each subscriber, notifying of the news
    for Subscriber in [MediaSubscriber, PrintSubscriber, EmailSubscriber]:
        Subscriber(news_publisher) # we have three subscribers to our news observable
        news_publisher.addNews('something newsworthy just happened')
    news_publisher.notifySubscribers() # they all get notified
