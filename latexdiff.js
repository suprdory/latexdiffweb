
const button = document.getElementById("go");

button.addEventListener('click',go);

function go() {
    oldtex = document.getElementById('old').value
    newtex = document.getElementById('new').value
    difftex=document.getElementById('diff')
    difftex.value=oldtex+newtex
    
    var url = 'https://meow.suprdory.com:8002/latexdiff'
    const data = {
        oldtex: oldtex,
        newtex: newtex
    };

    fetch(url, {
        method: 'POST', // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });

}


