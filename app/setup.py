from setuptools import setup, find_packages

setup(
    name='PySql',
    version='0.1',
    packages=find_packages(),  # Найдет все пакеты в текущем каталоге
    install_requires=[
        'psycopg2',
    ],
    python_requires='>=3.12.2',
)