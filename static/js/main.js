
function get_data() {
    fetch('/hola/mundo')
        .then(res => res.json())
        .then(res => console.log(res))
}