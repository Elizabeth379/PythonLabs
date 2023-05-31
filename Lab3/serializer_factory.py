from json import JsonSerializer
from xml import XMLSerializer

class SerializerFactory:

    @staticmethod
    def serializer(name_type:str):

        match name_type.lower():

            case "json":
                return JsonSerializer()
            
            case "xml":
                return XMLSerializer()

            case _:
                ValueError
