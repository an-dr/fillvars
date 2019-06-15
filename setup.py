from setuptools import setup
from info import info

setup(name=info["fillvars"],
      version=info["version"],
      description=info["description"],
      url=info["url"],
      author=info["author"],
      author_email=info["author_email"],
      license=info["license"],
      packages=['fillvars'],
      python_requires=">=2.7",
      zip_safe=False)
