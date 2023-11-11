# setup.py
from setuptools import setup, find_packages

setup(
    name='math_quiz_game',
    version='3.10.7',
    packages=find_packages(),
    install_requires=[
        # Specify any dependencies here
        'random',
    ],
    entry_points={
        'console_scripts': [
            'math-quiz-game = math_quiz_game.quiz:math_quiz',
        ],
    },
)
