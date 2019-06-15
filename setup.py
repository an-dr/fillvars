from setuptools import setup
from info import info

setup(name=info["name"],
      version=info["version"],
      description=info["description"],
      url=info["url"],
      author=info["author"],
      author_email=info["author_email"],
      license=info["license"],
      packages=[info["name"]],
      python_requires=">=2.7",
      zip_safe=False)
