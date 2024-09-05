# Star Wars Movie Characters (Node.js)

This project is a Node.js script that fetches and displays all characters from a specified Star Wars movie using the [Star Wars API (SWAPI)](https://swapi-api.alx-tools.com/).

## Prerequisites

1. Node.js installed (v12 or higher)
2. `axios` module installed

### Installation

1. Clone or download this repository.
2. Navigate to the project directory and install dependencies:

   ```bash
   npm install axios
   ```

### Usage

Run the script from the command line, passing the movie ID as the first argument.

#### Example

To display the characters from **"Return of the Jedi"** (movie ID: 3):

```bash
node star_wars_characters.js 3
```

This will print the names of all characters in the movie **"Return of the Jedi"**.

### Movie IDs

- **1**: The Phantom Menace
- **2**: Attack of the Clones
- **3**: Return of the Jedi
- **4**: A New Hope
- **5**: The Empire Strikes Back
- **6**: Revenge of the Sith
- **7**: The Force Awakens

### Example Output

```bash
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
```

### Error Handling

If an invalid movie ID is passed, the script will display an error message indicating the issue with fetching the movie or character data.
