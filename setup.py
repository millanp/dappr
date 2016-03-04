from setuptools import setup

setup(name='dappr',
      version='0.1',
      description='Django app for registration, with an approval step.',
      url='https://github.com/millanp/dappr',
      author='Millan Philipose',
      author_email='millanmakes@gmail.com',
      license='MIT',
      packages=['dappr'],
      install_requires=[
          'Django>=1.8',
      ],
      zip_safe=False
)
