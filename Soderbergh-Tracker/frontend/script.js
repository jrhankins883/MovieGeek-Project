fetch('http://localhost:5000/movies') // Makes the call
    .then(response => response.json()) // Converts the response to JSON
    .then(data => {

    })
    .catch(error => {
        console.error('Error:', error)
    });