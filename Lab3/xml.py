from serializer import Serializer, Deserializer
from constants import ELEMENT
import regex

class XMLSerializer:

    def __int__(self):
        self.ser = Serializer()
        self.des = Deserializer()

    def convert(self, value):

        if isinstance(value, (int, float, bool)):
            return f"<{type(value).__name__}>{str(value)}</{type(value).__name__}>"

        elif isinstance(value, str):
            value = value.replace('"', "&quot;").replace("'", "&apos;").replace("<", "&lt").replace(">", "&gt").replace("&", "&amp")
            return f"<str>{value}</str>"

        elif isinstance(value, list):
            value = "".join([self.convert(val) for val in value])
            return f"<list>{value}</list>"

        elif isinstance(value, dict):
            value = "".join([f"{self.convert(key)}{self.convert(val)}" for (key, val) in value.items()])
            return f"<dict>{value}</dict>"

        elif not value:
            return "<NoneType>None</NoneType>"

    def find(self, value):

        res = regex.fullmatch(ELEMENT, value)

        if not res:
            return

        key = res.group("key")
        val = res.group("value")

        match key:

            case "int":
                return int(val)

            case "float":
                return float(val)

            case "bool":
                return str(val) == "True"

            case "str":
                return val.replace("&quot;", '"').replace("&apos;", "'").replace("&lt", '<').replace("&gt", '>').replace("&amp",
                                                                                                                 '&')
            case "list":
                res = regex.findall(ELEMENT, val)
                return [self.find(match[0]) for match in res]

            case "dict":
                res = regex.findall(ELEMENT, val)
                return {self.find(res[i][0]): self.find(res[i + 1][0]) for i in range(0, len(res), 2)}

            case "NoneType":
                return None

    def dumps(self, obj):
        return self.convert(self.ser.serialize(obj))

    def dump(self, obj, f):
        f.write(self.dumps(obj))

    def loads(self, value):
        return self.des.deserialize(self.find(value))

    def load(self, f):
        return self.loads(f.read)
    