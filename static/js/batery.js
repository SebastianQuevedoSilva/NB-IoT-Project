function obtenerDatosBateria() {
    // Realiza una solicitud Ajax para obtener datos de batería desde Flask
    // Ajusta la URL de la solicitud según tu configuración Flask
    fetch('/batery')
        .then(response => response.json())
        .then(data => {
            // Formatea los datos para el gráfico de batería
            const labels = data.map(entry => entry.timestamp);
            const valores = data.map(entry => entry.bateria);

            // Renderiza el gráfico de batería
            renderizarGrafico('Batería', labels, valores);
        })
        .catch(error => console.error('Error al obtener datos de batería:', error));
}

// Llama a la función para obtener y mostrar los datos de batería
obtenerDatosBateria();
