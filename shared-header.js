// This file creates the same header on every page.
// Edit the text or links here once to update the whole website.
const siteHeader = `<div id="global-site-header">
  <header class="universal-site-header">
    <div class="universal-site-identity">
      <h1>ANY RODRIGUES</h1>
      <p>molecular bioengineer / neural interfaces / biological intelligence</p>
    </div>
    <div class="universal-status">
      <strong>STATUS:</strong>
      <span><span class="universal-online-dot"></span> online</span>
    </div>
  </header>
  <nav class="universal-site-nav" aria-label="Main navigation">
    <a href="index.html">HOME</a>
    <a href="about-me.html">ABOUT</a>
    <a href="research.html">RESEARCH</a>
    <a href="projects.html">PROJECTS</a>
    <a href="Any_Rodrigues_CV.pdf" target="_blank" rel="noopener">CV</a>
    <a href="mailto:anycgrodrigues@gmail.com">CONTACT</a>
  </nav>
</div>`;
document.currentScript.insertAdjacentHTML("beforebegin", siteHeader);

const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('#global-site-header .universal-site-nav a').forEach(link => {
  if (link.getAttribute('href') === currentPage) {
    link.setAttribute('aria-current', 'page');
  }
});
