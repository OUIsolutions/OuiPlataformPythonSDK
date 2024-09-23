from setuptools import setup, find_packages

setup(
    name='OuiPlataform',
    version='0.1.0',
    packages=find_packages(where='src'),  
    package_dir={'': 'src'},  
    package_data={
        '': ['*.py'],  
    },

    install_requires=[],
    author='Mateus',
    author_email='mateusmoutinho01@gmail.com',
    description='OUI Plataform SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/OUIsolutions/OuiPlataformPythonSDK',  # URL do repositório
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)