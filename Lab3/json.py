from serializer import Serializer, Deserializer
from constants import INT, FLOAT, STR, BOOL, NONE, VALUE
import regex

class JsonSerializer:
    def __int__(self):
        self.ser = Serializer()
        self.des = Deserializer()

    def convert(self,value):

        if isinstance(value, (int, float, bool)):
            return str(value).lower()

        elif isinstance(value,str):
            return '"' + value.replace("\\", "\\\\").replace("'", "\'").replace('"', "\"") + '"'

        elif isinstance(value, list):
            return "[" + ", ".join([self.convert(val) for val in value]) + "]"

        elif isinstance(value, dict):
            return "{" + ", ".join([f"{self.convert(key)}:{self.convert(val)}" for (key, val) in value.items()]) + "}"

    def find(self, value):

        value = value.strip()

        res = regex.fullmatch(INT, value)
        if res:
            return int(res.group(0))

        res = regex.fullmatch(FLOAT, value)
        if res:
            return float(res.group(0))

        res = regex.fullmatch(BOOL, value)
        if res:
            return res.group(0) == "true"

        res = regex.fullmatch(NONE, value)
        if res:
            return None

        res = regex.fullmatch(STR, value)
        if res:
            res = res.group(0)
            res = res.replace("\\\\", "\\").replace(r"\'", "'").replace(r"\"", '"')
            return res[1:-1]

        if value[0] == "[" and value[-1] == "]":
            value = value[1:-1]
            res = regex.findall(VALUE, value)
            return [self.find(match[0]) for match in res]

        if value[0] == "{" and value[-1] == "}":
            value = value[1:-1]
            res = regex.findall(VALUE, value)
            return {self.find(res[i][0]): self.find(res[i+1][0]) for i in range(0, len(res), 2)}

    