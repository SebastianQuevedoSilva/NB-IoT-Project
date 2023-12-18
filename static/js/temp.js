// Código JavaScript para el gráfico de temperatura
function obtenerDatosTemperatura() {
    // Realiza una solicitud Ajax para obtener datos de temperatura desde Flask
    // Ajusta la URL de la solicitud según tu configuración Flask
    fetch('/temperatura')
        .then(response => response.json())
        .then(data => {
            // Formatea los datos para el gráfico de temperatura
            const labels = data.map(entry => entry.timestamp);
            const valores = data.map(entry => entry.temperatura);

            // Renderiza el gráfico de temperatura
            renderizarGrafico('Temperatura', labels, valores);
        })
        .catch(error => console.error('Error al obtener datos de temperatura:', error));
}

// Llama a la función para obtener y mostrar los datos de temperatura
obtenerDatosTemperatura();
