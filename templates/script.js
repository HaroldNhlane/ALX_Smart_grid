// Function to fetch data from the live Django API
async function fetchData() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/sensordata/');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Could not fetch data:", error);
        return [];
    }
}

// Function to make a simple prediction based on the rule (temperature > 35)
function getPrediction(temperature) {
    return temperature > 35 ? 'Failure' : 'Normal';
}

// Function to render the chart using Chart.js
function renderChart(data) {
    // Check if a Chart instance already exists on the canvas and destroy it
    const existingChart = Chart.getChart('temperatureChart');
    if (existingChart) {
        existingChart.destroy();
    }
    
    const ctx = document.getElementById('temperatureChart').getContext('2d');
    
    const timestamps = data.map(item => item.timestamp);
    const temperatures = data.map(item => item.temperature);
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Temperature (°C)',
                data: temperatures,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Timestamp'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Temperature (°C)'
                    }
                }
            }
        }
    });
}

// Function to populate the data table
function populateTable(data) {
    const tableBody = document.getElementById('data-table-body');
    tableBody.innerHTML = ''; // Clear existing data
    
    data.forEach(item => {
        const row = tableBody.insertRow();
        row.innerHTML = `
            <td>${new Date(item.timestamp).toLocaleString()}</td>
            <td>${item.current} A</td>
            <td>${item.temperature} °C</td>
            <td>${item.vibration} m/s²</td>
            <td>${item.voltage} V</td>
        `;
    });
}

// Main function to run the dashboard
async function main() {
    const sensorData = await fetchData();
    
    if (sensorData && sensorData.length > 0) {
        // Get the latest data point
        const latestData = sensorData[sensorData.length - 1];
        
        // Update the prediction status
        const prediction = getPrediction(latestData.temperature);
        const predictionElement = document.getElementById('prediction-status');
        predictionElement.textContent = prediction;
        predictionElement.style.color = prediction === 'Failure' ? 'red' : 'green';
        
        // Update the latest temperature metric
        document.getElementById('latest-temp').textContent = `${latestData.temperature} °C`;
        
        // Render the chart and table
        renderChart(sensorData);
        populateTable(sensorData.slice(-5)); // Show last 5 records
    }
}

// This line is what runs the entire script. It's the most crucial part.
main();