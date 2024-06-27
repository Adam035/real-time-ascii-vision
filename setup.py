from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as file:
    readme = file.read()

with open('LICENSE', 'r', encoding='utf-8') as file:
    license_content = file.read()

setup(
    name='real-time-ascii-vision',
    version='0.1.0',
    description='Real time ASCII representation of images from camera',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Adam Lipian',
    url='https://github.com/Adam035/real-time-ascii-vision',
    license=license_content,
    packages=find_packages(exclude='tests')
)
