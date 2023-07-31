# Tabu Search Algorithm for Matrix Optimization

This Python project implements the Tabu Search algorithm to optimize a square matrix. The main objective is to find the best upper triangle half of the matrix through swaps while adhering to certain constraints.

## Problem Description

The matrix is initialized as a 5x5 square matrix with the lower triangle half set to zero. The algorithm aims to find the best solution by performing swaps on the upper triangle half of the matrix. The optimization process is based on a set of candidate lists, where each candidate list contains pairs of indices and their corresponding objective function values.

## Functions

- `generate_candidate_lists(num_lists, list_size)`: Generates `num_lists` random candidate lists, each containing `list_size` pairs of indices and their corresponding objective function values.

- `sort_candidate_lists(candidate_lists)`: Sorts the `candidate_lists` based on their objective function values in descending order.

- `Print_Matrix_Half()`: Displays the upper triangle half of the matrix.

- `Candidate_List_Generator(i)`: Generates predefined candidate lists based on the iteration index `i` in `Tabu_Search_HardCoded.py`.

- `Reduce_Matrix()`: Reduces the value in all matrix indexes by 1 (-1).

- `Swap(First_Number, Second_Number)`: Swaps two elements in the `Init_Solution` list.

- `Pick_Our_Best_Candidate(i, j)`: Picks the best candidate from the predefined candidate lists for each iteration in `Tabu_Search_HardCoded.py`.

- `Check(Iteration, Participant, Obj_Func, Best_Obj_Func)`: Checks if the best pick is already in the tabu storage and applies the aspiration criterion if necessary.

- `Check_Life_Period(matrix)`: Checks if any candidate in the tabu list has a dead life period in the matrix.

- `Tabu_Search(Obj_Func, Init_Solution)`: Implements the Tabu Search algorithm using the generated or predefined candidate lists. It updates the matrix and performs swaps to find the best solution, while also considering tabu restrictions to avoid repeated solutions.

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

The implementation is based on the Tabu Search algorithm, a metaheuristic optimization technique.
The script uses the Python random module for generating random values.

## Author

**Bouchana Hicham**
