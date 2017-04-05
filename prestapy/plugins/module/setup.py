from setuptools import setup, find_packages

setup(
    name='prestapy_module_plugin',
    version='0.0.1',
    description="Module plugin",
    packages=find_packages('.'),
    entry_points={
        'plugin_system': 'main = module:main'
    },
)
