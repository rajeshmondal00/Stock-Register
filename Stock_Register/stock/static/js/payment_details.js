async function searchPaymentDetails() {
  const startDate = document.getElementById("start-date").value;
  const endDate = document.getElementById("end-date").value;

  if (!startDate || !endDate) {
    alert("Please select both start and end dates.");
    return;
  }

  try {
    const response = await fetch(
      `/get-payment-history/?start_date=${startDate}&end_date=${endDate}`
    );
    const data = await response.json();
    const tableBody = document
      .getElementById("payment-table")
      .querySelector("tbody");
    tableBody.innerHTML = "";

    if (data.payment_data && data.payment_data.length > 0) {
      data.payment_data.forEach((payment) => {
        const row = document.createElement("tr");
        row.innerHTML = `
                        <td>${payment.date}</td>
                        <td>${payment.supplier_name}</td>
                        <td>$${payment.amount}</td>
                        <td>${payment.payment_method}</td>
                    `;
        tableBody.appendChild(row);
      });
    } else {
      tableBody.innerHTML =
        '<tr><td colspan="4" style="text-align: center;">No data found for the selected range.</td></tr>';
    }
  } catch (error) {
    console.error("Error fetching payment details:", error);
    alert("Failed to fetch payment history.");
  }
}
