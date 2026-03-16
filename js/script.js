/* ════════════════════════════════════════════════════
   Lena Eblenkamp — Portfolio 2026
   script.js
════════════════════════════════════════════════════ */

/* ── Smooth scroll for all anchor links ─────────── */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

/* ── Highlight active project in nav on scroll ───── */
const projectSections = document.querySelectorAll('.proj-section');
const navItems = document.querySelectorAll('.pnav-item');

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;

      const id = entry.target.id;
      navItems.forEach(item => {
        const matches = item.getAttribute('href') === `#${id}`;
        item.classList.toggle('is-active', matches);
      });
    });
  },
  {
    threshold: 0.25,
    rootMargin: '0px 0px -20% 0px',
  }
);

projectSections.forEach(section => observer.observe(section));

/* ── Subtle fade-in on scroll for project sections ─ */
const fadeEls = document.querySelectorAll(
  '.proj-section, .proj-sub-heading, .proj-main-title, .proj-section-heading'
);

const fadeObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        fadeObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.08 }
);

fadeEls.forEach(el => {
  el.classList.add('fade-in');
  fadeObserver.observe(el);
});

/* ── Brand Research mind map — floating nodes animation ─ */
(function () {
  const svg = document.getElementById('mmSvg');
  if (!svg) return;

  const nodes      = Array.from(svg.querySelectorAll('.mm-node'));
  const connectors = Array.from(svg.querySelectorAll('.mm-connector'));

  // Parse base positions
  const bases = nodes.map(n => ({
    x: parseFloat(n.dataset.bx),
    y: parseFloat(n.dataset.by)
  }));

  // Set initial transforms
  nodes.forEach((n, i) => n.setAttribute('transform', `translate(${bases[i].x},${bases[i].y})`));

  let startTime = null;
  let rafId     = null;
  let running   = false;

  function tick(now) {
    if (!startTime) startTime = now;
    const t = (now - startTime) / 1000;

    nodes.forEach((node, i) => {
      const phase = (i / nodes.length) * Math.PI * 2;
      const x = bases[i].x + Math.sin(t * 0.38 + phase)       * 13;
      const y = bases[i].y + Math.cos(t * 0.30 + phase * 1.5) * 9;
      node.setAttribute('transform', `translate(${x},${y})`);
      connectors[i].setAttribute('x2', x);
      connectors[i].setAttribute('y2', y);
    });

    if (running) rafId = requestAnimationFrame(tick);
  }

  // Start / pause based on visibility
  const brandMap = document.getElementById('brandMap');
  if (brandMap) {
    new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting && !running) {
          running = true;
          rafId = requestAnimationFrame(tick);
        } else if (!e.isIntersecting && running) {
          running = false;
          cancelAnimationFrame(rafId);
        }
      });
    }, { threshold: 0.1 }).observe(brandMap);
  }
}());

/* ── Skills carousel ─────────────────────────────── */
document.querySelectorAll('.skills-carousel').forEach(carousel => {
  const viewport = carousel.querySelector('.sc-viewport');
  const track    = carousel.querySelector('.sc-track');
  const slides   = carousel.querySelectorAll('.sc-slide');
  const dots     = carousel.querySelectorAll('.sc-dot');
  const prev     = carousel.querySelector('.sc-btn--prev');
  const next     = carousel.querySelector('.sc-btn--next');
  const gap      = 16;
  let current    = 0;

  function updateTrack() {
    const slideW  = slides[0].offsetWidth;
    const vpW     = viewport.offsetWidth;
    const offset  = -(current * (slideW + gap)) + (vpW - slideW) / 2;
    track.style.transform = `translateX(${offset}px)`;
    slides.forEach((s, i) => s.classList.toggle('active', i === current));
    dots.forEach((d, i)   => d.classList.toggle('active', i === current));
  }

  function goTo(n) {
    current = (n + slides.length) % slides.length;
    updateTrack();
  }

  prev.addEventListener('click', () => goTo(current - 1));
  next.addEventListener('click', () => goTo(current + 1));
  dots.forEach((dot, i) => dot.addEventListener('click', () => goTo(i)));
  window.addEventListener('resize', updateTrack);
  updateTrack();
});
