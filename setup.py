from distutils.core import setup

setup(name='docker-helper',
      version='0.1',
      description='Docker Helper to clean up and attach to a container',
      author='Gerald Lee',
      author_email='changgen218@gmail.com',
      url='https://github.com/GeraldLee/docker-helper.git',
      packages=['src'],
      scripts=['src/docker-helper'],
     )