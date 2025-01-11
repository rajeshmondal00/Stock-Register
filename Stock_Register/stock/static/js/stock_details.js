// Search and display product stock data
function searchProductStock() {
    const selectedProductId = document.getElementById("product-select");
    const selectedOption = selectedProductId.options[selectedProductId.selectedIndex];
    const productId = selectedOption.getAttribute("data_id")
    if (!productId) {
        alert('Please select a product.');
        return;
    }else{
        fetch(`/get-stock-details/?product_id=${productId}`)
        .then((Response) => Response.json())
        .then((productData) => {
            const tableBody = document.getElementById('current-stock-table').querySelector('tbody');
            tableBody.innerHTML = '';
        
            if (productData) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${productData.product_name}</td>
                    <td>${productData.quantity}</td>
                    <td>${productData.price}</td>
                    <td>${productData.weight}</td>
                `;
                tableBody.appendChild(row);
            } else {
                tableBody.innerHTML = '<tr><td colspan="5">No data found</td></tr>';
            }

        })
    }

}

function searchProductStockHistory() {
    const selectedProduct = document.getElementById("product-select").value;
    const selectedProductInput = selectedProduct.options[selectedProduct.selectedIndex];
    const productId = selectedProductInput.getAttribute("data_id")
    if (!productId) {
        alert("Please select a product.");
        return;
    }

    fetch(`/get-stock-history/?product_id=${productId}`)
        .then((response) => response.json())
        .then((data) => {
            const stockHistoryTable = document.querySelector("section:nth-of-type(2) table tbody");
            stockHistoryTable.innerHTML = "";

            if (data.history && data.history.length > 0) {
                data.history.forEach((entry) => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${entry.date}</td>
                        <td>${entry.transaction_type}</td>
                        <td>${entry.product_name}</td>
                        <td>${entry.quantity}</td>
                        <td>${entry.price}</td>
                    `;
                    stockHistoryTable.appendChild(row);
                });
            } else {
                stockHistoryTable.innerHTML = "<tr><td colspan='5'>No history available for the selected product.</td></tr>";
            }
        })
        .catch((error) => {
            console.error("Error fetching stock history:", error);
            alert("Failed to fetch stock history.");
        });
}

function downloadExcel(dataType) {
    const urls = {
        product: '/download-product-data/',
        sell: '/download-sell-data/',
        current: '/download-current-stock/'
    };

    if (urls[dataType]) {
        window.location.href = urls[dataType];
    } else {
        alert('Invalid data type selected!');
    }
}