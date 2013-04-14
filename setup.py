from setuptools import setup, find_packages
import re

VERSIONFILE="lpe-manager/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name='LPE Manager',
    version=verstr,
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-Babel',
        'Flask-Login',
        'Flask-SQLAlchemy',
        'Flask-WTF',
    ]
)
