// Código JavaScript para el gráfico de ppm
function obtenerDatosPPM() {
    // Realiza una solicitud Ajax para obtener datos de ppm desde Flask
    // Ajusta la URL de la solicitud según tu configuración Flask
    fetch('/ppm')
        .then(response => response.json())
        .then(data => {
            // Formatea los datos para el gráfico de ppm
            const labels = data.map(entry => entry.timestamp);
            const valores = data.map(entry => entry.ppm);

            // Renderiza el gráfico de ppm
            renderizarGrafico('PPM', labels, valores);
        })
        .catch(error => console.error('Error al obtener datos de ppm:', error));
}

// Llama a la función para obtener y mostrar los datos de ppm
obtenerDatosPPM();