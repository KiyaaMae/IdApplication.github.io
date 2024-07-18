// validation.js
function validateForm() {
    const form = document.getElementById('application-form');
    const studentNumberInput = document.getElementById('student-number');
    const studentNumberValue = studentNumberInput.value.trim();
    const fields = form.querySelectorAll('input[required], textarea[required]');
    let isValid = true;

    fields.forEach(field => {
        if (!field.value.trim()) {
            alert('Please answer the required fields');
            isValid = false;
            return false;
        }
    });

    const studentNumber = document.getElementById('student-number').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;

    const studentNumberPattern = /^\d{4}-\d{5}-[A-Z]{2}-\d$/;
    const phonePattern = /^\+63\d{10}$/;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!studentNumberPattern.test(studentNumber)) {
        alert('Please follow the specified format for Student Number (YYYY-XXXXX-XX-X).');
        return false;
    }

    if (studentNumberValue === '2021-10268-MN-0') {
        alert('Student number already entered. Please try again.');
        return false;
    }

    if (!phonePattern.test(phone)) {
        alert('Please follow the specified format for Phone/Mobile Number (+63XXXXXXXXXX).');
        return false;
    }

    if (!emailPattern.test(email)) {
        alert('Please follow the specified format for Email Address (example@email.com).');
        return false;
    }

    if (isValid) {
        return confirm('Do you want to confirm application?');
    }

    return false;
}

function confirmCancel() {
    return confirm('Are you sure you want to cancel?');
}


