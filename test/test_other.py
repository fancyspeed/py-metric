
def test_static():
  class A():
    @staticmethod
    def a():
      print 'a'

    @staticmethod
    def b():
      print 'b'
      A.a()

  A.a()
  A.b()

def test_plus():
  A = range(0, 100)
  B = range(0, 100)
  i = 0
  for a in A:
    b, i = B[i], i+1
    print b, i
    
def test_object():
  class A(object):
    def __init__(self): pass

  print dir(A)

  class B():
    def __init__(self): pass

  print dir(B)

if __name__ == '__main__':
  test_static()
  test_plus()
  test_object()

