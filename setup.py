from distutils.core import setup
setup(
  name = 'mizoo',
  packages = ['mizoo'], # this must be the same as the name above
  version = '0.1',
  description = 'Use deep learning to rename your images with the related caption.',
  author = 'Alberto Quesada',
  author_email = 'qa.alberto@gmail.com',
  url = 'https://github.com/albertoqa/mizoo.git', # use the URL to the github repo
  download_url = 'https://github.com/albertoqa/mizoo.git/tarball/0.1',
  keywords = ['captioning', 'image', 'ai', 'deep learning'],
  classifiers = [],
  license="MIT",
  install_requires=[
    # list of this package dependencies
    requests
  ],
  entry_points='''
    [console_scripts]
    mizoo=mizoo:cli
   '''
)
