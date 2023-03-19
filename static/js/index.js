window.onload = () => {
    // js makes request to server carrying the inner content of the searchbar in order to filter the table view
    const searchbar = document.querySelector('#searchbar')
    searchbar.onkeyup = (event) => {
        let searchbarVal = event.target.value
        fetch("/filter?" +  new URLSearchParams({
            searchbar_val: searchbarVal
        }), {
            method: "GET"
        })
        .then(response => {
            return response.text();
        })
        .then(html => {
            const tableBody = document.querySelector('#tableBody')
            tableBody.innerHTML = html
        })
    }
    // displaying the name of the file to be uploaded
    const dataInput = document.querySelector('#data');
    const fileChosen = document.querySelector('#file-chosen');
    dataInput.onchange = () => {
        fileChosen.textContent = dataInput.files[0].name
    }
}