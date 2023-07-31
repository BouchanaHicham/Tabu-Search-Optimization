Tabu Search Algorithm
This is a Python implementation of the Tabu Search algorithm. The Tabu Search is a metaheuristic optimization algorithm used for solving combinatorial optimization problems. In this implementation, the algorithm is applied to solve a specific problem involving a matrix and a set of candidate lists.

Problem Description
The problem consists of a matrix of size 5x5 with certain constraints. The lower triangle half of the matrix should be set to zero. The algorithm aims to find the best solution by performing swaps on the upper triangle half of the matrix. It uses a list of candidate solutions, where each candidate solution is represented as a pair of indices in the matrix and an objective function value.

Getting Started
Clone this repository to your local machine or download the Python script.

Make sure you have Python installed on your system.

Run the Python script using any Python interpreter or IDE.

How to Use
The script starts by initializing the matrix and the candidate list.

The generate_candidate_lists function generates the candidate lists with random values.

The sort_candidate_lists function sorts the candidate lists based on their objective function values.

The main function Tabu_Search performs the Tabu Search algorithm on the candidate lists. It updates the matrix and swaps elements to find the best solution. The best objective function value found during the search is printed.

The Print_Matrix_Half function displays the upper triangle half of the matrix.

The Print_Matrix_Full function displays the full matrix.

Customization
You can customize the initial matrix, candidate list size, and other parameters to experiment with different instances of the problem. Modify the parameters in the script and re-run it to see different results.

Important Note
Please note that this implementation might not be fully optimized and may require further modifications or improvements for specific use cases or larger problem sizes.

Contributing
If you find any issues or want to contribute to this project, feel free to create a pull request or open an issue on the GitHub repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This implementation is based on the Tabu Search algorithm.
The script uses the Python random module for generating random values.
Authors
Bouchana Hicham
