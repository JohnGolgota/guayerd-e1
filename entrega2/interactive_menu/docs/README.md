# Diagrama de Flujo del Visor Interactivo

## Ver Diagrama de Flujo en Línea

**Visor de Documentación Interactivo:**

👉 **[Abrir Diagrama en MermaidChart](https://www.mermaidchart.com/d/47deed55-555a-49b4-b045-2f80363d53e5)**

Este diagrama muestra el flujo completo del programa `interactive_menu/main.py`, incluyendo:
- Carga y parseo del archivo `documentation.md`
- Navegación por menú interactivo
- Búsqueda de secciones H1 y subsecciones H2
- Renderizado con formato Markdown y colores ANSI
- Manejo de errores y validaciones

---

## Archivo Local

El código fuente del diagrama también está disponible localmente:

```
interactive_menu/docs/flowchart.mmd
```

```mermaid
flowchart TD
    Start([INICIO]) --> LoadFile[Cargar documentacion.md<br/>desde directorio padre]
    LoadFile --> CheckFile{¿Archivo<br/>existe?}
    
    CheckFile -->|No| ErrorFile[Mostrar error:<br/>Archivo no encontrado]
    ErrorFile --> End1([FIN - Error])
    
    CheckFile -->|Sí| Parse[Parsear documento:<br/>Identificar H1 secciones<br/>y H2 subsecciones]
    Parse --> BuildStruct[Construir estructura:<br/>titulo, contenido, subsecciones]
    BuildStruct --> CheckSections{¿Secciones<br/>encontradas?}
    
    CheckSections -->|No| ErrorEmpty[Mostrar error:<br/>No se encontraron secciones]
    ErrorEmpty --> End2([FIN - Error])
    
    CheckSections -->|Sí| IndexSections[Indexar secciones:<br/>• Primera sección<br/>• Dataset de Referencia<br/>• Programa]
    IndexSections --> FindScale[Buscar subsección<br/>Escala dentro de Dataset]
    
    FindScale --> ClearScreen[Limpiar pantalla]
    ClearScreen --> Menu[Mostrar Menú:<br/>1-6 opciones + 0 salir]
    
    Menu --> Input[Leer opción del usuario]
    Input --> ValidateInput{Validar<br/>entrada}
    
    ValidateInput -->|Ctrl+C/Ctrl+D| Interrupt[Capturar interrupción]
    Interrupt --> Goodbye1[Mostrar: ✓ Saliendo...]
    Goodbye1 --> End3([FIN - Normal])
    
    ValidateInput -->|Opción 0| Goodbye2[Mostrar: ✓ Saliendo...]
    Goodbye2 --> End4([FIN - Normal])
    
    ValidateInput -->|Opción 1| Op1[Buscar subsecciones:<br/>Tema, Problema, Solución<br/>en primera sección]
    ValidateInput -->|Opción 2| Op2[Buscar sección:<br/>Dataset de Referencia]
    ValidateInput -->|Opción 3| Op3[Verificar subsección:<br/>Escala de BD]
    ValidateInput -->|Opción 4| Op4[Buscar sección:<br/>Programa]
    ValidateInput -->|Opción 5| Op5[Renderizar documento<br/>completo con formato]
    ValidateInput -->|Opción 6| Op6[Mostrar información<br/>de Notebooks de análisis]
    ValidateInput -->|Otra| Invalid[Mostrar:<br/>Opción inválida 0-6]
    
    Op1 --> FormatSubs1[Formatear subsecciones<br/>con Markdown]
    FormatSubs1 --> ShowContent1[Mostrar contenido<br/>formateado con colores]
    
    Op2 --> CheckDataset{¿Dataset<br/>encontrado?}
    CheckDataset -->|Sí| FormatSection2[Formatear sección<br/>completa con Markdown]
    FormatSection2 --> ShowContent2[Mostrar título + contenido<br/>+ todas subsecciones]
    CheckDataset -->|No| ErrorDataset[Error: Sección<br/>Dataset no encontrada]
    
    Op3 --> CheckScale{¿Escala<br/>encontrada?}
    CheckScale -->|Sí| FormatSubs3[Formatear subsección<br/>con Markdown]
    FormatSubs3 --> ShowContent3[Mostrar contenido<br/>de Escala]
    CheckScale -->|No| ErrorScale[Error: Subsección<br/>Escala no encontrada]
    
    Op4 --> CheckProgram{¿Programa<br/>encontrado?}
    CheckProgram -->|Sí| FormatSection4[Formatear sección<br/>completa con Markdown]
    FormatSection4 --> ShowContent4[Mostrar título + contenido<br/>+ todas subsecciones]
    CheckProgram -->|No| ErrorProgram[Error: Sección<br/>Programa no encontrada]
    
    Op5 --> RenderAll[Procesar línea por línea:<br/>• Detectar bloques código<br/>• Aplicar formato Markdown<br/>• Renderizar con colores]
    RenderAll --> ShowAll[Mostrar documento<br/>completo formateado]

    Op6 --> ShowNotebooks[Mostrar menú:<br/>4 notebooks de análisis<br/>con descripciones]
    ShowNotebooks --> ShowContent6[Mostrar información<br/>formateada de cada notebook]
    
    ShowContent1 --> Wait1[Presione ENTER...]
    ShowContent2 --> Wait2[Presione ENTER...]
    ShowContent3 --> Wait3[Presione ENTER...]
    ShowContent4 --> Wait4[Presione ENTER...]
    ShowAll --> Wait5[Presione ENTER...]
    ShowContent6 --> Wait6[Presione ENTER...]
    ErrorDataset --> Wait7[Presione ENTER...]
    ErrorScale --> Wait8[Presione ENTER...]
    ErrorProgram --> Wait9[Presione ENTER...]
    Invalid --> Wait10[Presione ENTER...]
    
    Wait1 --> ClearScreen
    Wait2 --> ClearScreen
    Wait3 --> ClearScreen
    Wait4 --> ClearScreen
    Wait5 --> ClearScreen
    Wait6 --> ClearScreen
    Wait7 --> ClearScreen
    Wait8 --> ClearScreen
    Wait9 --> ClearScreen
    Wait10 --> ClearScreen
    
    style Start fill:#4CAF50,stroke:#2E7D32,color:#fff,stroke-width:3px
    style End1 fill:#F44336,stroke:#C62828,color:#fff,stroke-width:3px
    style End2 fill:#F44336,stroke:#C62828,color:#fff,stroke-width:3px
    style End3 fill:#2196F3,stroke:#1565C0,color:#fff,stroke-width:3px
    style End4 fill:#2196F3,stroke:#1565C0,color:#fff,stroke-width:3px
    
    style Menu fill:#FF9800,stroke:#E65100,color:#fff,stroke-width:2px
    style ClearScreen fill:#FFEB3B,stroke:#F57F17,color:#000,stroke-width:2px
    
    style LoadFile fill:#9C27B0,stroke:#6A1B9A,color:#fff
    style Parse fill:#9C27B0,stroke:#6A1B9A,color:#fff
    style BuildStruct fill:#9C27B0,stroke:#6A1B9A,color:#fff
    style IndexSections fill:#9C27B0,stroke:#6A1B9A,color:#fff
    
    style FormatSubs1 fill:#00BCD4,stroke:#006064,color:#fff
    style FormatSection2 fill:#00BCD4,stroke:#006064,color:#fff
    style FormatSubs3 fill:#00BCD4,stroke:#006064,color:#fff
    style FormatSection4 fill:#00BCD4,stroke:#006064,color:#fff
    style RenderAll fill:#00BCD4,stroke:#006064,color:#fff
    style ShowNotebooks fill:#00BCD4,stroke:#006064,color:#fff
```