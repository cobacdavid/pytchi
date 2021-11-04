from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pytci',
    version='0.1',
    description='Python YouTube concentric Circles Image',
    long_description_content_type='text/markdown',
    long_description=long_description,
    # url='https://twitter.com/david_cobac',
    url="https://github.com/cobacdavid/pytci",
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
