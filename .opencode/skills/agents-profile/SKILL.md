---
name: agents-profile
description: Genera el archivo AGENTS.md en la raíz del proyecto, con el rol, responsabilidades, restricciones, convenciones fijas del curso y herramientas disponibles del agente. Uso cuando el proyecto todavía no tiene un AGENTS.md o cuando el desarrollador pide definir/redefinir el perfil del agente.
allowed-tools: none
license: MIT
compatibility: Skill de razonamiento puro — no ejecuta código, no requiere Python ni dependencias.
metadata:
  author: curso-ai-skill-architect
  version: "1.0"
  generatedBy: "practica-my-calendar-iii"
  status: borrador — pendiente de confirmación al archivar openspec/changes/create-agents-profile
---

# agents-profile

## Naturaleza de este skill

Este skill **no tiene `implementation.py` ni `tests/`**. A diferencia de
`setup-production-project` y `setup-virtual-environment`, no hay lógica
determinista que ejecutar: sos vos, el agente, quien tiene que razonar
sobre el contexto del proyecto y redactar el contenido. Estas instrucciones
son el "programa" que seguís paso a paso.

## Paso 0 — Verificación previa (obligatoria, antes de escribir nada)

Antes de generar cualquier contenido, verificá si ya existe un archivo
`AGENTS.md` en la raíz del proyecto.

- **Si ya existe:** DETENETE. No lo sobrescribas ni intentes fusionarlo.
  Informale al desarrollador que ya existe un `AGENTS.md` en el proyecto,
  mostrale un resumen breve de su contenido actual, y pedile confirmación
  explícita sobre cómo proceder (reemplazarlo completo, dejarlo como está,
  o que te indique manualmente qué agregar). No continúes con los pasos
  siguientes hasta recibir esa confirmación.
- **Si no existe:** continuá con el Paso 1.

## Paso 1 — Generar las 5 secciones obligatorias

El `AGENTS.md` que generes debe tener, en este orden, las siguientes
secciones. Ninguna es opcional.

### 1. Rol del agente
Redactá una descripción breve (2-4 líneas) de qué tipo de agente es en
este proyecto — por ejemplo, "agente de implementación de features
siguiendo SDD" o "tutor/arquitecto de skills", experto desarrollador en python.
Si el desarrollador no especificó el rol al invocar este skill, preguntale antes de inventarlo.

### 2. Responsabilidades
Lista concreta de qué tareas puede/debe ejecutar el agente en este
proyecto. Inferila del tipo de proyecto (por ejemplo, si es un proyecto
de práctica algorítmica sin arquitectura ni despliegue, no incluyas
responsabilidades de infraestructura que no aplican) y de lo que el
desarrollador haya indicado.

### 3. Restricciones
Qué NO debe hacer el agente sin supervisión explícita del desarrollador.
Como mínimo, incluí:
- No hacer push a un repositorio remoto sin confirmación.
- No hacer merge a `main` sin que el desarrollador lo apruebe.
- No sobrescribir artefactos de `openspec/changes/` ya archivados.
- No ejecutar `openspec archive` sin confirmación explícita.

### 4. Convenciones del proyecto
Esta sección se completa **copiando textualmente** el siguiente bloque,
sin resumirlo ni reinterpretarlo — son las convenciones fijas acordadas
en este curso:

```markdown
- Estructura SDD: openspec/changes/<nombre>/ con proposal.md, design.md,
  tasks.md, delta.md.
- Prefijos de cambio: create-<nombre> para artefactos/skills nuevos,
  update-<nombre> para modificaciones de uno existente.
- Entorno virtual: .venv/ en la raíz del proyecto (no venv/ ni env/).
- Documentación operativa de skills: opencode/skills/<nombre>/SKILL.md se
  actualiza recién cuando el cambio correspondiente en openspec/ se
  archiva — no antes.
- Comandos en opencode/commands/<nombre>.md delegan al skill, nunca
  duplican su lógica.
- tasks.md usa formato checklist (- [ ] / - [x]) para que el agente marque
  el avance.
```

### 5. Herramientas disponibles
Listá los skills presentes en `.opencode/skills/` al momento de ejecutar
este skill (nombre y una línea de descripción, tomada del campo
`description` del encabezado de cada `SKILL.md` encontrado).

- **Si `.opencode/skills/` no existe o está vacía:** no dejes la sección
  vacía sin contexto. Escribí explícitamente: *"Todavía no hay skills
  instalados en este proyecto."*
- **Si hay skills:** listalos con su nombre y descripción, por ejemplo:
  - `setup-production-project`: estructura de carpetas, Git y .gitignore.
  - `setup-virtual-environment`: entorno virtual y herramientas de calidad.

## Paso 2 — Crear el archivo

Escribí el resultado en `AGENTS.md`, en la raíz del proyecto (no dentro de
`.opencode/` ni de ninguna subcarpeta).

## Paso 3 — Confirmar al desarrollador

Al terminar, mostrale al desarrollador un resumen breve de las 5 secciones
generadas (no el archivo completo repetido), y preguntale si el rol y las
responsabilidades reflejan correctamente lo que espera del agente en este
proyecto.

## Especificación de origen

`openspec/changes/create-agents-profile/{proposal,design,tasks,delta}.md`

## Validación

Este skill no tiene tests automatizados (no hay código que testear). Se
valida con revisión manual de completitud: el `AGENTS.md` resultante debe
tener las 5 secciones, el bloque de convenciones copiado sin alterar, y la
lista de herramientas fiel al estado real de `.opencode/skills/` en el
momento de la ejecución.