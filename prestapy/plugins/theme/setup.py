from setuptools import setup, find_packages

setup(
    name='prestapy_theme_plugin',
    version='0.0.1',
    description="Theme plugin",
    packages=find_packages('.'),
    entry_points={
        'plugin_system': 'main = theme:main'
    },
)
