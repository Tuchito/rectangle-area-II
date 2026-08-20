---
description: Crea/completa el entorno virtual e instala herramientas de calidad (Experimental)
---

Ejecuta el skill `setup-virtual-environment` ubicado en
`.opencode/skills/setup-virtual-environment/`.

Este comando no contiene lógica propia — delega completamente en el skill,
que es la única fuente de verdad. Ver `.opencode/skills/setup-virtual-environment/SKILL.md`
para el detalle de comportamiento, alcance y salida esperada.

```bash
python .opencode/skills/setup-virtual-environment/implementation.py
```