# here we explore coroutines
from asyncio import coroutines

# In Python, generators and coroutines are both constructed using a syntax that looks
# like we are constructing a function. But the resulting object is not a function at all; it's
# a totally different kind of object. Functions are, of course, also objects. But they have
# a different interface; functions are callable and return values, generators have data
# pulled out using next(), and coroutines have data pushed in using send.

# we can write a custom coroutine
def tally():
    score = 0
    while True:
        increment = yield score # here we both return a value (score) AND set a value (increment)
        score += increment

# The order in which things happens:
#  yield occurs and the generator pauses
#  send() occurs from outside the function and the generator wakes up
#  The value sent in is assigned to the left side of the yield statement
#  The generator continues processing until it encounters another yield statement

if __name__ == '__main__':
    w = tally()
    b = tally()

    print(type(tally)) # the coroutine returns a generator object

    print(next(w)) # 0
    print(next(b))

    print(w.send(3)) # 3
    print(w.send(3)) # 6
    print(b.send(9)) # 9

    # tidy up
    w.close()
    b.close()