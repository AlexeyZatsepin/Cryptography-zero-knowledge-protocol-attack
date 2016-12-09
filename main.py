from fractions import gcd
from mechanize import Browser
import json
import random


def attack(mod):
    browser.open("http://asymcryptwebservice.appspot.com/?section=znp")
    browser.form = list(browser.forms())[2]
    t = random.randint(1, mod)
    y = format(t * t % mod, '02X')
    browser["y"] = y
    print "Show y: " + y
    response = browser.submit()
    t = random.randint(1, mod)
    z = int(json.loads(response.read())['root'], 16)
    print "Received z: " + format(z, '02X')
    if t != z:
        dev = gcd(t + z, mod)
        if mod % dev == 0:
            print "yeah mod dividers is "
            print dev
            print format(mod / dev, '02X')
        else:
            attack(mod)


if __name__ == '__main__':
    print "Connecting to test server"
    browser = Browser()
    browser.set_handle_robots(False)
    browser.open("http://asymcryptwebservice.appspot.com/?section=znp")
    browser.form = list(browser.forms())[0]
    print "Get key :"
    response = browser.submit()
    mod = int(json.loads(response.read())['modulus'], 16)
    print "KEY:" + format(mod, '02X')
    attack(mod)
