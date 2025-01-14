document
  .getElementById("payment-form")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
      const csrfToken = getCookie("csrftoken"); // Function to get the CSRF token from cookies

      const response = await fetch("/payments/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken, // Add CSRF token to headers
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        alert("Payment details added successfully!");
        event.target.reset();
      } else {
        const errorData = await response.json();
        alert(`Error: ${errorData.message}`);
      }
    } catch (error) {
      alert("An error occurred while submitting the payment details.");
      console.error(error);
    }
    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [key, value] = cookie.trim().split('=');
            if (key === name) {
                return decodeURIComponent(value);
            }
        }
        return null;
    }
    
  });
