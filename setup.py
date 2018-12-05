from setuptools import setup

setup(
    name='address-net',
    version='1.0',
    packages=['addressnet'],
    url='https://github.com/jasonrig/address-net',
    license='MIT',
    author='Jason Rigby',
    author_email='hello@jasonrig.by',
    description='Splits Australian addresses into their components',
    extras_require={
        "tf": ["tensorflow>=1.12"],
        "tf_gpu": ["tensorflow-gpu>=1.12.0"],
    },
    install_requires=[
        'numpy',
    ],
    include_package_data=True
)
