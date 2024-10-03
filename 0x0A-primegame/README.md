# Prime Game

## Description

This project involves creating a Python program to solve a game played between two players, Maria and Ben. The game is played using a set of consecutive integers from 1 to `n`, and the players take turns picking prime numbers and removing those numbers and their multiples from the set. The player who cannot make a move loses the game. Maria always plays first, and both players make optimal moves.

Your task is to determine the winner of each round, given `x` rounds, and to return the player who won the most rounds.

## Concepts Needed

### Prime Numbers
- **Understanding prime numbers**: A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
- **Efficient prime number algorithms**: You will need to check for prime numbers efficiently in each game round.

### Sieve of Eratosthenes
- **Efficient prime number finding**: The Sieve of Eratosthenes is an algorithm for finding all prime numbers up to a given limit. This is crucial for optimizing the solution, especially for large values of `n`.

### Game Theory
- **Optimal play**: Since both players play optimally, understanding how players think in competitive games and choosing the best possible moves is important.
- **Win conditions**: You need to understand the game's structure and how the game ends when no moves are left for a player.

### Dynamic Programming / Memoization
- **Optimization**: Storing the results of previous computations to avoid recalculating primes for each round. This speeds up the algorithm when processing multiple rounds.

## Requirements

- You will use Python3 for implementation, and the solution should adhere to **PEP 8** coding standards.
- The game should be played for up to 10,000 rounds.
- You cannot import any external Python packages.
- You must implement an efficient algorithm for detecting prime numbers and applying game theory principles.

## Usage

The game consists of several rounds, each with a different value of `n` (maximum integer in the set). Your task is to create a function `isWinner(x, nums)` where:
- `x`: Number of rounds.
- `nums`: List of integers where each value represents the upper bound `n` of the set for that round.

You need to return the name of the player who won the most rounds (either "Maria" or "Ben"). If the result is a tie or no winner can be determined, return `None`.

### Example

```python
x = 3
nums = [4, 5, 1]

# In round 1 (n=4), Ben wins.
# In round 2 (n=5), Maria wins.
# In round 3 (n=1), Ben wins.
# Result: Ben wins the most rounds.

print(isWinner(3, [4, 5, 1]))  # Output: "Ben"
```

## How It Works

1. **Prime Number Calculation**: Use the Sieve of Eratosthenes to precompute all prime numbers up to the maximum value of `n` for any round.
2. **Game Simulation**: For each round, simulate the game with Maria and Ben taking turns, removing primes and their multiples, and tracking who wins.
3. **Optimal Play**: Ensure both players play optimally, meaning they make the best move possible at each turn.
4. **Winner Determination**: After all rounds are played, determine the player who has won the most rounds.

## File Structure

- `0-prime_game.py`: Contains the core logic for the `isWinner()` function.
- `README.md`: Documentation for the project.
- `main_0.py`: Example usage and test cases.

## Example Output

```bash
$ ./main_0.py
Winner: Ben
```

## Additional Resources

- [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:algebra-factoring/x2f8bb11595b61c86:introduction-to-prime-numbers)
- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [Game Theory Introduction](https://plato.stanford.edu/entries/game-theory/)
- [Dynamic Programming in Python](https://www.geeksforgeeks.org/dynamic-programming/)

By understanding and applying these concepts, you will be well-equipped to solve the problem efficiently.
