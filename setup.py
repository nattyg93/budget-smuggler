#!/usr/bin/env python
import io

from setuptools import find_packages, setup


def _read(filename, as_lines=True):
    with io.open(filename, encoding='utf-8') as handle:
        if as_lines:
            return [line.strip('\n').strip() for line in handle.readlines()]
        return handle.read()


setup(
    name='budget_smuggler',
    version='0.1.0',
    description='RESTful API for Budget Smuggler - a simple budgeting webapp',
    long_description=_read('README.md', as_lines=False),
    author='Nathanael Gordon',
    author_email='nathanael.l.gordon@gmail.com',
    url='https://github.com/nattyg93/budget-smuggler',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'dj-core[defaults]==0.1.1',
        'dj-core-drf[defaults]==0.1.0',
        'Django==1.11.7',
    ],
    extras_require={
        'dev': [
            'ipdb',
            'ipython',
            'ptpython',
            'yapf',
            'werkzeug',
            'django-extensions',
        ],
        'prod': [
            'gunicorn',
        ]
    },
    python_requires='>=3.5',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Private :: Do not Upload',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
