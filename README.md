# Guía de Uso y Modificación del EcoBot

A continuación se detallan los pasos para utilizar y modificar el bot, junto con la estructura de archivos y comandos disponibles:

### Configuración Inicial

1. **Clona o descarga el repositorio** en tu máquina local.
2. **Abre el archivo `EcoBot.py`** en tu editor de texto o IDE favorito.
3. **Obtén un token de bot de Discord**. Sigue las instrucciones en la [documentación oficial de Discord](https://discord.com/developers/docs/intro) para obtenerlo.
4. **Reemplaza `TU_TOKEN_DE_DISCORD`** en el archivo `EcoBot.py` con el token de tu bot.

---

### Estructura del Proyecto

- **`EcoBot.py`**: Este es el archivo principal del bot. Contiene la definición de los comandos.
- **`Bot/Module/Clasificacion_tiempo_y_peligros.py`**: Define la función `mostrar_informacion_categoria`, que proporciona detalles sobre las categorías de residuos.

---

### Comandos Disponibles

El bot ofrece varios comandos que puedes usar en tu servidor de Discord:

- **`Manu`**: Busca manualidades reciclables.
- **`DataContaA`**: Muestra la calidad del aire en tu ubicación actual.
- **`DataContaM`**: Muestra la calidad del aire en una ciudad específica.
- **`ContaA`**: Muestra el contaminante dominante en tu ubicación actual.
- **`ContaM`**: Muestra el contaminante dominante en una ciudad específica.
- **`ClimA`**: Muestra el clima actual en tu ubicación.
- **`ClimM`**: Muestra el clima actual en una ciudad específica.
- **`Datacien`**: Busca datos científicos sobre un tema.
- **`Consejo`**: Proporciona consejos sobre un tema.
- **`Catere`**: Muestra las categorías de residuos.
- **`Info`**: Muestra información detallada sobre una categoría de residuos.

---

### Ejemplo de Uso

Para ejecutar el bot, abre una terminal en el directorio donde se encuentra el archivo `EcoBot.py` y ejecuta el siguiente comando:

```
python EcoBot.py
```

---

### Modificación del Bot

Si deseas agregar o modificar comandos, sigue estos pasos:

1. **Editar comandos**: Abre el archivo `EcoBot.py` y sigue la estructura de los comandos existentes para agregar nuevos.
2. **Modificar categorías de residuos**: Para cambiar la información relacionada con las categorías de residuos, edita la función `mostrar_informacion_categoria` en el archivo `Bot/Module/Clasificacion_tiempo_y_peligros.py`.

Recuerda probar el bot después de realizar cualquier modificación.
