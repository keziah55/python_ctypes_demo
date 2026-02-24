#!/usr/bin/env python3


import ctypes
from pathlib import Path


class DemoStruct(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint8), ("c", ctypes.c_char)]


if __name__ == "__main__":

    lib_path = Path().absolute().joinpath("libcommand.so")
    assert lib_path.exists()

    libc = ctypes.CDLL(lib_path)

    ds = DemoStruct(ctypes.c_uint8(10), ctypes.c_char(b"b"))

    libc.printDemoStruct(ctypes.byref(ds))
