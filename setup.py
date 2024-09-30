from setuptools import setup, find_packages


setup(
    name='pyHLS',
    version='0.0.1',
    license='MIT',
    author="Worakrit Sittirit",
    author_email='kritsitti.coe@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/worakrit-sittirit/pyHLS.git',
    keywords='MKY36 HLS USB Board',
    description= "python lib for call the HLS DLL 's function.",

)
