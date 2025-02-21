const movieList = document.getElementById('movieList');

fetch('http://localhost:5000/movies') // Makes the call
    .then(response => response.json()) // Converts the response to JSON
    .then(data => {
        data.forEach(movie => {
            const li = document.createElement('li');
            li.textContent = movie.title;
            movieList.appendChild(li);
        })
})
    .catch(error => {
        console.error('Error:', error)
    });