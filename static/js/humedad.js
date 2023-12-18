function obtenerDatosHumedad() {
    // Realiza una solicitud Ajax para obtener datos de humedad desde Flask
    // Ajusta la URL de la solicitud según tu configuración Flask
    fetch('/humedad')
        .then(response => response.json())
        .then(data => {
            // Formatea los datos para el gráfico de humedad
            const labels = data.map(entry => entry.timestamp);
            const valores = data.map(entry => entry.humedad);

            // Renderiza el gráfico de humedad
            renderizarGrafico('Humedad', labels, valores);
        })
        .catch(error => console.error('Error al obtener datos de humedad:', error));
}

// Llama a la función para obtener y mostrar los datos de humedad
obtenerDatosHumedad();