const urlParams = new URLSearchParams(window.location.search);
const name = urlParams.get('name');
    if (name) {
    document.getElementById('name').value = name;
    }

document.getElementById("dateOfBirth").value = "2000-01-01";
document.getElementById("dateOfDeath").value = new Date().toISOString().slice(0,10)
