# Tabu Search Algorithm for Matrix Optimization

This Python script implements the Tabu Search algorithm to optimize a square matrix. The main objective is to find the best upper triangle half of the matrix through swaps while adhering to certain constraints.

## Problem Description

The matrix is initialized as a 5x5 square matrix with the lower triangle half set to zero. The algorithm aims to find the best solution by performing swaps on the upper triangle half of the matrix. The optimization process is based on a set of candidate lists, where each candidate list contains pairs of indices and their corresponding objective function values.

## Functions

- `generate_candidate_lists`: Generates random candidate lists containing pairs of indices and objective function values.

- `sort_candidate_lists`: Sorts the candidate lists based on their objective function values in descending order.

- `Tabu_Search`: Implements the Tabu Search algorithm using the generated candidate lists. It updates the matrix and performs swaps to find the best solution, while also considering tabu restrictions to avoid repeated solutions.

- `Print_Matrix_Half`: Displays the upper triangle half of the matrix.

## Usage

1. Clone the repository or download the Python script.

2. Run the script using any Python interpreter or IDE.

3. The script will initialize the matrix, generate candidate lists, and perform the Tabu Search optimization.

## Customization

You can modify the initial matrix, candidate list size, or other parameters to experiment with different instances of the problem. The provided candidate lists can also be replaced with custom ones for specific use cases.

## Note

The implementation is designed for educational purposes and may require further optimization or modifications for more complex scenarios.

## Contributing

Feel free to contribute to this project by creating pull requests or opening issues on the GitHub repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- The implementation is based on the Tabu Search algorithm, a metaheuristic optimization technique.
- The script uses the Python `random` module for generating random values.

## Author

Bouchana Hicham
