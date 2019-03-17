from setuptools import setup, find_packages

setup(
    name='Python-Mkdocs-Autodoc-Plugin',
    version='1.0.1',
    packages=['dodoc'],
    url='https://github.com/plasmatech8/Python-Mkdocs-Autodoc-Plugin',
    license='MIT',
    author='Mark Connelly',
    author_email='markjunk669@gmail.com',
    description='DoDoc is a plugin that does autodoc.',
    install_requires=['mkdocs'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'dodoc = dodoc:DoDoc',
        ]
    },
)
