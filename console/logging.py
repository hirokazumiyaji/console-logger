# coding: utf-8
from __future__ import absolute_import, unicode_literals
import sys
from logging import NOTSET, WARNING, Logger, StreamHandler

__all__ = ['getLogger', 'critical', 'error', 'exception',
           'warning', 'warn', 'info', 'debug']

COLOR_NONE = '\e[m'
COLOR_RED = '\e[31m'
COLOR_BLUE = '\e[3m'
COLOR_YELLOW = '\e[33m'

class ConsoleLogger(Logger):
    def __init__(self, name, level=NOTSET):
        super(ConsoleLogger, self).__init__(name, level)
        handler = StreamHandler(sys.stdout)
        handler.setLevel(level)
        self.addHandler(handler)

    def _generate_color_msg(self, msg, color):
        return '{}{}{}'.format(color, msg, COLOR_NONE)

    def debug(self, msg, *args, **kwargs):
        msg = self._generate_color_msg(msg, COLOR_NONE)
        super(ConsoleLogger, self).debug(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        msg = self._generate_color_msg(msg, COLOR_RED)
        super(ConsoleLogger, self).critical(msg, *args, **kwargs)

    fatal = critical

    def error(self, msg, *args, **kwargs):
        msg = self._generate_color_msg(msg, COLOR_RED)
        super(ConsoleLogger, self).error(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        msg = self._generate_color_msg(msg, COLOR_RED)
        super(ConsoleLogger, self).exception(msg, *args, **kwargd)

    def warning(self, msg, *args, **kwargs):
        msg = self._generate_color_msg(msg, COLOR_YELLOW)
        super(ConsoleLogger, self).warning(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        msg = self._generate_color_msg(msg, COLOR_YELLOW)
        super(ConsoleLogger, self).warn(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        msg = self._generate_color_msg(msg, COLOR_BLUE)
        super(ConsoleLogger, self).info(msg, *args, **kwargs)

root = ConsoleLogger('root', WARNING)

def getLogger(name=None):
    if name:
        ConsoleLogger.manager.setLoggerClass(ConsoleLogger)
        logger = ConsoleLogger.manager.getLogger(name)
        logger.addHandler(logging.StreamHandler)
    else:
        return root

def critical(msg, *args, **kwargs):
    root.critical(msg, *args, **kwargs)

fatal = critical

def error(msg, *args, **kwargs):
    root.error(msg, *args, **kwargs)

def exception(msg, *args, **kwargs):
    root.exception(msg, *args, **kwargs)

def warning(msg, *args, **kwargs):
    root.warning(msg, *args, **kwargs)

def warn(msg, *args, **kwargs):
    root.warn(msg, *args, **kwargs)

def info(msg, *args, **kwargs):
    root.info(msg, *args, **kwargs)

def debug(msg, *args, **kwargs):
    root.debug(msg, *args, **kwargs)
