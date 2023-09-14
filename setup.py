from setuptools import setup

setup(
    name='yt-downloader',
    version='1.0',
    packages=['src'],
    url='',
    license='',
    author='cedric',
    author_email='cedric.sillaber@gmail.com',
    description='youtube downloader',
    install_requires=[
        "pytube",
        "pyinstaller",
        "rich",
        "pyinstaller",
        # place for other packages
    ],
)
