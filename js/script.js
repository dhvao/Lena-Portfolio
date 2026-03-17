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
  '.proj-sub-heading, .proj-main-title, .proj-section-heading'
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

/* ── Product gallery lightbox ────────────────────── */
(function () {
  const overlay  = document.getElementById('gallery-overlay');
  const content  = document.getElementById('gallery-content');
  const closeBtn = overlay.querySelector('.gallery-close');

  function open(sections) {
    content.innerHTML = '';

    // Tab bar (only shown when multiple sections)
    if (sections.length > 1) {
      const tabs = document.createElement('div');
      tabs.className = 'gallery-tabs';
      sections.forEach((section, i) => {
        const tab = document.createElement('button');
        tab.className = 'gallery-tab' + (i === 0 ? ' is-active' : '');
        tab.textContent = section.label;
        tab.addEventListener('click', () => showSection(i));
        tabs.appendChild(tab);
      });
      content.appendChild(tabs);
    }

    // Section panels
    sections.forEach((section, i) => {
      const panel = document.createElement('div');
      panel.className = 'gallery-panel' + (i === 0 ? ' is-active' : '');

      const grid = document.createElement('div');
      grid.className = 'gallery-collage';
      section.images.forEach(src => {
        const img = document.createElement('img');
        img.src = src;
        img.alt = section.label;
        grid.appendChild(img);
      });
      panel.appendChild(grid);
      content.appendChild(panel);
    });

    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden', 'false');
  }

  function showSection(index) {
    content.querySelectorAll('.gallery-tab').forEach((t, i) =>
      t.classList.toggle('is-active', i === index));
    content.querySelectorAll('.gallery-panel').forEach((p, i) =>
      p.classList.toggle('is-active', i === index));
    overlay.querySelector('.gallery-scroll').scrollTop = 0;
  }

  function close() {
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
  }

  document.querySelectorAll('.showcase-cta[data-gallery]').forEach(btn => {
    btn.addEventListener('click', () => {
      const raw = btn.dataset.gallery.trim();
      if (!raw) return;
      try {
        const sections = JSON.parse(raw);
        open(sections);
      } catch (e) {}
    });
  });

  closeBtn.addEventListener('click', close);
  overlay.addEventListener('click', e => { if (e.target === overlay) close(); });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') close();
  });
}());

/* ── 3D model — oscillating rotation (no full 360) ── */
function animateModel(id, speed, swing, phi, direction, thetaOffset = 0, radius = 'auto') {
  const mv = document.getElementById(id);
  if (!mv) return;
  mv.addEventListener('load', () => {
    let startTime = null;
    function tick(now) {
      if (!startTime) startTime = now;
      const t = (now - startTime) / 1000;
      const theta = thetaOffset + Math.sin(t * speed) * swing * direction;
      mv.cameraOrbit = `${theta}deg ${phi}deg ${radius}`;
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  });
}

// id, speed, swing°, phi°, direction (1=normal, -1=reversed)
animateModel('mv-product-01', 0.45, 38, 75,  1);
animateModel('mv-product-02', 0.75, 30, 80, -1);
animateModel('mv-product-03', 0.60, 45, 70,  1);
animateModel('mv-jaguar',     0.55, 30, 90,  1, -90);

/* ── Passenger Journey Roadmap ───────────────────── */
(function () {
  const svg  = document.getElementById('roadmapSvg');
  if (!svg) return;

  const path  = document.getElementById('roadmapPath');
  const nodes = svg.querySelectorAll('.rm-node');

  // Waypoints: fraction of path drawn when each node should appear
  const waypoints = [0, 0.125, 0.25, 0.375, 0.50, 0.625, 0.75, 0.875, 1.0];
  const shown = new Array(nodes.length).fill(false);
  let started = false;

  function easeInOut(t) {
    return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
  }

  function run() {
    if (started) return;
    started = true;

    const total    = path.getTotalLength();
    const duration = 4800;
    path.style.strokeDasharray  = total;
    path.style.strokeDashoffset = total;

    let start = null;
    function frame(now) {
      if (!start) start = now;
      const raw     = Math.min((now - start) / duration, 1);
      const eased   = easeInOut(raw);

      path.style.strokeDashoffset = total * (1 - eased);

      waypoints.forEach((wp, i) => {
        if (!shown[i] && eased >= wp) {
          shown[i] = true;
          nodes[i].classList.add('visible');
        }
      });

      if (raw < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) run(); });
  }, { threshold: 0.15 }).observe(svg);
}());

/* ── Packaging lightbox ──────────────────────────── */
(function () {
  const thumbs   = Array.from(document.querySelectorAll('.pkg-thumb'));
  const lightbox = document.getElementById('pkg-lightbox');
  const img      = document.getElementById('pkg-lb-img');
  if (!thumbs.length || !lightbox) return;

  const srcs = thumbs.map(t => t.src);
  let current = 0;

  function show(index) {
    current = (index + srcs.length) % srcs.length;
    img.src = srcs[current];
    lightbox.classList.add('is-open');
    lightbox.setAttribute('aria-hidden', 'false');
  }

  function close() {
    lightbox.classList.remove('is-open');
    lightbox.setAttribute('aria-hidden', 'true');
  }

  thumbs.forEach((t, i) => t.addEventListener('click', () => show(i)));

  lightbox.querySelector('.pkg-lb-close').addEventListener('click', close);
  lightbox.querySelector('.pkg-lb-prev').addEventListener('click', () => show(current - 1));
  lightbox.querySelector('.pkg-lb-next').addEventListener('click', () => show(current + 1));

  lightbox.addEventListener('click', e => { if (e.target === lightbox) close(); });

  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('is-open')) return;
    if (e.key === 'Escape')      close();
    if (e.key === 'ArrowLeft')   show(current - 1);
    if (e.key === 'ArrowRight')  show(current + 1);
  });
}());
