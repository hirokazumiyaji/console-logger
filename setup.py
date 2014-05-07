# coding: utf-8


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='console_logger',
    version='0.0.1',
    description='Python Custom Logger',
    long_description='',
    url='',
    author='Hirokazu Miyaji',
    maintainer_email='hirokazu.miyaji@gmail.com',
    keywords=['logger'],
    license='MIT',
    packages=['console'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ]
)
