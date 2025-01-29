residuos = {
    "organicos": {
        "ejemplos": ["restos de comida", "cáscaras de frutas", "hojas", "ramas"],
        "tiempo_descomposicion": {
            "cáscaras de frutas": "2-4 semanas",
            "restos de comida": "1-6 meses",
            "hojas o ramas": "1-3 años"
        },
        "afectaciones_ambientales": [
            "Emisión de gases de efecto invernadero (metano)",
            "Contaminación de suelos y aguas si no se gestionan adecuadamente"
        ]
    },
    "inorganicos_reciclables": {
        "ejemplos": ["plásticos", "vidrio", "aluminio", "papel", "cartón"],
        "tiempo_descomposicion": {
            "plásticos": "100-1,000 años",
            "vidrio": "indefinido",
            "aluminio": "10-100 años",
            "papel y cartón": "2-5 meses"
        },
        "afectaciones_ambientales": [
            "Contaminación de suelos y cuerpos de agua",
            "Acumulación de materiales que tardan siglos en degradarse",
            "Microplásticos que dañan la fauna marina y terrestre"
        ]
    },
    "inorganicos_no_reciclables": {
        "ejemplos": ["papel higiénico", "colillas de cigarro", "envolturas metalizadas", "residuos sanitarios"],
        "tiempo_descomposicion": {
            "colillas de cigarro": "10 años",
            "envolturas metalizadas": "100-500 años",
            "residuos sanitarios": "500 años"
        },
        "afectaciones_ambientales": [
            "Bloqueo de drenajes",
            "Contaminación de agua y suelo por químicos tóxicos",
            "Daño a la fauna si se ingieren accidentalmente"
        ]
    },
    "peligrosos": {
        "ejemplos": ["pilas", "baterías", "aceites usados", "medicamentos caducados", "productos químicos"],
        "tiempo_descomposicion": {
            "pilas": "500-1,000 años",
            "aceites usados": "indefinido",
            "medicamentos": "décadas"
        },
        "afectaciones_ambientales": [
            "Contaminación de agua subterránea y suelo con metales pesados (mercurio, cadmio, plomo)",
            "Intoxicación de animales y plantas",
            "Riesgo para la salud humana"
        ]
    },
    "electronicos": {
        "ejemplos": ["teléfonos móviles", "televisores", "electrodomésticos", "cables"],
        "tiempo_descomposicion": {
            "componentes plásticos": "100-1,000 años",
            "componentes metálicos": "variable (algunos no se descomponen)"
        },
        "afectaciones_ambientales": [
            "Liberación de sustancias tóxicas como plomo, arsénico y bromo al suelo y agua",
            "Riesgo de contaminación por lixiviados",
            "Daño a la fauna y flora por acumulación de materiales no degradables"
        ]
    },
    "biodegradables_especiales": {
        "ejemplos": ["madera tratada", "textiles naturales", "cuero"],
        "tiempo_descomposicion": {
            "madera tratada": "5-15 años",
            "textiles naturales": "1-5 años",
            "cuero": "10-50 años"
        },
        "afectaciones_ambientales": [
            "Liberación de sustancias químicas (barnices, tintes)",
            "Aumento del volumen de residuos en vertederos",
            "Lenta degradación en condiciones anaeróbicas"
        ]
    },
    "peligrosos_biologicos": {
        "ejemplos": ["residuos hospitalarios", "sangre", "jeringas", "ropa contaminada"],
        "tiempo_descomposicion": {
            "plástico de jeringas": "400 años"
        },
        "afectaciones_ambientales": [
            "Propagación de enfermedades infecciosas",
            "Contaminación del suelo y agua con microorganismos peligrosos",
            "Riesgo para la salud pública y trabajadores"
        ]
    }
}

# Ejemplo de cómo acceder a los datos
# Ejemplo de cómo acceder a los datos
def mostrar_informacion_categoria(categoria):
    # sourcery skip: for-append-to-extend, last-if-guard, merge-list-append, merge-list-appends-into-extend, remove-unnecessary-else, swap-if-else-branches
    if categoria in residuos:
        informacion = []
        informacion.append(f"Categoría: {categoria.capitalize()}")
        informacion.append("Ejemplos: " + ", ".join(residuos[categoria]["ejemplos"]))
        informacion.append("Tiempo de descomposición:")
        for material, tiempo in residuos[categoria]["tiempo_descomposicion"].items():
            informacion.append(f"  - {material}: {tiempo}")
        informacion.append("Afectaciones ambientales:")
        for afectacion in residuos[categoria]["afectaciones_ambientales"]:
            informacion.append(f"  - {afectacion}")
        return "\n".join(informacion)
    else:
        return f"No se encontro categoria, porfavor utilizar una de las siguientes:\n{', '.join(residuos.keys())}"