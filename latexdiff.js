
const button = document.getElementById("go");

button.addEventListener('click',go);
difftex = document.getElementById('diff')
function go() {
    oldtex = document.getElementById('old').value
    newtex = document.getElementById('new').value
    
    // difftex.value=oldtex+newtex
    
    var url = 'https://meow.suprdory.com:8002/latexdiff'
    const indata = {
        oldtex: oldtex,
        newtex: newtex,
    };
    // console.log(data)
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(indata),
    })
        .then(response => response.json())
        .then(data => updateDoc(data))
        .catch((error) => {
            console.error('Error:', error)
        });
}
function updateDoc(data){
    console.log(data)
    difftex.value=data.text
}


