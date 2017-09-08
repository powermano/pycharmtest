def gen():
    value = 0
    while True:
        receive = yield value #可以通过send传值进来，赋值给receive 但是每个next()只会执行yield value  并没有赋值给receive
        if receive == 'e':
            break
        value = 'got: %s' % receive


g=gen()
print(g.send(None))
print(g.send('aaa'))
print(g.send(3))
# print(g.send('e'))

#result
# 0
# got: aaa
# got: 3
# Traceback (most recent call last):
# File "h.py", line 14, in <module>
#   print(g.send('e'))
# StopIteration

class strtest:
    def __init__(self):
        self.val = 1

    def __str__(self):
        return str(self.val)


if __name__ == "__main__":
    st = strtest()
    print(st.__str__())
    print(str(st))