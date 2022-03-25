from setuptools import setup, find_packages

__version__ = "0.11.0"

setup(name='semtest',
      version=__version__,
      description='Sem Test',
      author='Lars Fenneberg',
      author_email='lf@elemental.net',
      license='LGPG-3',
      python_requires='~=3.6',
      packages=find_packages('src'),
      package_dir={
          '': 'src',
      },
)
