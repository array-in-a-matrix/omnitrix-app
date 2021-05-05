from setuptools import setup
 
setup(
    name='omnitrix',
    version='1.0',
    scripts=['omnitrix'],
    license="gpl-3.0",
    discription="App that simulates the omnitrix from the ben 10 tv show",
    author="array-in-a-matrix",
    url="https://array-in-a-matrix.github.io/",
    download_url="https://github.com/array-in-a-matrix/omnitrix-app/archive/refs/tags/1.0.tar.gz",
    keywords = ["game"],

    install_requires=[
        "tkinter",
        "PIL",
        "boombox"
    ],
    
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3',
  ],
)
