from setuptools import setup

setup(name='lms',
      version='2020.05',
      description='LXDB MediaSorter, a program to sort files after metadata.',
      long_description='LXDB MediaSorter, a program to soft files fast and easy.',
      url='https://github.com/lxdb/lms',
      author='Denys Konovalov',
      author_email='service@lxdb.de',
      license='GPLv3',
      packages=['lms'],
      install_requires=['PyQt5'],
      zip_safe=False,
      scripts=['data/bin/lms', 'data/bin/lms-cli'],
      include_package_data=True,
      data_files=[("share/applications", ["data/de.lxdb.lms.desktop"]), ("share/icons/hicolor/symbolic/apps/", ["data/icons/symbolic/de.lxdb.lms-symbolic.svg"]), ("share/icons/hicolor/scalable/apps/", ["data/icons/normal/de.lxdb.lms.svg"]), ("share/metainfo", ["data/de.lxdb.lms.appdata.xml"])])
