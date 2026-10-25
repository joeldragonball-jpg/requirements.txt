/* Service worker de Mi Cerebro (móvil): la app abre al instante desde la caché y se actualiza sola en segundo plano
   (estrategia «caché primero, red después»). Solo toca archivos del propio sitio; las noticias y los precios en vivo van por red. */
const V = "cerebro-movil-6";
const BASE = ["./", "index.html", "manifest.webmanifest", "assets/icono-192.png", "assets/icono-180.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(V).then(c => c.addAll(BASE)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const r = e.request;
  if (r.method !== "GET" || new URL(r.url).origin !== location.origin) return;
  e.respondWith(caches.open(V).then(async c => {
    const guardado = await c.match(r, { ignoreSearch: true });
    const red = fetch(r).then(res => { if (res.ok) c.put(r, res.clone()); return res; }).catch(() => guardado);
    return guardado || red;
  }));
});
