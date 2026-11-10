# -*- coding: utf-8 -*-
"""Leyendas en lenguaje llano para los bloques de contratación (PLACSP) y subvenciones (BDNS).
Las usan leer_contratacion.py y leer_bdns.py; la Órbita las pinta junto a las tablas."""

# Códigos de procedimiento: lista oficial SyndicationTenderingProcessCode 2.07 de la PLACSP
# (https://contrataciondelestado.es/codice/cl/2.07/SyndicationTenderingProcessCode-2.07.gc). Nivel P.
LEYENDA_CONTRATACION = {
    "expediente": "Un expediente es UN procedimiento de contratación concreto (por ejemplo, «obras de la calle X»), con un número identificador propio. No es una ley ni un presupuesto: es el papeleo de una compra pública. Contar expedientes es contar procedimientos, no euros.",
    "presupuesto": "Presupuesto base de licitación = el máximo que el órgano está dispuesto a gastar en ese contrato, fijado antes de que se presenten ofertas (sin IVA).",
    "adjudicado": "Importe adjudicado = lo que el contrato acaba costando según la oferta ganadora (sin IVA). Suele ser menor que el presupuesto. Es 0 mientras el expediente no está adjudicado. En un acuerdo marco con varias empresas, el importe es un techo común, no dinero repartido.",
    "procedimientos": {
        "Abierto": "Cualquier empresa puede presentar oferta. Es el procedimiento ordinario y el más transparente.",
        "Abierto simplificado": "Variante rápida del abierto para contratos de menor cuantía (obras hasta 2 M€, suministros y servicios hasta 143.000 € aprox.).",
        "Restringido": "Solo presentan oferta las empresas invitadas tras una selección previa.",
        "Negociado sin publicidad": "El órgano negocia directamente con una o pocas empresas, sin anuncio público. Solo cabe en supuestos tasados (urgencia, exclusividad técnica...). Es el que más conviene mirar con atención, aunque usarlo no es ilegal.",
        "Negociado con publicidad": "Se anuncia el contrato y luego se negocia con las empresas que se presentan.",
        "Licitación con negociación": "Procedimiento de la Ley 9/2017 (código 13 de la plataforma): se anuncia, se pide oferta inicial y se negocia con las empresas admitidas.",
        "Diálogo competitivo": "Para contratos muy complejos: el órgano dialoga con las empresas para definir la solución antes de pedir oferta final.",
        "Asociación para la innovación": "Para desarrollar un producto o servicio nuevo que aún no existe en el mercado y comprarlo después.",
        "Derivado de acuerdo marco": "Contrato concreto que se adjudica dentro de un acuerdo marco ya licitado (por ejemplo, la compra centralizada del Estado).",
        "Concurso de proyectos": "Se premia el mejor proyecto (típicamente de arquitectura o diseño).",
        "Normas internas": "Contratación de entes públicos que no son administración (empresas públicas, fundaciones) con sus propias reglas internas.",
        "Contrato menor": "Contratos de muy poco importe (hasta 40.000 € obras / 15.000 € resto) que se adjudican directamente. Van en otro fichero.",
        "Otros": "Procedimientos que la plataforma no clasifica en las categorías anteriores.",
    },
    "codigos": {"3": "Negociado sin publicidad", "4": "Negociado con publicidad", "13": "Licitación con negociación",
                "9": "Abierto simplificado", "100": "Normas internas", "999": "Otros"},
    "estados": {"PUB": "Publicada (se puede ofertar)", "EV": "En evaluación de ofertas", "ADJ": "Adjudicada",
                "RES": "Resuelta (adjudicada y formalizada o cerrada)", "PRE": "Anuncio previo", "ANUL": "Anulada"},
    "no_dice": "Un contrato grande, un adjudicatario repetido o un órgano con muchos expedientes NO es una irregularidad. Y esta lista NO es toda la contratación pública de España: solo recoge las entidades con perfil en la plataforma estatal; faltan plataformas autonómicas y locales propias. Tampoco son pagos: son contratos adjudicados.",
    "ventana": "Solo octubre de 2026: expedientes cuya última actualización cayó en ese mes (algunos son de años anteriores, p. ej. una adjudicación de 2021 que se modificó en octubre).",
}

LEYENDA_SUBVENCIONES = {
    "concesion": "Una concesión es una ayuda concreta concedida a un beneficiario (una empresa, una entidad o una persona). Una convocatoria es la oferta pública de ayudas; de una convocatoria salen muchas concesiones.",
    "importe": "Importe concedido = lo que la administración se compromete a dar. No es lo pagado ni lo ejecutado.",
    "niveles": {"ESTADO": "Administración General del Estado y sus organismos", "AUTONOMICA": "Comunidades y ciudades autónomas",
                "LOCAL": "Ayuntamientos, diputaciones, cabildos y consells", "OTROS": "Otras entidades (universidades, cámaras, etc.)"},
    "instrumentos": {"SUBVENCIÓN y ENTREGA DINERARIA SIN CONTRAPRESTACIÓN": "Dinero a fondo perdido: no hay que devolverlo si se cumplen las condiciones",
                     "PRÉSTAMO": "Dinero que hay que devolver, a menudo sin intereses o con intereses bajos",
                     "GARANTÍA": "La administración avala un préstamo de otro", "OTROS INSTRUMENTOS DE AYUDA": "Otras formas de ayuda"},
    "no_dice": "Un beneficiario grande o repetido NO es una irregularidad: muchos son cabildos, ayuntamientos, universidades o entes que reparten ayudas europeas. Las personas físicas vienen enmascaradas por la BDNS y no se listan. Tampoco es todo el gasto en ayudas de España: depende de lo publicado en la ventana y de que cada entidad lo comunique.",
    "ventana": "Solo concesiones de los últimos 60 días (ventana indicada arriba); no es un año completo.",
}
