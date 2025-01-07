function toggleProductInput(event) {
  const selectedOption = event.target.options[event.target.selectedIndex];
  const supplierId = selectedOption.getAttribute("data-id");
  const productNameSelect = document.getElementById("productName");
  const customProductInput = document.getElementById("customProductName");
  const priceInput = document.getElementById("price");
  const selectedProduct = productNameSelect.value;
  if (selectedProduct === "other") {
    customProductInput.style.display = "block";
    priceInput.value = ""; // Clear the price field for custom product
  } else {
    customProductInput.style.display = "none";
    fetch(`/get-product-price/?product_id=${supplierId}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.price) {
          priceInput.value = data.price; // Set the price from the backend
        } else {
          priceInput.value = ""; // Clear the field if no price is returned
          alert(data.error || "Unable to fetch price");
        }
      })
      .catch((error) => {
        console.error("Error fetching product price:", error);
        alert("Failed to fetch product price.");
      });
  }

  // fetch('/get-products/')
  // .then(response => response.json())
  // .then(data => {
  //     const productSelect = document.getElementById('productName');
  //     data.forEach(product => {
  //         const option = document.createElement('option');
  //         option.value = product.id;
  //         option.textContent = product.name;
  //         productSelect.appendChild(option);
  //     });
  // })
  // .catch(error => console.error('Error fetching products:', error));
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

function togglePaymentInput() {}

function addStockForm(value) {
  const form = document.getElementById("addStockForm");
  const formData = new FormData(form); // Collect form data
  const feedbackMessage = document.getElementById("feedbackMessage");
  // formData.append('supplier_id',value);
  console.log(value);
  console.log(formData);
  // fetch("/add-stock/", {
  //   method: "POST",
  //   body: formData,
  //   headers: {
  //     "X-CSRFToken": getCookie("csrftoken"), // Include CSRF token
  //   },
  // })
  
  //   .then((response) => response.json())
  //   .then((data) => {
  //     if (data.success) {
  //       feedbackMessage.textContent = data.message; // Show success message
  //       feedbackMessage.style.color = "green";
  //       form.reset(); // Reset form on success
  //     } else {
  //       feedbackMessage.textContent = data.message || "Failed to add stock";
  //       feedbackMessage.style.color = "red";
  //     }
  //   })
  //   .catch((error) => {
  //     console.error("Error:", error);
  //     feedbackMessage.textContent = "An error occurred. Please try again.";
  //     feedbackMessage.style.color = "red";
  //   });
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
