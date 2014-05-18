#!/usr/bin/env python
from setuptools import setup

setup(name='PyrserPTT',
      version='0.1',
      description='A Ptt Artical Parser',
      author='eternnoir',
      author_email='eternnoir@gmail.com',
      url='https://github.com/eternnoir/PyrserPTT',
      packages=['PyrserPTT'],
      install_requires=['BeautifulSoup==3.2.1',
                        'mechanize==0.2.5',
                        'mongoengine==0.8.7',
                        'pymongo==2.6.3',
                        'wsgiref==0.1.2',],
      )
