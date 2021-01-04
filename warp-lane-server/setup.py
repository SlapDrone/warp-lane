from setuptools import setup, find_packages

setup(
    name='warp_lane_server',
    version='0.1',
    url='https://github.com/mypackage.git',
    author='Pomeron',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),
    install_requires=[
        'bcrypt',
        'dateutils',
        'psycopg2',
        'sanic',
    ],
)