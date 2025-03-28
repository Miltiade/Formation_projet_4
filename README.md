# Formation_projet_4

SOFTWARE FOR RUNNING CHESS TOURNAMENTS

---------------------------------------

What is it?

This Python stand-alone software is for running chess tournaments: the user creates a new tournament (i.e. creating players, setting tournament's place and date, etc.), and types matches' results. The software pairs players before each round, and adds up each player's score until the end of the tournament.
The software displays information on demand, such as existing list of players.
The software saves and loads a given tournament on demand.
The software works offline. It is used through the Terminal of the computer where it is installed.


---------------------------------------

## Installation

1. Clone the repository.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main program:
    ```sh
    python main.py
    ```

## Code Quality

1. Generate flake8 report:
    ```sh
    flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport