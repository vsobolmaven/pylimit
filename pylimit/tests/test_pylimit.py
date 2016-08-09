from __future__ import absolute_import
from pylimit import PyRateLimit
from pylimit import PyRateLimitException
import unittest
import time


class TestPyLimit(unittest.TestCase):
    def test_exception(self):
        limit = PyRateLimit()
        self.assertRaises(PyRateLimitException, limit.attempt, u'test_namespace')

    def test_throttle(self):
        PyRateLimit.init(redis_host=u"localhost", redis_port=6379)
        limit = PyRateLimit()
        limit.create(10,                    # rate limit period in seconds
                     10)                    # no of attempts in the time period
        for x in xrange(0, 20):
            time.sleep(.5)
            if x < 10:
                self.assertTrue(limit.attempt(u'test_namespace'))
            else:
                self.assertFalse(limit.attempt(u'test_namespace'))
        time.sleep(6)
        self.assertTrue(limit.attempt(u'test_namespace'))

    def test_peek(self):
        PyRateLimit.init(redis_host=u"localhost", redis_port=6379)
        limit = PyRateLimit()
        limit.create(10,                    # rate limit period in seconds
                     10)                    # no of attempts in the time period
        for x in xrange(0, 10):
            self.assertTrue(limit.attempt(u'test_namespace2'))
        self.assertTrue(limit.is_rate_limited(u'test_namespace2'))
        time.sleep(10)
        self.assertFalse(limit.is_rate_limited(u'test_namespace2'))

