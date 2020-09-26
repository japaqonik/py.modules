from datetime import datetime
from singleton import SingletonMeta
import re

ERROR, ABNORMAL, FT_GLOBAL = range(0, 3)

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

    def enabled_trace(self, trace_object):
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
            result = get_trace_line(trace_object, result)
            print(result)

def try_get_class_name(wrapedstring):
    match = re.match(r"\<class \'(.*)\'\>", wrapedstring)
    if match is not None:
        wrapedstring = match.group(1).split('.')[-1]
    return wrapedstring

def get_trace_line(trace_object, stringline):
    return str(datetime.now()) + " " + trace_string(trace_object) + " \"" + stringline + "\"" 