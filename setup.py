from setuptools import setup, find_packages

setup(
    name='autogui',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyautogui',
    ],
    entry_points={
        'console_scripts': [
            'autogui=autogui.core.automation:main',
        ],
    },
)
