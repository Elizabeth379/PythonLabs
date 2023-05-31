import unittest
from serializer_factory import SerializerFactory
from data_for_tests import func, my_decorator, Three, One


class JsonTests(unittest.TestCase):

    def setUp(self) -> None:
        self.serializer = SerializerFactory.serializer("JSON")

    def test1(self):
        ser = self.serializer.dumps(19)
        des = self.serializer.loads(ser)

        self.assertEquals(des, 19)

    def test2(self):
        ser = self.serializer.dumps(19.5)
        des = self.serializer.loads(ser)

        self.assertEquals(des, 19.5)

    def test3(self):
        boolean = True

        ser = self.serializer.dumps(boolean)
        des = self.serializer.loads(ser)

        self.assertEquals(des, boolean)

    def test4(self):
        string = "hello"

        ser = self.serializer.dumps(string)
        des = self.serializer.loads(ser)

        self.assertEquals(des, string)

    def test5(self):
        l = ["1", "2", "3", "4"]

        ser = self.serializer.dumps(l)
        des = self.serializer.loads(ser)

        self.assertEquals(des, l)

    def test6(self):
        d = {"1": "masha", "2": "dasha", "3": "sasha", "4": "pasha"}

        ser = self.serializer.dumps(d)
        des = self.serializer.loads(ser)

        self.assertEquals(des, d)

    def test7(self):
        st = {1, "masha", 2, "dasha", 3, 4, 6}

        ser = self.serializer.dumps(st)
        des = self.serializer.loads(ser)

        self.assertEquals(des, st)

    def test8(self):

        ser = self.serializer.dumps(func)
        des = self.serializer.loads(ser)

        self.assertEquals(des(19), func(19))

    def test9(self):
        func_l = lambda x: x % 2 == 0

        ser = self.serializer.dumps(func_l)
        des = self.serializer.loads(ser)

        self.assertEquals(des(19), func_l(19))

    def test10(self):
        func_dec = my_decorator(func)

        ser = self.serializer.dumps(my_decorator)
        des = self.serializer.loads(ser)

        func_des = des(func)

        self.assertEquals(func_des(19), func_dec(19))

    def test11(self):
        cls = Three()

        ser = self.serializer.dumps(cls)
        des = self.serializer.loads(ser)

        self.assertEquals(des.test1(), cls.test1())

    def test12(self):
        static_method = One()

        ser = self.serializer.dumps(static_method)
        des = self.serializer.loads(ser)

        self.assertEquals(des.static_test1(), static_method.static_test1())


class XMLTests(unittest.TestCase):

    def setUp(self) -> None:
        self.serializer = SerializerFactory.serializer("XML")

    def test1(self):
        ser = self.serializer.dumps(19)
        des = self.serializer.loads(ser)

        self.assertEquals(des, 19)

    def test2(self):
        ser = self.serializer.dumps(19.5)
        des = self.serializer.loads(ser)

        self.assertEquals(des, 19.5)

    def test3(self):
        boolean = True

        ser = self.serializer.dumps(boolean)
        des = self.serializer.loads(ser)

        self.assertEquals(des, boolean)

    def test4(self):
        string = "hello"

        ser = self.serializer.dumps(string)
        des = self.serializer.loads(ser)

        self.assertEquals(des, string)

    def test5(self):
        l = ["1", "2", "3", "4"]

        ser = self.serializer.dumps(l)
        des = self.serializer.loads(ser)

        self.assertEquals(des, l)

    def test6(self):
        d = {"1": "masha", "2": "dasha", "3": "sasha", "4": "pasha"}

        ser = self.serializer.dumps(d)
        des = self.serializer.loads(ser)

        self.assertEquals(des, d)

    def test7(self):
        st = {1, "masha", 2, "dasha", 3, 4, 6}

        ser = self.serializer.dumps(st)
        des = self.serializer.loads(ser)

        self.assertEquals(des, st)

    def test8(self):

        ser = self.serializer.dumps(func)
        des = self.serializer.loads(ser)

        self.assertEquals(des(19), func(19))

    def test9(self):
        func_l = lambda x: x % 2 == 0

        ser = self.serializer.dumps(func_l)
        des = self.serializer.loads(ser)

        self.assertEquals(des(19), func_l(19))

    def test10(self):
        func_dec = my_decorator(func)

        ser = self.serializer.dumps(my_decorator)
        des = self.serializer.loads(ser)

        func_des = des(func)

        self.assertEquals(func_des(19), func_dec(19))

    def test11(self):
        cls = Three()

        ser = self.serializer.dumps(cls)
        des = self.serializer.loads(ser)

        self.assertEquals(des.test1(), cls.test1())

    def test12(self):
        static_method = One()

        ser = self.serializer.dumps(static_method)
        des = self.serializer.loads(ser)

        self.assertEquals(des.static_test1(), static_method.static_test1())
