from ida_typeinf import tinfo_t

def get_func(int) -> "func_t": ...
def get_func_name(int) -> str: ...


class func_t:
    frsize: int
    def get_stkoff_delta(self) -> int: ...

