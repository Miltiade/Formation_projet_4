# Formation_projet_4

SOFTWARE FOR RUNNING CHESS TOURNAMENTS

---------------------------------------

## Table of Contents
1. [What is it?](#what-is-it)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Quality](#code-quality)
5. [Features](#features)
6. [Contributing](#contributing)
7. [License](#license)

---------------------------------------

## What is it?

This Python stand-alone software is for running chess tournaments: the user creates a new tournament (i.e. creating players, setting tournament's place and date, etc.), and types matches' results. The software pairs players before each round, and adds up each player's score until the end of the tournament.
The software displays information on demand, such as existing list of players.
The software saves and loads a given tournament on demand.
The software works offline. It is used through the Terminal of the computer where it is installed.

---------------------------------------

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd Formation_projet_4
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main program:
    ```sh
    python main.py
    ```
2. Example commands:
    - Create a new tournament.
    - Load a tournament.

## Code Quality

1. Generate flake8 report:
    ```sh
    flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport
    ```

## Features

- Create and manage chess tournaments.
- Pair players automatically for each round.
- Save and load tournaments.
- View player and tournament details.
- Works offline and standalone.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```sh
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```sh
    git commit -m "Description of changes"
    ```
4. Push to your branch:
    ```sh
    git push origin feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.