import re
import inspect
import types

from constants import CODE_ATTRIBUTES, OBJECT_ATTRIBUTES, BASIC_TYPES, BASIC_COLLECTIONS


class Serializer:

    def serialize(self, obj):

        res = {}

        if isinstance(obj, (str, float, int, bool)):
            res["type"] = self.get_type_of_obj(obj)
            res["value"] = obj

        elif isinstance(obj, (tuple, list, set, frozenset, bytearray, bytes)):
            res["type"] = self.get_type_of_obj(obj)
            ser_object = []

            for value in obj:
                ser_object.append(self.serialize(value))

            res["value"] = ser_object

        elif isinstance(obj, dict):
            res["type"] = "dict"
            ser_object = []

            for value in obj.items():
                ser_object.append(self.serialize(value))

            res["value"] = ser_object

        elif isinstance(obj, types.CellType):
            res["type"] = "cell"
            res["value"] = self.serialize(obj.cell_contents)

        elif inspect.isfunction(obj):
            res["type"] = "function"
            res["value"] = self.serialize_type_function(obj)

        elif inspect.isclass(obj):
            res["type"] = "class"
            res["value"] = self.serialize_type_class(obj)

        elif inspect.iscode(obj):
            res["type"] = "code"
            args = dict()

            for (key, value) in inspect.getmembers(obj):
                if key in CODE_ATTRIBUTES:
                    args[key] = self.serialize(value)

            res["value"] = args

        elif not obj:
            res["type"] = "NoneType"
            res["value"] = "Null"

        else:
            res["type"] = "object"
            res["value"] = self.serialize_type_object(obj)

        return res

    def get_type_of_obj(self, obj):
        return re.search(r"\'(\w+)\'", str(type(obj)))[1]

    def serialize_type_object(self, obj):

        res = {}
        res["__class__"] = self.serialize(obj.__class__)

        fields = {}

        for (key, value) in inspect.getmembers(obj):
            if not inspect.isfunction(value) and not inspect.ismethod(value) and not key.startswith("__"):
                fields[key] = self.serialize(value)

        res["__members__"] = fields

        return res

    def serialize_type_function(self, obj, class_object=None):

        res = {}
        arguments = {}

        res["__name__"] = obj.__name__
        res["__globals__"] = self.get_globals(obj, class_object)

        if obj.__closure__:
            res["__closure__"] = self.serialize(obj.__closure__)

        else:
            res["__closure__"] = self.serialize(tuple())

        for (key, value) in inspect.getmembers(obj.__code__):
            if key in CODE_ATTRIBUTES:
                arguments[key] = self.serialize(value)

        res["__code__"] = arguments

        return res

    def get_globals(self, obj, class_object = None):

        res = {}
        globals = obj.__globals__

        for value in obj.__code__.co_names:

            if value in globals:

                if inspect.isclass(globals[value]):
                    if (class_object and obj.__globals__[value] != class_object) or not class_object:
                        res[value] = self.serialize(globals[value])

                elif isinstance(globals[value], types.ModuleType):
                    res["module" + value] = self.serialize(globals[value].__name__)

                elif value != obj.__code__.co_name:
                    res[value] = self.serialize(globals[value])

                else:
                    res[value] = self.serialize(obj.__name__)

        return res

    def serialize_type_class(self, obj):

        res = {}
        bases = []

        for base in obj.__bases__:
            if base != object:
                bases.append(self.serialize(base))

        res["__name__"] = self.serialize(obj.__name__)
        res["__bases__"] = \
            {
                "type": "tuple",
                "value": bases
            }

        for key in obj.__dict__:

            value = obj.__dict__[key]

            if key in OBJECT_ATTRIBUTES or type(value) in (types.WrapperDescriptorType, types.MethodDescriptorType, types.BuiltinFunctionType,
                                                           types.GetSetDescriptorType, types.MappingProxyType):
                continue

            elif isinstance(value, (staticmethod, classmethod)):

                if isinstance(value, staticmethod):
                    value_type = "staticmethod"
                else:
                    value_type = "classmethod"

                res[key] = \
                    {
                        "type": value_type,
                        "value": {
                            "type": "function",
                            "value": self.serialize_type_function(value.__func__, obj)
                        }
                    }

            elif inspect.ismethod(value):
                res[key] = self.serialize_type_function(value.__func__, obj)

            elif inspect.isfunction(value):
                res[key] = \
                    {
                        "type": "function",
                        "value": self.serialize_type_function(value, obj)
                    }

            else:
                res[key] = self.serialize(value)

        return res


class Deserializer:

    def deserialize(self, obj):

        if obj["type"] in BASIC_TYPES:
            return self.deserialize_basic_types(obj["type"], obj["value"])

        elif obj["type"] in BASIC_COLLECTIONS:
            return self.deserialize_basic_collections(obj["type"], obj["value"])

        elif obj["type"] == "dict":
            return dict(self.deserialize_basic_collections("list", obj["value"]))

        elif obj["type"] == "cell":
            return types.CellType(self.deserialize(obj["value"]))

        elif obj["type"] == "function":
            return self.deserialize_type_function(obj["value"])

        elif obj["type"] == "class":
            return self.deserialize_type_class(obj["value"])

        elif obj["type"] == "staticmethod":
            return staticmethod(self.deserialize(obj["value"]))

        elif obj["type"] == "classmethod":
            return classmethod(self.deserialize(obj["value"]))

        elif obj["type"] == "object":
            return self.deserialize_type_object(obj["value"])

        elif obj["type"] == "cell":
            return types.CellType(self.deserialize(obj["value"]))

        elif obj["type"] == "code":
            code = obj["value"]
            return types.CodeType(*tuple(self.deserialize(code[attribute]) for attribute in CODE_ATTRIBUTES))

    def deserialize_basic_types(self, type_obj, obj):

        if type_obj == "int":
            return int(obj)

        elif type_obj == "float":
            return float(obj)

        elif type_obj == "bool":
            return bool(obj)

        elif type_obj == "str":
            return str(obj)

    def deserialize_basic_collections(self, type_obj, obj):

        if type_obj == "tuple":
            return tuple(self.deserialize(elem) for elem in obj)

        elif type_obj == "list":
            return list(self.deserialize(elem) for elem in obj)

        elif type_obj == "set":
            return set(self.deserialize(elem) for elem in obj)

        elif type_obj == "frosenset":
            return frozenset(self.deserialize(elem) for elem in obj)

        elif type_obj == "bytearray":
            return bytearray(self.deserialize(elem) for elem in obj)

        elif type_obj == "bytes":
            return bytes(self.deserialize(elem) for elem in obj)

    def deserialize_type_function(self, obj):

        globals = obj["__globals__"]

        closures = obj["__closure__"]
        code = obj["__code__"]

        obj_globals = {}

        for key in globals:

            if "module" in key:
                obj_globals[globals[key]["value"]] = __import__(globals[key]["value"])

            elif globals[key] != obj["__name__"]:
                obj_globals[key] = self.deserialize(globals[key])

        closures = tuple(self.deserialize(closures))

        code = types.CodeType(*tuple(self.deserialize(code[attribute]) for attribute in CODE_ATTRIBUTES))

        res = types.FunctionType(code=code, globals=obj_globals, closure=closures)
        res.__globals__.update({res.__name__: res})

        return res

    def deserialize_type_class(self, obj):

        bases = self.deserialize(obj["__bases__"])
        items = {}

        for item, value in obj.items():
            items[item] = self.deserialize(value)

        res = type(self.deserialize(obj["__name__"]), bases, items)

        for item in items.values():

            if inspect.isfunction(item):
                item.__globals__.update({res.__name__: res})

            elif isinstance(item, (staticmethod, classmethod)):
                item.__func__.__globals__.update({res.__name__: res})

        return res

    def deserialize_type_object(self, obj):

        cls = self.deserialize(obj["__class__"])
        items = {}

        for (key, value) in obj["__members__"].items():
            items[key] = self.deserialize(value)

        res = object.__new__(cls)
        res.__dict__ = items

        return res