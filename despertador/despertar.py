"""Despierta la app de Streamlit para que esté lista cuando la abras.

Streamlit Cloud (plan gratis) duerme las apps tras ~12 horas sin visitas y al abrirlas tarda en arrancar.
GitHub Actions lanza este programa cada mañana y cada pocas horas (.github/workflows/despertador.yml):
abre la app con un navegador invisible, pulsa "despertar" si está dormida y espera a que cargue.
"""
import re
import time

from playwright.sync_api import sync_playwright

URL = "https://requirementstxt-ns7rcahvp34hst8onfbyxg.streamlit.app/"
ESPERA_MAXIMA = 240  # segundos


def app_cargada(page):
    """True cuando el título de la app aparece en la página o dentro de su marco."""
    for frame in page.frames:
        try:
            if "Mi Cartera Cripto" in frame.content():
                return True
        except Exception:
            pass
    return False


def main():
    inicio = time.time()
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        page = navegador.new_page()
        page.goto(URL, timeout=120_000)

        despertada = False
        while time.time() - inicio < ESPERA_MAXIMA:
            boton = page.get_by_role("button", name=re.compile("get this app back up", re.I))
            if not despertada and boton.count():
                boton.first.click()
                despertada = True
                print("La app estaba dormida: la despierto.")
            if app_cargada(page):
                print(f"App lista en {time.time() - inicio:.0f} s" + (" (estaba dormida)" if despertada else ""))
                break
            time.sleep(5)
        else:
            print("La app no terminó de cargar a tiempo; se volverá a intentar en la próxima ejecución.")
        time.sleep(10)  # deja que termine de cargar los datos (así también quedan en caché)
        navegador.close()


if __name__ == "__main__":
    main()
