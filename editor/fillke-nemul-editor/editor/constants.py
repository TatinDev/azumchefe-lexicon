from dataclasses import dataclass

# Views

# Labels
@dataclass(frozen=True)
class ApplicationLabel:
    TITLE = "Editor ñi Fillke Nemül"

@dataclass(frozen=True)
class MenuBarLabel:
    FILE_MENU = "Archivo"
    FILE_NEW = "Nuevo archivo"
    FILE_OPEN = "Abrir..."
    FILE_SAVE = "Guardar"
    FILE_SAVE_AS = "Guardar como..."
    FILE_EXIT = "Salir"

    EDIT_MENU = "Editar"
    EDIT_UNDO = "Deshacer"
    EDIT_COPY = "Copiar"
    EDIT_PASTE = "Pegar"
    EDIT_DELETE = "Borrar"
    EDIT_FIND = "Buscar..."
    EDIT_GO_TO = "Ir a..."

    HELP_MENU = "Ayuda"
    HELP_VIEW_HELP = "Ver ayuda"
    HELP_ABOUT = "Acerca de"

@dataclass(frozen=True)
class StatusBarLabel:
    WORKPLACE_ENTRIES_COUNT = "entrada(s)"

@dataclass(frozen=True)
class WorkplaceLabel:
    TOOL_BAR_SEARCH_GO_BUTTON = "Ir"
    TOOL_BAR_SEARCH_TITLE = "Buscar"

    TREE_VIEW_TITLE = "Selector"
    TREE_VIEW_DEFAULT_STATUS = "Todas las entradas"

    # Dialogs

    DIALOG_FILE_OPEN_TITLE = "Abrir"

# Colors
@dataclass(frozen=True)
class Color:

    # views.common.button_frame

    ACCENT_BUTTON = "#ffd153"
    ACCENT_BUTTON_HOVER = "#fffab8"
    ACCENT_BUTTON_HOVER_FOREGROUND = "#b4810c"

    BUTTON = "#181818"
    BUTTON_HIGHLIGHT = "#aaaaaa"
    BUTTON_HIGHLIGHT_HOVER = "#ffd153"
    BUTTON_HIGHLIGHT_HOLD = "#de953f"

    # views.common.element_tree_view_frame

    TREE_VIEW_STATUS = "#ffd153"

    # views.common.entry_frame

    ENTRY_FIELD_HIGHLIGHT = "#a0a0a0"

    # views.common.text_frame

    TEXT_FIELD_HIGHLIGHT = "#a0a0a0"

    # views.workspace_frame

    ARTICLE_BACKGROUND = "#ebdfc5"
    ARTICLE_TITLE_FOREGROUND = "#b4810c"

    # views.editor.workspace_element_edit_frame

    EDITOR_BACKGROUND = "#aaaaaa"

# Files

# Tags
@dataclass(frozen=True)
class XMLTag:
    LEXICAL_RESOURCE = "lx"
    ENTRY = "en"
    ENTRY_GROUP = ""
    FORM = "fr"
    SUBENTRY = "cf"
    SENSE = "sn"
    REFERENCE = "rf"
    DEFINITION = "df"
    QUOTE = "qt"

    FULL_NAME = {
        LEXICAL_RESOURCE: "Léxico",
        ENTRY: "Artículo",
        ENTRY_GROUP: "Grupo de artículos",
        FORM: "Forma",
        SUBENTRY: "Artículo",
        SENSE: "Acepción",
        REFERENCE: "Referencia",
        DEFINITION: "Definición",
        QUOTE: "Ejemplo",
    }

# Attributes
@dataclass(frozen=True)
class XMLTagAttribute:

    @dataclass(frozen=True)
    class LexicalResource:
        RESOURCE_IDENTITY = ""
        TITLE = "l"
        SOURCE_LANGUAGE = "s"
        TARGET_LANGUAGE = "t"

        FULL_NAME = {
            RESOURCE_IDENTITY: "Identidad del recurso",
            TITLE: "Título",
            SOURCE_LANGUAGE: "Idioma fuente",
            TARGET_LANGUAGE: "Idioma objetivo",
        }

    @dataclass(frozen=True)
    class Entry:
        ENTRY_IDENTITY = ""
        TITLE = "l"
        PHONETIC_TITLE = ""

        FULL_NAME = {
            ENTRY_IDENTITY: "Identidad del artículo",
            TITLE: "Título",
            PHONETIC_TITLE: "Pronunciación (IPA)",
        }

    @dataclass(frozen=True)
    class EntryGroup:
        TITLE = "l"

        FULL_NAME = {
            TITLE: "Título",
        }

    @dataclass(frozen=True)
    class Reference:
        RESOURCE_IDENTIFIER = "_"
        TYPE = ""

        FULL_NAME = {
            RESOURCE_IDENTIFIER: "Identificador de recurso",
            TYPE: "Tipo",
        }

    @dataclass(frozen=True)
    class Form:
        TITLE = "_"
        PHONETIC_TITLE = ""

        FULL_NAME = {
            TITLE: "Título",
            PHONETIC_TITLE: "Pronunciación (IPA)"
        }

    @dataclass(frozen=True)
    class Sense:
        PART_OF_SPEECH = "p"
        GEOGRAPHIC_MARK = "g"
        CONTEXT_MARK = "r"
        EDITORIAL_NOTE = "n"

        FULL_NAME = {
            PART_OF_SPEECH: "Categoría gramatical",
            GEOGRAPHIC_MARK: "Marca geográfica",
            CONTEXT_MARK: "Marca contextual",
            EDITORIAL_NOTE: "Nota del editor",
        }

    @dataclass(frozen=True)
    class Definition:
        CONTENT = "_"
        EDITORIAL_NOTE = "n"

        FULL_NAME = {
            CONTENT: "Contenido",
            EDITORIAL_NOTE: "Nota del editor",
        }

    @dataclass(frozen=True)
    class Quote:
        CONTENT = "_"
        TARGET_LANGUAGE_TRANSLATION = "t"

        FULL_NAME = {
            CONTENT: "Contenido",
            TARGET_LANGUAGE_TRANSLATION: "Traducción",
        }

    # Initialization

    LEXICAL_RESOURCE = LexicalResource()
    ENTRY = Entry()
    ENTRY_GROUP = EntryGroup()
    REFERENCE = Reference()
    FORM = Form()
    SENSE = Sense()
    DEFINITION = Definition()
    QUOTE = Quote()

    TAG_TO_ATTRIBUTE_LIST = {
        XMLTag.LEXICAL_RESOURCE: LexicalResource,
        XMLTag.ENTRY: Entry,
        XMLTag.ENTRY_GROUP: EntryGroup,
        XMLTag.REFERENCE: Reference,
        XMLTag.FORM: Form,
        XMLTag.SENSE: Sense,
        XMLTag.DEFINITION: Definition,
        XMLTag.QUOTE: Quote,
    }

# Initialization

APPLICATION_LABEL = ApplicationLabel()
MENU_BAR_LABEL = MenuBarLabel()
STATUS_BAR_LABEL = StatusBarLabel()
WORKSPACE_LABEL = WorkplaceLabel()
COLOR = Color()
XML_TAG = XMLTag()
XML_TAG_ATTRIBUTE = XMLTagAttribute()