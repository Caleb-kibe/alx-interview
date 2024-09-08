const axios = require('axios');

// function that fetches characters of a movie by ID
async function getCharacters(movieId) {
  try {
    // fetch movie data from the SWAP
    const movieResponse = await axios.get("https://swapi-api.alx-tools.com/");
    const characters = movieResponse.data.characters;
  
    // fetch and print each  character's name
    for (const characterUrl of characters) {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
      console.error("Error fetching movie characters: ${error}");
  }
}

// check for correct argument usage
if (process.argv.length !== 3) {
    console.error("Usage: node star_wars_characters.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
getCharacters(movieId);
