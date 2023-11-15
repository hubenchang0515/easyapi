from setuptools import setup, find_packages

setup(
    name='easyapi',

    version='1.0',

    author='planc',

    author_email='hubenchang0515@outlook.com',

    description='',
    
    license='GNU General Public License v3.0',

    url='https://github.com/hubenchang0515/easyapi',

    packages=find_packages("src"),
    package_dir = {'' : 'src'},

    platforms = 'any',
    zip_safe = False,
    include_package_data = True,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],

    entry_points={"console_scripts": [
        "easyapi = easyapi.easyapi:main"
    ]}
)