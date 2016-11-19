from setuptools import setup
import sys, twine

setup(
    name='mizoo',
    version='0.5',

    description='Use deep learning to rename your images with the related caption.',
    long_description='Use deep learning to rename your images with the related caption.',
    license='MIT',
    url = 'https://github.com/albertoqa/mizoo.git', # use the URL to the github repo
    download_url = 'https://github.com/albertoqa/mizoo.git/tarball/0.1',

    author = 'Alberto Quesada',
    author_email = 'qa.alberto@gmail.com',

    classifiers=[
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],

    keywords = ['captioning', 'image', 'ai', 'deep learning'],
    packages=["mizoo"],

    entry_points={
        "console_scripts": [
            "mizoo = mizoo.mizoo:main",
        ],
    },

    install_requires=[
        "requests"
    ],
)
