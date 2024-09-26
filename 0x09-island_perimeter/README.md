# Island Perimeter Calculator

## Description

This program contains a function `island_perimeter(grid)` that calculates the perimeter of an island represented by a 2D grid. The grid is composed of 0's (water) and 1's (land). The function returns the perimeter of the island described in the grid.

## Function Specification

### `island_perimeter(grid)`

#### Parameters:
- `grid`: A list of list of integers where:
  - 0 represents water
  - 1 represents land

#### Returns:
- An integer representing the perimeter of the island.

#### Constraints:
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

## Usage

To use this function, import it into your Python script and call it with a valid grid:

```python
from island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

perimeter = island_perimeter(grid)
print(f"The island perimeter is: {perimeter}")
```

## Example

For the grid:
```
[
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

The function will return `12`, as the island's perimeter is 12 units.

## Implementation Details

The function works by iterating through each cell in the grid. When it encounters a land cell (1), it adds 4 to the perimeter (assuming all sides are exposed). It then checks the left and top neighbors of the current cell. If they are also land, it subtracts 2 from the perimeter (because that side is not exposed). This approach avoids double-counting shared sides between land cells.

## Testing

You can test the function using the provided `0-main.py` script:

```bash
./0-main.py
```

This should output `12`, corresponding to the perimeter of the island in the example grid.

## Notes

- The function assumes that the input grid is valid and meets all the specified constraints.
- For an empty grid or a grid with no land cells, the function will return 0.
