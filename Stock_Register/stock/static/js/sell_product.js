function toggleProductInput() {
    const productNameSelect = document.getElementById('productName');
    const customProductInput = document.getElementById('customProductName');
    const priceInput = document.getElementById('price');
    const selectedProduct = productNameSelect.value;
    if (selectedProduct === 'other') {
        customProductInput.style.display = 'block';
        priceInput.value = ''; // Clear the price field for custom product
    } else {
        customProductInput.style.display = 'none';
        fetch(`/get-product-price/?product_id=${selectedProduct}`)
            .then(response => response.json())
            .then(data => {
                if (data.price) {
                    priceInput.value = data.price; // Set the price from the backend
                } else {
                    priceInput.value = ''; // Clear the field if no price is returned
                    alert(data.error || 'Unable to fetch price');
                }
            })
            .catch(error => {
                console.error('Error fetching product price:', error);
                alert('Failed to fetch product price.');
            });
    }
    
    fetch('/get-products/')
    .then(response => response.json())
    .then(data => {
        const productSelect = document.getElementById('productName');
        data.forEach(product => {
            const option = document.createElement('option');
            option.value = product.id;
            option.textContent = product.name;
            productSelect.appendChild(option);
        });
    })
    .catch(error => console.error('Error fetching products:', error));
}


