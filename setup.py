from setuptools import setup, find_packages

setup(
    name='SnakeGameAI',
    version='1.0.0',
    description='A Snake game AI that learns to play using Deep Q-Learning.',
    author='Anahita Bhalme',
    author_email='',
    url='https://github.com/anahita-jpeg/SnakeGame',
    packages=find_packages(),
    install_requires=[
        'pygame',
        'torch',
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
