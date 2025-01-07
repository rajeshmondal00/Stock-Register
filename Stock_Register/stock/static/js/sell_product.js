function toggleProductInput(event) {
    const selectedOption = event.target.options[event.target.selectedIndex];
    const productId = selectedOption.getAttribute("data-id");
    const productNameSelect = document.getElementById('productName');
    const customProductInput = document.getElementById('customProductName');
    const priceInput = document.getElementById('price');
    const selectedProduct = productNameSelect.value;
    const weightInput = document.getElementById("Weight");
    if (selectedProduct === 'other') {
        customProductInput.style.display = 'block';
        priceInput.value = ''; // Clear the price field for custom product
        weightInput.value = ""; // Clear the weight field for custom product
    } else {
        customProductInput.style.display = 'none';
        fetch(`/get-product-price/?product_id=${productId}`)
            .then(response => response.json())
            .then(data => {
                if (data.price && data.weight) {
                    priceInput.value = data.price; // Set the price from the backend
                    weightInput.value = data.weight; // Set the weight from the backend
                } else {
                    priceInput.value = ''; // Clear the field if no price is returned
                    alert(data.error || 'Unable to fetch price');
                    weightInput.value = ""; // Clear the field if no weight is returned
                    alert(data.error || "Unable to fetch weight");
                }
            })
            .catch(error => {
                console.error('Error fetching product price:', error);
                alert('Failed to fetch product price.');
            });
    }
    
}


function sellProductForm(){

}