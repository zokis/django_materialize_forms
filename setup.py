from setuptools import setup

setup(
    name='django-materialize-forms',
    version='0.2.1',
    url='https://github.com/zokis/django-materialize-forms',
    author='Marcelo Fonseca Tambalo',
    author_email='marcelo.zokis@gmail.com',
    license='MIT',
    packages=['materialize_forms', 'materialize_forms.templatetags'],
    include_package_data=True,
    description='Materializecss support for Django projects',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
