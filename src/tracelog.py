from datetime import datetime
from singleton import SingletonMeta
from pathlib import Path
import os
import re
import inspect

ERROR, ABNORMAL, FT_GLOBAL = range(0, 3)

TRACE_LOG_DIR = Path(__file__).resolve().parent.parent.joinpath(
    "logs").joinpath("trace_log.txt")

LOG_FILE_BUFFER = 10000


def trace_string(trace_object):
    if trace_object is ERROR:
        return "ERROR"
    elif trace_object is ABNORMAL:
        return "ABNORMAL"
    elif trace_object is FT_GLOBAL:
        return "FT_GLOBAL"


class TraceLogger(metaclass=SingletonMeta):
    def __init__(self):
        self._to_list = [ERROR, ABNORMAL, FT_GLOBAL]
        self._enabled = [ERROR, ABNORMAL]

    def enable_trace(self, trace_object):
        if trace_object in self._to_list:
            if not trace_object in self._enabled:
                self._enabled.append(trace_object)

    def disable_trace(self, trace_object):
        if trace_object is not ABNORMAL and trace_object is not ERROR:
            if trace_object in self._enabled:
                self._enabled.remove(trace_object)

    def trace(self, trace_object, *args):
        if trace_object in self._enabled:
            result = ''
            for arg in args:
                argstr = try_get_class_name(str(arg))
                result += argstr
            prev_frame = inspect.currentframe().f_back
            caller_class = try_get_class_name(
                str(prev_frame.f_locals['self'].__class__))
            caller_method = str(prev_frame.f_code.co_name)
            result = get_trace_line(
                trace_object, caller_class, caller_method, result)
            print(result)
            save_line_to_file(result)


def try_get_class_name(wrapedstring):
    match = re.match(r"\<class \'(.*)\'\>", wrapedstring)
    if match is not None:
        wrapedstring = match.group(1).split('.')[-1]
    return wrapedstring


def get_trace_line(trace_object, caller_class, caller_method, stringline):
    return str(datetime.now()) + " " + caller_class + "::" + caller_method + "() " + trace_string(trace_object) + " \"" + stringline + "\""


def save_line_to_file(line):
    filelines = []
    if not TRACE_LOG_DIR.parent.exists():
        TRACE_LOG_DIR.parent.mkdir()
    elif TRACE_LOG_DIR.exists():
        with TRACE_LOG_DIR.open(mode='r') as file:
            filelines = file.readlines()
            if len(filelines) == LOG_FILE_BUFFER:
                filelines.pop(0)

    filelines.append(line + '\n')

    with TRACE_LOG_DIR.open(mode='w') as file:
        file.writelines(filelines)
        file.close()
