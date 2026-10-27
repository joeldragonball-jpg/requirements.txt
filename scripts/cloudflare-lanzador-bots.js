// Worker de Cloudflare: lanza cada 30 minutos los bots de alertas y de vigilancia on-chain de GitHub Actions.
// Motivo: el cron de GitHub es de «mejor esfuerzo» y en este repo solo se ejecuta cada 2-7 horas.
// Lanza bots SIN IA (alertas.yml, onchain.yml y paneles.yml) y, una vez por hora, noticias.yml (C34): ese solo llama a la API de Anthropic
// cuando toca una franja de envío (8, 13, 18 y 21 h de España), con los topes de noticias/config.toml; el resto de las horas solo recoge reacciones y envía las manuales.
// El token NO va aquí: se guarda en Cloudflare como secreto con el nombre GITHUB_TOKEN.
const REPO = "joeldragonball-jpg/requirements.txt";
const BOTS = [
  { archivo: "alertas.yml", inputs: { prueba: "false" } }, // sin mensaje de prueba
  { archivo: "onchain.yml", inputs: undefined }, // este bot no tiene inputs
];

// Además refresca los paneles de datos del móvil (workflow paneles.yml) de lunes a viernes a estas horas UTC [hora, minuto].
// GitHub lo lanza solo a las 21:30, pero con retraso; así sale puntual y se añaden dos pasadas más por el día.
const HORAS_PANELES = [[7, 0], [13, 0], [21, 30]];

export default {
  async scheduled(event, env, ctx) {
    const t = new Date(event.scheduledTime);
    const lanzar = [...BOTS];
    if (t.getUTCDay() >= 1 && t.getUTCDay() <= 5 && HORAS_PANELES.some(([h, m]) => t.getUTCHours() === h && t.getUTCMinutes() === m)) {
      lanzar.push({ archivo: "paneles.yml", inputs: undefined });
    }
    // Noticias: cada hora en punto (el cron de GitHub solo lo ejecutaba 5-6 veces al día). prueba=false es obligatorio: por defecto el workflow manda noticias de prueba.
    if (t.getUTCMinutes() === 0) lanzar.push({ archivo: "noticias.yml", inputs: { prueba: "false" } });
    for (const bot of lanzar) {
      const cuerpo = { ref: "main" };
      if (bot.inputs) cuerpo.inputs = bot.inputs;
      const r = await fetch(`https://api.github.com/repos/${REPO}/actions/workflows/${bot.archivo}/dispatches`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${env.GITHUB_TOKEN}`,
          Accept: "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "User-Agent": "lanzador-bots",
        },
        body: JSON.stringify(cuerpo),
      });
      // 204 = lanzado. Si no, se escribe el motivo que da GitHub (nunca contiene el token).
      const motivo = r.status === 204 ? "" : (await r.text()).slice(0, 300);
      console.log(bot.archivo, r.status, motivo);
    }
  },
  // Visitar la dirección del Worker solo muestra este texto: no lanza nada.
  async fetch() {
    return new Response("lanzador-bots activo (solo por cron)");
  },
};
