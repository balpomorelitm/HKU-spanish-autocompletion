# -*- coding: utf-8 -*-
# Este es el archivo principal de tu plugin de Anki.

from aqt import mw
from aqt.utils import showInfo
from aqt import gui_hooks

# Esta función se ejecutará cuando Anki se inicie.
def mi_primer_plugin_de_anki():
    showInfo("¡Hola desde tu plugin de Anki en español!")

# Aquí es donde "conectamos" nuestra función a un evento de Anki.
# gui_hooks.profile_did_open es un "gancho" que se activa cuando abres tu perfil de Anki.
gui_hooks.profile_did_open.append(mi_primer_plugin_de_anki)
