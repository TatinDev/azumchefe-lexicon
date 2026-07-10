# fillke-nemul-editor — Guía para el agente

## Proyecto
Editor de recursos léxicos XML con **tkinter + lxml** para mapudungun ("ñi Fillke Nemül"). Escritorio, patrón MVC, interfaz en español.

## Estructura del repo
```
fillke-nemul-editor/     # Proyecto principal
  editor/
    main.py               # Punto de entrada — ejecutar desde la raíz del repo
    constants.py          # Etiquetas, colores, definiciones de tags/atributos XML (dataclasses inmutables)
    models/
      lexical_resource_model.py    # Documento XML (lxml) + índice de elementos
    controllers/
      application_controller.py    # Conecta modelo, menú, barra de estado y área de trabajo
      menu_bar_controller.py       # Acciones del menú mediante entryconfig()
      workspace_controller.py      # Abrir archivos, navegación en árbol, ventanas de edición
      status_bar_controller.py     # Actualizaciones de la barra de estado
    views/
      application_frame.py, menu_bar.py, status_bar_frame.py, workspace_frame.py
      about_dialog.py, help_dialog.py
      common/                      # Frames reutilizables (botón, árbol, entrada)
      editor/                      # Ventana de edición de elementos (árbol + editor de atributos)
  Ayuda/                  # Contenido de ayuda (markdown)
dictionary.alex          # Diccionario XML de muestra para pruebas
```

## Ejecutar
```bash
python fillke-nemul-editor/editor/main.py
```
Sin compilación. Requiere Python 3.x + `lxml` solamente.

## Dependencias
- `lxml` (parseo XML) — no hay requirements.txt; instalar con `pip install lxml`
- Librería estándar: tkinter, ttk, os, dataclasses, filedialog

## Flujo de trabajo con Git
- **Rama activa**: `dev_2` — trabajar en esta rama, NO en `main`
- **Formato de commits** (`CONTRIBUTING.md`): `<tipo>: <descripción>` (imperativo, minúscula, sin punto)
  - `chore:` — cambios que no modifican código fuente
  - `feat:` — nueva funcionalidad
  - `fix:` — corrección de errores

## Arquitectura y convenciones
- **MVC**: Los modelos poseen los datos, las Vistas son UI pasivas, los Controladores las conectan
- **Conexión controlador-vista**: Los comandos se vinculan con `menu.entryconfig(etiqueta, command=método)` en el `__init__` del controlador
- **Diálogos**: `tk.Toplevel` con `transient(padre)` + `grab_set()` para modal; pasar `self.application.tk` como padre
- **Constantes**: Todas las etiquetas, colores, nombres de tags XML y definiciones de atributos viven en `constants.py` como dataclasses inmutables
- **Patrones de diseño**: `PanedWindow` para paneles redimensionables, `grid` para scrollbar+contenido, `pack` para flujo lineal
- **Esquema XML**: `lx` (raíz), `en` (artículo), `fr` (forma), `cf` (subartículo), `sn` (acepción), `rf` (referencia), `df` (definición), `qt` (ejemplo)
- **Índice de elementos**: Clave por `id(elemento)` — se reconstruye al abrir archivo mediante `_build_element_index()`

## Pruebas
No se detectó framework de pruebas. No hay configuración de lint ni typecheck. Verificar los cambios ejecutando la app manualmente.

## Datos de muestra
`dictionary.alex` en la raíz del repo es un diccionario mapudungun-español en XML. Usarlo para probar la apertura de archivos y la edición.
