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
            const tableBody = document.querySelector('#table-body')
            tableBody.innerHTML = html
        })
    }
    // displaying the name of the file to be uploaded
    const dataInput = document.querySelector('#data');
    const fileChosen = document.querySelector('#file-chosen');
    const fileInputSubmitBtn = document.querySelector('.file-input-submit')
    dataInput.onchange = () => {
        const uploadedFile = dataInput.files[0]
        if (uploadedFile) {
            fileChosen.textContent = uploadedFile.name
            fileInputSubmitBtn.removeAttribute('disabled')
            fileInputSubmitBtn.classList.add('hvr-sweep-to-top');
        }
        else {
            fileInputSubmitBtn.setAttribute('disabled')
            fileInputSubmitBtn.classList.remove('hvr-sweep-to-top');
        }
    }
}