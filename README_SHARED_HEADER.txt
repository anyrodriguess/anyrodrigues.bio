SHARED HEADER — WEBSITE UPDATE

All HTML pages now load the same header from header.html.
Edit header.html to change the site title, subtitle or navigation links.
Edit shared-header.css to change the header design.
shared-header.js loads it and marks the active navigation item.

IMPORTANT: The shared header uses fetch(), which works on GitHub Pages
and when using a local web server, but not by double-clicking an HTML file
from your computer (file://). For local preview, run:
    python -m http.server 8000
Then visit http://localhost:8000/

Upload all HTML, CSS and JS files together to the same GitHub Pages folder.
Keep existing CV, images and other assets in the repository.
