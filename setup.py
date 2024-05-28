from setuptools import setup, find_packages

setup(
    name='EmtFreeMalaga',
    version='0.0.1',
    license='MIT',
    description='Paquete para obtener los tiempos de las paradas de la emt de malaga sin tener que hacer uso de la api',
    author='Luis Aranda Hidalgo',
    install_requieres=['beautifulsoup4', 'requests'],
    author_email='arandahidalgoluis@hmail.com',
    packages=find_packages(),
    url='git@github.com:ArandaHidalgoLuis/libreriaEMT.git',
)