document.getElementById('certificate-form').addEventListener('submit', function (e) {
    const name = document.getElementById('name').value.trim();
    const organization = document.getElementById('organization').value.trim();
    const course = document.getElementById('course').value.trim();
  
    if (name === '' || organization === '' || course === '') {
      e.preventDefault();
      alert('Please fill out all fields!');
    }
  });
  