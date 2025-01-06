// Populate product dropdown (replace with API call or server data)
const products = [
    { id: 1, name: "Example Product" },
    { id: 2, name: "Another Product" }
];

const productSelect = document.getElementById('product-select');
products.forEach(product => {
    const option = document.createElement('option');
    option.value = product.id;
    option.textContent = product.name;
    productSelect.appendChild(option);
});

// Search and display product stock data
function searchProductStock() {
    const productId = productSelect.value;
    if (!productId) {
        alert('Please select a product.');
        return;
    }

    // Example data; replace with an actual API call
    const stockData = {
        1: { name: "Example Product", quantity: 50, price: 20, category: "Electronics", description: "High-quality electronic product" },
        2: { name: "Another Product", quantity: 30, price: 15, category: "Stationery", description: "Useful stationery item" }
    };

    const productData = stockData[productId];
    const tableBody = document.getElementById('current-stock-table').querySelector('tbody');
    tableBody.innerHTML = '';

    if (productData) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${productData.name}</td>
            <td>${productData.quantity}</td>
            <td>$${productData.price}</td>
            <td>${productData.category}</td>
            <td>${productData.description}</td>
        `;
        tableBody.appendChild(row);
    } else {
        tableBody.innerHTML = '<tr><td colspan="5">No data found</td></tr>';
    }
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