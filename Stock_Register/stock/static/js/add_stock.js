function toggleProductInput(event) {
  const selectedOption = event.target.options[event.target.selectedIndex];
  const productId = selectedOption.getAttribute("data_id");
  const productNameSelect = document.getElementById("productName");
  const customProductInput = document.getElementById("customProductName");
  const priceInput = document.getElementById("price");
  const weightInput = document.getElementById("Weight");
  const selectedProduct = productNameSelect.value;
  if (selectedProduct === "other") {
    customProductInput.style.display = "block";
    priceInput.value = ""; // Clear the price field for custom product
    weightInput.value = ""; // Clear the weight field for custom product
  } else {
    customProductInput.style.display = "none";
    fetch(`/get-product-price/?product_id=${productId}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.price && data.weight) {
          priceInput.value = data.price; // Set the price from the backend
          weightInput.value = data.weight; // Set the weight from the backend
        } else {
          priceInput.value = ""; // Clear the field if no price is returned
          alert(data.error || "Unable to fetch price");
          weightInput.value = ""; // Clear the field if no weight is returned
          alert(data.error || "Unable to fetch weight");
        }
      })
      .catch((error) => {
        console.error("Error fetching product price:", error);
        alert("Failed to fetch product price.");
      });
  }

}

function toggleBuyerInput() {
  const productBuyerSelect = document.getElementById("buyerName");
  const BuyerProductInput = document.getElementById("customBuyerName");

  if (productBuyerSelect.value === "other") {
    BuyerProductInput.style.display = "block";
  } else {
    BuyerProductInput.style.display = "none";
  }
}

function togglePaymentInput() {
  const paymentType = document.getElementById("paymentMethod");
  const paymentValueInput = document.getElementById("paymentValue");
  const paymentTypeValue = paymentType.value;
  if(paymentTypeValue === "online" || paymentTypeValue === "cash"){
    paymentValueInput.style.display = "block";
  }else{
    paymentValueInput.style.display = "none";
  }
}

function addStockForm() {
  const form = document.getElementById("addStockForm");
  const formData = new FormData(form); // Collect form data
  const buyerNameElement = document.getElementById("buyerName");
  const selectedBuyerOption = buyerNameElement.options[buyerNameElement.selectedIndex];
  const productNameElement = document.getElementById("productName");
  const selectedOption = productNameElement.options[productNameElement.selectedIndex];
  const productId = selectedOption.getAttribute("data_id")
  const supplierId = selectedBuyerOption.id; // Get the selected option's ID
  const feedbackMessage = document.getElementById("feedbackMessage");
  formData.append('supplier_id', supplierId);
  formData.append('product_id', productId);

  fetch("/add-stocks/", {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": getCookie("csrftoken"), // Include CSRF token
    },
  })
  
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        feedbackMessage.textContent = data.message; // Show success message
        feedbackMessage.style.color = "green";
        form.reset(); // Reset form on success
      } else {
        feedbackMessage.textContent = data.message || "Failed to add stock";
        feedbackMessage.style.color = "red";
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      feedbackMessage.textContent = "An error occurred. Please try again.";
      feedbackMessage.style.color = "red";
    });
}

// Utility function to get CSRF token from cookies
function getCookie(name) {
  const cookies = document.cookie.split(";");
  for (let cookie of cookies) {
    const [key, value] = cookie.trim().split("=");
    if (key === name) return decodeURIComponent(value);
  }
  return null;
}
