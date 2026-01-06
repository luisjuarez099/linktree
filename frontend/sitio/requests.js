function cargarClientes() {
    fetch("/api/clientes")
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent =
                JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error("Error:", error);
        });
}