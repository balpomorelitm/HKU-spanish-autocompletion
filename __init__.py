# -*- coding: utf-8 -*-
# Este es el archivo principal de tu plugin de Anki.

from aqt import mw
from aqt.utils import showInfo
from aqt import gui_hooks
from PyDictionary import PyDictionary

# Esta función se ejecutará cuando Anki se inicie.
def mi_primer_plugin_de_anki():
    showInfo("¡Hola desde tu plugin de Anki en español!")

# Aquí es donde "conectamos" nuestra función a un evento de Anki.
# gui_hooks.profile_did_open es un "gancho" que se activa cuando abres tu perfil de Anki.
gui_hooks.profile_did_open.append(mi_primer_plugin_de_anki)

# Instancia del diccionario para obtener definiciones
diccionario = PyDictionary()


def autocompletar_definicion(cambiado: bool, nota, indice_campo: int) -> bool:
    """Completa el campo 'Definicion' basado en el campo 'Palabra'."""
    try:
        palabra = nota["Palabra"].strip()
    except Exception:
        return cambiado

    try:
        definicion_actual = nota["Definicion"].strip()
    except Exception:
        definicion_actual = ""

    # Si ya hay una definición o la palabra está vacía, no hacemos nada
    if definicion_actual or not palabra:
        return cambiado

    try:
        significado = diccionario.meaning(palabra)
    except Exception:
        significado = None

    if significado:
        if isinstance(significado, dict):
            partes = [defs[0] for defs in significado.values() if defs]
            definicion = "; ".join(partes)
        else:
            definicion = str(significado)
    else:
        definicion = "[No encontrada]"

    nota["Definicion"] = definicion
    return True


# Conectamos la función al gancho que se ejecuta al perder el foco un campo
gui_hooks.editor_did_unfocus_field.append(autocompletar_definicion)
