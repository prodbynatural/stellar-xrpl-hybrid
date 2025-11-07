from setuptools import setup, find_packages
import os

setup(
    name='stellar-xrpl-hybrid',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'stellar-sdk>=13.1.0',
        'xrpl-py>=1.0.0',
        'python-dotenv>=1.0.0',
    ],
    author='prodb',
    author_email='prodbynatural@gmail.com',
    description='A hybrid library combining Stellar and XRPL SDKs for cross-chain operations',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/prodbynatural/stellar-xrpl-hybrid',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
