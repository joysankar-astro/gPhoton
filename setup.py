from setuptools import setup, find_packages

setup(
    name='gPhoton-astro',
    version='1.0.4',
    author='Joysankar Majumdar',
    author_email='j.majumdar@uw.edu.pl',
    description='Modified version of gPhoton for GALEX photon data analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joysankar-astro/gPhoton',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'numpy>=1.20',
        'pandas>=1.2',
        'astropy>=5.0',
        'requests>=2.25',
        'scipy>=1.6',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
