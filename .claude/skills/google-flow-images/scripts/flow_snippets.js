// Snippets for mcp__claude-in-chrome__javascript_tool on a Flow project page.
// Paste one block at a time; each returns a JSON-able value. Thresholds (x>980, naturalWidth>=1000)
// match a ~1500px-wide window with the agent panel docked right — re-check with a screenshot.

// --- 1. Idle detection: the agent is busy while a "Stop" button exists. ---
(() => {
  const busy = [...document.querySelectorAll('button')].some(b =>
    /^stop$/i.test((b.getAttribute('aria-label') || '').trim()) ||
    /^stop$/i.test((b.innerText || '').trim()));
  const tail = (document.body.innerText || '').slice(-600);
  const error = /Too many generations|Something went wrong|try again/i.test(tail);
  return { busy, error, tail };
})();

// --- 2. Collect large images: chat panel (x > 980) or whole grid. ---
// Only meaningful on the project view, not /edit/<id>. In the chat panel the last N are the
// newest batch, in prompt order.
((scope = 'chat', lastN = 0) => {
  const imgs = [...document.querySelectorAll('img')].filter(i => {
    if (!i.complete || i.naturalWidth < 1000) return false;
    const r = i.getBoundingClientRect();
    return scope === 'chat' ? r.left > 980 : true;
  });
  const uniq = [...new Map(imgs.map(i => [i.currentSrc || i.src, i])).values()];
  const pick = lastN ? uniq.slice(-lastN) : uniq;
  window.__flowPick = pick.map(i => i.currentSrc || i.src);
  return pick.map((i, k) => ({ k, w: i.naturalWidth, h: i.naturalHeight, alt: i.alt, src: (i.currentSrc || i.src).slice(0, 80) }));
})('chat', 4);

// --- 3. Post picked images to flow_recv.py (python3 flow_recv.py <dir>). ---
// Names are given in prompt order; verify afterwards with flow_match.py / by eye.
(async (names, port = 8765) => {
  const srcs = window.__flowPick || [];
  if (srcs.length !== names.length) return `count mismatch: ${srcs.length} images vs ${names.length} names`;
  const out = [];
  for (let k = 0; k < srcs.length; k++) {
    const blob = await (await fetch(srcs[k], { credentials: 'include' })).blob();
    const ext = blob.type.includes('png') ? 'png' : blob.type.includes('webp') ? 'webp' : 'jpg';
    const r = await fetch(`http://127.0.0.1:${port}/${names[k]}.${ext}`, { method: 'POST', body: blob });
    out.push(`${names[k]}.${ext}: ${r.status} ${blob.size}B`);
  }
  return out;
})(['s01', 's02', 's03', 's04']);

// --- 4. Collection page: scroll the inner scroller to force lazy tiles to load. ---
(async () => {
  const sc = [...document.querySelectorAll('*')]
    .filter(e => e.scrollHeight > e.clientHeight + 50 && /(auto|scroll)/.test(getComputedStyle(e).overflowY))
    .sort((a, b) => b.scrollHeight - a.scrollHeight)[0];
  if (!sc) return 'no scroller';
  let last = -1;
  while (sc.scrollTop !== last) {
    last = sc.scrollTop;
    sc.scrollTop += sc.clientHeight;
    await new Promise(r => setTimeout(r, 800));
  }
  return document.querySelectorAll('img').length + ' imgs loaded';
})();
