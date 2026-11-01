// Load the same header on every page.
document.addEventListener('DOMContentLoaded', function () {
  var place = document.getElementById('shared-header');
  if (!place) return;
  fetch('header.html')
    .then(function (response) {
      if (!response.ok) throw new Error('Header could not load');
      return response.text();
    })
    .then(function (html) {
      place.innerHTML = html;
      var page = window.location.pathname.split('/').pop() || 'index.html';
      var section = ['neurodose.html', 'neurotouch.html'].includes(page) ? 'projects.html' : page;
      place.querySelectorAll('.main-nav a').forEach(function (link) {
        if (link.getAttribute('href') === section) link.setAttribute('aria-current', 'page');
      });
    })
    .catch(function () {
      place.innerHTML = '<p><a href="index.html">HOME</a> · <a href="projects.html">PROJECTS</a></p>';
    });
});
