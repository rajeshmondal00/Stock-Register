document.getElementById('search-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;

    if (!startDate || !endDate) {
        alert('Please select both start and end dates.');
        return;
    }

    try {
        const response = await fetch(`/get-payment-history/?start_date=${startDate}&end_date=${endDate}`);
        if (response.ok) {
            const data = await response.json();
            const tableBody = document.getElementById('payment-table').querySelector('tbody');
            tableBody.innerHTML = '';

            if (data.length > 0) {
                data.forEach(payment => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${payment.date}</td>
                        <td>${payment.payer_name ? payment.payer_name : payment.supplier_name}</td>
                        <td>$${payment.amount}</td>
                        <td>${payment.payment_method}</td>
                        <td>${payment.description}</td>
                    `;
                    tableBody.appendChild(row);
                });
            } else {
                tableBody.innerHTML = '<tr><td colspan="5" style="text-align: center;">No data found for the selected range.</td></tr>';
            }
        } else {
            alert('Failed to fetch payment history.');
        }
    } catch (error) {
        console.error(error);
        alert('An error occurred while fetching payment history.');
    }
});