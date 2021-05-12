async function getData(){
    
    // get WHO data
    const response = await fetch('../data/WHO-COVID-19-global-data.csv')
    const data = await response.text()

    // get rows starting with index 1 (no header)
    const table = data.split('\n').slice(1)
    const date = []
    const new_cases = []
    const new_deaths = []
    table.forEach(row => {
        const columns = row.split(',')
        const date_reported = columns[0]
        const new_cases_US = columns[4]
        const new_deaths_US = columns[6]
        date.push(date_reported)
        new_cases.push(new_cases_US)
        new_deaths.push(new_deaths_US)

    })
    return {date, new_cases, new_deaths}
}
