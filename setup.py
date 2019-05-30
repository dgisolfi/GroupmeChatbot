#!/usr/bin/python3
from setuptools import setup

setup(
    name='GroupmeChatbot',
    version='3.0.0',
    description='A Bot that responds with custom messages when mentioned in a Groupme chat',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dgisolfi/GroupmeChatbot',
    author='dgisolfi',
    license='MIT',
    packages=['GroupmeChatbot'],
    install_requires=[
        'chatterbot>=0.8.7',
        'chatterbot-corpus>=1.1.2',
        'flask>=0.12.3',
        'requests>=2.20.0',
        'markdown>=2.6.11',
    ],
    zip_safe=False
)