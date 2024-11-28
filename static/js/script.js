document.getElementById('certificate-form').addEventListener('submit', function (e) {
    const name = document.getElementById('name').value.trim();
    const organization = document.getElementById('organization').value.trim();
    const course = document.getElementById('course').value.trim();
  
    if (name === '' || organization === '' || course === '') {
      e.preventDefault();
      alert('Please fill out all fields!');
    }
  });
  
// Highlight the creator's name on hover
document.querySelector('.footer .name').addEventListener('mouseenter', function () {
    this.style.color = '#0056b3';
  });
  
  document.querySelector('.footer .name').addEventListener('mouseleave', function () {
    this.style.color = '#003366';
  });
  