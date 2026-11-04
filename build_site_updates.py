from pathlib import Path
import re, shutil
ROOT=Path(__file__).resolve().parent
NAV='<nav aria-label="Main navigation" class="main-nav"><a href="index.html">HOME</a><a href="about-me.html">ABOUT</a><a href="research.html">RESEARCH</a><a href="projects.html">PROJECTS</a><a href="Any_Rodrigues_CV.pdf" rel="noopener" target="_blank">CV</a><a href="mailto:anycgrodrigues@gmail.com">CONTACT</a></nav>'
SECTION='''\n<section id="featured-projects" class="featured-projects" aria-labelledby="featured-projects-title" style="margin:1.5rem 0;padding:1.25rem;background:#fff;border:2px solid #1c355d;box-shadow:5px 5px 0 #c4d3e6">\n  <div style="font:700 .8rem monospace;color:#2863ae">PROJECTS / IN DEVELOPMENT</div>\n  <h2 id="featured-projects-title">Independent research projects</h2>\n  <p>Computational studies and experimental proposals exploring how living neuronal networks might process information and act on it. Simulated results are identified as such.</p>\n  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem">\n    <article style="padding:1rem;border:1px solid #b8cbe4;background:#edf4fd"><h3>NeuroDose</h3><p>Closed-loop organoid-based decision-making for a simulated Dravet syndrome pharmacology study.</p><a href="neurodose.html">Explore NeuroDose →</a></article>\n    <article style="padding:1rem;border:1px solid #b8cbe4;background:#edf4fd"><h3>NeuroTouch</h3><p>Texture encoding, classification and generalization using real tactile recordings and simulated neuronal networks.</p><a href="neurotouch.html">Explore NeuroTouch →</a></article>\n  </div>\n  <p><a href="projects.html">View all projects →</a></p>\n</section>\n'''

def patch(text, is_index=False):
    if re.search(r'<nav\b[^>]*class=["\'][^"\']*main-nav',text,re.I):
        text=re.sub(r'<nav\b[^>]*class=["\'][^"\']*main-nav[^>]*>.*?</nav>',NAV,text,count=1,flags=re.I|re.S)
    if is_index and 'id="featured-projects"' not in text:
        if '</main>' in text: text=text.replace('</main>',SECTION+'</main>',1)
        elif '</body>' in text: text=text.replace('</body>',SECTION+'</body>',1)
    return text

# Run in the directory containing your existing website files; updates all HTML pages.
def apply_to_site(directory):
    directory=Path(directory)
    changed=[]
    for f in directory.glob('*.html'):
        if f.name in ('projects.html','neurodose.html','neurotouch.html'): continue
        original=f.read_text(encoding='utf-8')
        updated=patch(original, f.name=='index.html')
        if updated!=original:
            f.write_text(updated,encoding='utf-8');changed.append(f.name)
    return changed

if __name__=='__main__':
    print('Updated:', ', '.join(apply_to_site(ROOT)) or 'No existing site pages found')
