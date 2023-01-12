import unittest
def keyv(dict,key):
    for key in dict.keys():
        return key
def mylist(l):
    for i in l:
        l.sort(reverse=True)
    return l
def mymin(l):
    mini=l[0]
    for i in l[0]:
        if i<mini:
            mini=i
class my_Test(unittest.TestCase):
    def test(self):
        dict={"madhu":80,"choci":90}
        key="madhu"
        r=keyv(dict,key)
        self.assertEqual(r,"madhu")
    def test1(self):
        l=[89,23,44,90]
        r=mylist(l)
        self.assertEqual(r,[90,89,44,23])
    def test2(self):
        l=[76,23,34,56]
        r=mymin(l)
        self.assertEqual(r,23)
