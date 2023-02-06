<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ README - Corigine Technical Assignment 2023                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

This is the README for the Corigine Technical Assignment 2023 repository. 
This README contains a recipe for the set-up and implementation of a Speechbrain
-->

<!-------------------------- GIT PROJECT LOGO ------------------------------>
<br />
<p align="center">
  <a href="git clone https://uyspieter9@bitbucket.org/must_research/whalecalls.git">
    <img src="images/must_saigen.png" alt="Logo" width="80" height="80">
  </a>
  <h1 align="center">Whale Call Detection</h1>
  <p align="center">
    Recipe for Whale Call Detection set-up and implementation. 
    <br />
    Developed for MUST Research team.
    <br />
    <br />
  </p>
</p>
<!---------------------------------------------------------------------------->

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ Table of Contents                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Whale Call Detection](#Whale Call Detection)
    * [Datasets](#Datasets)
    * [Training](#Training)
    * [Inferencing](#Inferencing)
* [Hyperparameter Optimisation with Orion](#Hyperparameter Optimisation with Orion)
* [Results](#Results)
* [License](#license)
* [References](#References)

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ About The Project                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## About The Project

**Version**: 0.1
**Date**: 2022-05-04

This repository was developed and released by Edrich Fourie as part of interview process at Corigine where a solution-driven challenge to evaluate technical problem-solving capabilities that needs to be solve.
The problem that was given is a algorithmic problem where the Fibonacci sequence is defined by the recurrence relation. The candidate needs write a program to find the index of the first term in the Fibonacci sequence to contain N digits, where N is passed in on the command line.
Example:
The 7th term, F7, is the first term to contain two digits.
The 12th term, F12, is the first term to contain three digits.


<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ 1. Project Requirements                                                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## 1. Project Requiremnets
Your solution should adhere to the following:
• Use Python3.
• Use numpy for all math operations.
• If possible, avoid casting variables.
• Follow good programming practices.
• Be packaged and executable as a Docker container.

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ 2. The Program                                                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## 2. The Program

In this program, there are three functions. The first function is the *check_input* function. It takes the argument provided as input and if the input is a positive interger it excutes 
the *fibonacci_sequence_digit_index* function otherwise it will display an error message. The next function is the *fibonacci_sequence_digit_index* function. It takes the number of digits as input and returns the index of the first term in the fibonacci sequence that contains that number of digits. It uses the numpy library to store and update the values in the sequence and to perform all mathematical operations. The last function is the *count_digits* function. It takes a number as input and return the number of digits in the number. The reason for this function is to avoid casting of varibles. Overall the program takes the value of n from the command line and prints the result.


<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║ 4. Results                                                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->
-------------------------------------------------------------------------------
## 4. Results

| Dataset       | Precision     | Recall      | Neg. Rate   | Accuracy   |
| ------------- | ------------- | --------    | --------    | --------   |
| small_3_nbg   | 0.991477      | 0.966759    | 0.992846    | 0.980779   |

<p align="center">
  <img src="images/per_epoch_val_acc_graph.png" width="300" title="hover text">
  <img src="images/per_epoch_info_graph.png" width="300" alt="accessibility text">
</p>



