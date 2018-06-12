from __future__ import absolute_import
from distutils.core import setup
setup(
  name = u'pylimit',
  packages = ['pylimit'],
  version = u'0.1.5',
  description = u'A distributed rate limiting library for python using leaky bucket algorithm and Redis',
  author=u'Biplap Sarkar',
  author_email=u'biplap.sarkar@gmail.com',
  url=u'https://github.com/biplap-sarkar/pylimit',
  download_url=u'https://github.com/biplap-sarkar/pylimit/archive/v0.1.5.tar.gz',
  keywords=[u'rate limiting', u'throttle', u'redis'],
  classifiers=[],
)
