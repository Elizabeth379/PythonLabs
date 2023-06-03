CODE_ATTRIBUTES = ("co_argcount", "co_posonlyargcount", "co_kwonlyargcount", "co_nlocals", "co_stacksize", "co_flags", "co_code",
                  "co_consts", "co_names", "co_varnames", "co_filename", "co_name", "co_firstlineno", "co_lnotab", "co_freevars", "co_cellvars")

OBJECT_ATTRIBUTES = ("__name__", "__base__", "__basicsize__", "__dictoffset__", "__class__")


BASIC_TYPES = ("int", "float", "bool", "str")

BASIC_COLLECTIONS = ("tuple", "list", "set", "frozenset", "bytearray", "bytes")

INT = r"[+-]?\d+"
FLOAT = r"([+-]?\d+(\.\d+))"
STR = r"\"((\\\")|[^\"])*\""
BOOL = r"\b(true|false)\b"
NONE = r"\b(Null)\b"

LIST_RECURSION = r"\[(?R)?(,(?R))*\]"
VALUE_RECURSION = r"\{((?R):(?R))?(,(?R):(?R))*\}"

VALUE = fr"\s*({LIST_RECURSION}|{VALUE_RECURSION}|{STR}|{FLOAT}|{BOOL}|{INT}|{NONE}\s*)"

REG_BASE_TYPES = r"str|int|float|bool|NoneType|list|dict"
ELEMENT = fr"\s*(\<(?P<key>{REG_BASE_TYPES})\>(?P<value>([^<>]*)|(?R)+)\</(?:{REG_BASE_TYPES})\>)\s*"
