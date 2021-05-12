caseChart()
    .then(response => {
        console.log('Fetched Chart')
    })
    .catch(error => {
        console.log('error!')
        console.log(error)
    })

async function caseChart(){
    // Wait for the data to load before showing chart
    const data = await getData()
    const ctx = document.getElementById('chart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.date,
            datasets: [{
                label: 'COVID-19 Cases by Date in the United States',
                data: data.new_cases,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                }
            }
        }
    });
}