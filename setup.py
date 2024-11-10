from setuptools import setup, find_packages

setup(
    name='todo_cmd',
    version='0.1.0',
    description='A command line tool for managing todos.',
    author='Tianyu Yuan',
    author_email='1374736640@qq.com',
    packages=find_packages(),
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
)