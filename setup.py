from setuptools import setup, find_packages

with open('README_pypi.md') as f:
    long_description = f.read()

setup(
    name='pytchi',
    version='0.2',
    description='Python YouTube Concentric Circles Image',
    long_description_content_type='text/markdown',
    long_description=long_description,
    # url='https://twitter.com/david_cobac',
    url="https://github.com/cobacdavid/pytchi",
    author='David COBAC',
    author_email='david.cobac@gmail.com',
    license='CC-BY-NC-SA',
    keywords=['youtube',
              'image',
              'concentric',
              'circle'],
    packages=find_packages(),
    install_requires=["pycairo",
                      "python-slugify",
                      "pytube",
                      "opencv-python-headless"],
    python_requires='>3.6'
)
