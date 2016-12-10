from fractions import gcd
import requests
import json
import random


def attack(mod,s):
    t = random.randint(1, mod)
    y = format(t * t % mod, '02X')
    url = "http://asymcryptwebservice.appspot.com/znp/challenge?y=" + str(y)
    response = s.get(url)
    print "Show y: " + y
    z = int(json.loads(response.content)['root'], 16)
    print "Received z: " + format(z, '02X')
    dev = gcd(t + z, mod)
    if t != z and mod % dev == 0 and dev != 1:
        print "yeah mod dividers is "
        print dev
        print format(mod / dev, '02X')
    else:
        attack(mod,s)


if __name__ == '__main__':
    url = "http://asymcryptwebservice.appspot.com/znp/serverKey"
    s = requests.session()
    response = s.get(url)
    mod = int(json.loads(response.content)['modulus'], 16)
    print "KEY:" + format(mod, '02X')
    attack(mod,s)
