from setuptools import setup, find_packages

requires = [
    "faust-streaming",
    "networkx",
    "simple-settings",
]

setup(
    name='graph-streaming',
    version='0.0.1',
    description='Graph streaming framework',
    long_description='''
    Example running Faust with Docker Compose (zookeeper, kafka and schema-registry)
    ''',
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Mariusz Paluch',
    author_email='mariuszpaluch001@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=[],
    setup_requires=[],
    dependency_links=[]
)