#!/usr/bin/env python3


import ctypes
from pathlib import Path


class DemoStruct(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint8), ("c", ctypes.c_char)]


class CommandStruct(ctypes.Structure):
    _fields_ = [("size", ctypes.c_uint8), ("command", ctypes.POINTER(ctypes.c_uint8))]


if __name__ == "__main__":

    lib_path = Path().absolute().joinpath("libcommand.so")
    assert lib_path.exists()

    libc = ctypes.CDLL(lib_path)

    ds = DemoStruct(ctypes.c_uint8(10), ctypes.c_char(b"b"))

    libc.printDemoStruct(ctypes.byref(ds))

    cmd = "1234"
    cmd_bts = bytes.fromhex(cmd)
    print(cmd_bts)

    Array = ctypes.c_uint8 * len(cmd_bts)
    ctypes_array = Array.from_buffer_copy(cmd_bts)
    print(ctypes_array[0], ctypes_array[1])

    cs = CommandStruct(ctypes.c_uint8(len(cmd_bts)), ctypes_array)

    libc.printCommand(ctypes.byref(cs))
