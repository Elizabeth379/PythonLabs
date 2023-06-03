def func(a):
    return a + 1


def my_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper


class One:

    value = 19

    def test1(self):
        return self.value + 1

    @staticmethod
    def static_test1():
        return One.value


class Two:

      number = 4

      def test2(self):
          return self.number/2


class Three(Two, One):
    pass