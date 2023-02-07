<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ README - Corigine Technical Assignment 2023                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

This is the README for the Corigine Technical Assignment 2023 repository. 

-->

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ Table of Contents                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## Table of Contents

* [About the Project](#about-the-project)
* [Project Requirements](#project-requirements)
* [Setup Program](#setup-program)
* [The Program](#the-program)
* [Results](#results)


<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ About The Project                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## About The Project

**Version**: 0.1
**Date**: 2022-05-04

This repository was developed and released by Edrich Fourie as part of the interview process at Corigine, where a solution-driven challenge is given to evaluate technical problem-solving capabilities. The task is designed to evaluate the candidate's ability to utilise new tools, coding, documentation, and error checking


The problem is algorithmic, where the recurrence relation defines the Fibonacci sequence. The candidate needs to write a program to find the index of the first term in the Fibonacci sequence to contain N digits, where N is passed in on the command line.


Example:\
The 7th term, F7, is the first term to contain two digits.\
The 12th term, F12, is the first term to contain three digits.


<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ 1. Project Requirements                                                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## Project Requirements
Your solution should adhere to the following:

* Use Python3.
* Use numpy for all math operations.
* If possible, avoid casting variables.
* Follow good programming practices.
* Be packaged and executable as a Docker container.

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ 2. Setup Program                                                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## Setup Program

1. Make sure you have Docker installed. You can check if Docker is installed by running the following:

```consol
$ docker --version
$ Docker version 23.0.0, build e92dd87
```

It is only installed if it shows the Docker version. Install Docker by following these steps in the video:

[Install Docker](https://www.youtube.com/watch?v=aMKUuaga85A&t=48s&ab_channel=ProgrammingKnowledge)

2. Make sure Python3 is installed. You can check if Python3 is installed by runningthe following:

```consol
$ python --version
$ Python 3.8.5
```

The Python version must be 3. It is only installed if it shows the Python version. Install Python by following these steps in the video:

[Install Python](https://www.youtube.com/watch?v=7H-DcdSmV0U&ab_channel=KamrulsKode)

4. Once everything is installed and working. Build a Docker container for the project by:

Option 1:

Cloning the git repository:\
`$ git clone https://github.com/EdrichF/fibonacci-term.git`\
Change directory:\
`$ cd fibonacci-term/`\
Build docker image:\
`$ docker build --tag fibonacci-term .`

Option 2:\
Extract fibonacci.tar.gz\
`$ tar -xvzf ./fibonacci.tar.gz`\
Change directory:\
`$ cd fibonacci-term/`\
Build docker image:\
`$ docker build --tag fibonacci-term .`


5. Run the program by typing in the terminal the following:

`docker run --rm fibonacci-term n`

where *n* is the number of digits.

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ 3. The Program                                                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## The Program

In this program, there are three functions. The first function is the *check_input* function. It takes the argument provided as input, and if the input is a positive integer, it executes the *fibonacci_sequence_digit_index* function; otherwise, it will display an error message. 

The next function is the *fibonacci_sequence_digit_index* function. It takes the number of digits as input and returns the index of the first term in the Fibonacci sequence that contains that number of digits. It uses the numpy library to store and update the sequence values and perform all mathematical operations. 

The last function is the *count_digits* function. It takes a number as input and returns the number of digits in the number. The reason for this function is to avoid the casting of variables. Overall the program takes the value of n from the command line and prints the result.


<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ 4. Results                                                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## Results

Terminal Output of different cases.

```consol
fibonacci-term$ docker run --rm fibonacci-term 2
In the Fibonacci sequence the first term to contain 2 digits is at index: 7
fibonacci-term$ docker run --rm fibonacci-term 3
In the Fibonacci sequence the first term to contain 3 digits is at index: 12
fibonacci-term$ docker run --rm fibonacci-term 10
In the Fibonacci sequence the first term to contain 10 digits is at index: 45
fibonacci-term$ docker run --rm fibonacci-term -1
Input is incorrect. Enter a Postive Interger.
fibonacci-term$ docker run --rm fibonacci-term 1.1
Input is incorrect. Enter a Postive Interger.
fibonacci-term$ docker run --rm fibonacci-term k
Input is incorrect. Enter a Postive Interger.

```





