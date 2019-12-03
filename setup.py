from setuptools import setup

setup(
    name='s3_package',
    py_modules=['s3_package'],
    entry_points={
        'sceptre.hooks': [
            's3_package = s3_package:S3Package',
        ],
    }
)
