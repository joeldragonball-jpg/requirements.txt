/* Service worker mínimo: Chrome en Android lo exige para ofrecer "Instalar app". No guarda nada en caché. */
self.addEventListener("install", function () { self.skipWaiting(); });
self.addEventListener("activate", function (e) { e.waitUntil(self.clients.claim()); });
self.addEventListener("fetch", function () {});
