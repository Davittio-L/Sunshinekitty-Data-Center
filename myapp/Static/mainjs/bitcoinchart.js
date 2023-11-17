document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById("bitcoinChart").getContext('2d');
    let bitcoinChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Bitcoin Price (USD)',
                data: [],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });

    function updateBitcoinChart(price, time) {
        bitcoinChart.data.labels.push(time);
        bitcoinChart.data.datasets.forEach((dataset) => {
            dataset.data.push(price);
        });
        bitcoinChart.update();
    }

    function fetchBitcoinPrice() {
        fetch('bitcoin-price/')
            .then(response => response.json())
            .then(data => {
                const price = data.price;
                const time = new Date().toLocaleTimeString();
                updateBitcoinChart(price, time);
            });
    }

    setInterval(fetchBitcoinPrice, 60000);
});