document.getElementById('payment-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/add-payment/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            alert('Payment details added successfully!');
            event.target.reset();
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.message}`);
        }
    } catch (error) {
        alert('An error occurred while submitting the payment details.');
        console.error(error);
    }
});