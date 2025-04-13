import os
from setuptools import setup, find_packages


# Function to read the README file
def read_readme():
    with open(
        os.path.join(os.path.dirname(__file__), 'README.md'),
        encoding='utf-8'
    ) as f:
        return f.read()
    

setup(
    name='todo_cmd',
    version='1.0.1',
    description='A command line tool for managing todos.',
    author='Tianyu Yuan',
    author_email='1374736640@qq.com',
    packages=find_packages(),
    long_description=read_readme(),  # Read the README file
    long_description_content_type='text/markdown',
    license='MIT',
    entry_points={
        'console_scripts': [
            'todo=todo_cmd.main:main',  # 命令行工具名和入口点
        ],
    },
    install_requires=[
        'click',  # 依赖的库
        'rich',
        'rich-click'
    ],
    package_data={
        'todo_cmd': ['todo_cmd/language.json'],  # Include all JSON files
    },
    include_package_data=True
)