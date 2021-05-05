from setuptools import setup
 
setup(
    name='omnitrix-app',
    version='1.0',
    scripts=['omnitrix'],
    license="gpl-3.0",
    discription="App that simulates the omnitrix from the ben 10 tv show",
    author="array-in-a-matrix",
    url="https://array-in-a-matrix.github.io/",
    download_url="https://github.com/array-in-a-matrix/raspberry-pi-omnitrix/archive/refs/tags/1.0.tar.gz",
    keywords = ["game"],

    install_requires=[
        "tkinter",
        "PIL",
        "boombox"
    ],
    
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: cosplay',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3.0',   # Again, pick a license
    'Programming Language :: Python :: 3',
  ],
)
