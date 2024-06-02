from setuptools import setup, find_packages

setup(
    name="informal_detector",
    version="0.1.1",
    description="A Python package to check if a text is informal Persian.",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author="Mahta Fetrat",
    author_email="77fetrat@gmail.com",
    url="https://github.com/MahtaFetrat/Persian-Informal-Text-Detector",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
