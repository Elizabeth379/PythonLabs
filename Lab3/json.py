from serializer import Serializer, Deserializer

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

    
