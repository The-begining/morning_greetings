from setuptools import setup, find_packages

setup(
    name="morning_greetings",
    version="0.1",
    packages=find_packages(),
    include_package_data= True,
    description="A package for sending automated Good Morning messages",
    long_description=open('README.md').read(),
    long_description_content_type= "text/markdown",
    url = "",
    author="Shubham singh",
    author_email="shsin5910@oslomet.no",
    install_requires=[],
    entry_points ={
        'console_scripts':[
            'morning_greetings = morning_greetings.main:main'
        ],
    },
    
)
