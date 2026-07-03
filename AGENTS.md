# AGENTS.md

## Forma Del Workspace

- Este workspace no es una sola app: `backend/` está vacío, `editor/` contiene el editor XML en Python y `frontend/azumchefe_lexicon/` contiene la app SvelteKit.
- Ejecuta los comandos desde el directorio del proyecto correspondiente; la raíz no tiene manifest ni task runner.
- Preserva las guías anidadas en `editor/AGENTS.md` y `frontend/azumchefe_lexicon/AGENTS.md` cuando trabajes dentro de esos árboles.

## Editor: `editor/fillke-nemul-editor`

- App de escritorio con tkinter + `lxml` para recursos léxicos XML; la interfaz está en español.
- Punto de entrada: desde `editor/`, ejecuta `python fillke-nemul-editor/editor/main.py`.
- No se encontró `requirements.txt`, lint, typecheck ni configuración de tests; instala `lxml` manualmente si hace falta y verifica abriendo la app.
- Rama actual verificada: `dev_2`; no asumas que la raíz del workspace es un repo git.
- La arquitectura principal es MVC: los modelos poseen el estado XML, las vistas son widgets tkinter pasivos y los controladores conectan callbacks.
- Las etiquetas y atributos XML viven en `editor/fillke-nemul-editor/editor/constants.py`; evita dispersar strings del esquema.
- El modelo XML indexa elementos por `id(element)` y reconstruye el índice en `_build_element_index()` después de abrir un archivo.
- Usa `editor/dictionary.alex` como XML de muestra para verificaciones manuales de apertura/edición.
- Convención de commits desde `CONTRIBUTING.md`: `feat: ...`, `fix: ...` o `chore: ...`, descripción imperativa en minúscula y sin punto final.

## Frontend: `frontend/azumchefe_lexicon`

- Proyecto SvelteKit + Svelte 5 runes con `pnpm`; la documentación indica Node.js 20+.
- Instala/ejecuta desde `frontend/azumchefe_lexicon`: `pnpm install`, `pnpm dev`.
- Comandos de verificación: `pnpm lint`, `pnpm check`, `pnpm build`; `pnpm lint` incluye Prettier check y ESLint.
- Usa `pnpm format` para autoformatear; Prettier usa tabs, comillas simples, sin trailing commas, ancho 100 y ordenamiento Tailwind vía `src/routes/layout.css`.
- La config de Vite fuerza Svelte runes mode para archivos del proyecto; escribe componentes nuevos con Svelte 5 runes.
- Las rutas API leen diccionarios JSON directamente desde `static/diccionarios` con `fs` y `path.resolve('static/diccionarios')`; mantén comandos y servidores ejecutándose desde el directorio frontend.
- El flujo principal de UI está en `src/routes/+page.svelte`; los componentes se reexportan desde `src/lib/components/index.ts`.
- La forma de datos del diccionario está en `src/lib/types.ts`; los mapeos de visualización y helpers de búsqueda están en `src/lib/constants.ts` y `src/lib/helpers.ts`.
- `.gitignore` ignora intencionalmente `README.md`, `AGENTS.md`, `DOCUMENTACION.md`, `.opencode/`, `.env*`, outputs de build y `.svelte-kit`.
