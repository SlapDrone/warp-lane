from setuptools import setup, find_packages

setup(
    name='warp_lane_server',
    version='0.1',
    url='https://github.com/mypackage.git',
    author='dev@pomeron.io',
    author_email='dev@pomeron.io',
    description='Description of my package',
    packages=find_packages(),
    scripts=['scripts/run_server.py'],
    install_requires=[
        'bcrypt',
        'dateutils',
        'psycopg2',
        'sanic',
    ],
)
