# Área de Rectángulos II

Se te da un arreglo bidimensional de rectángulos alineados con los ejes. Cada `rectangles[i] = [xi1, yi1, xi2, yi2]` denota el i-ésimo rectángulo, donde `(xi1, yi1)` son las coordenadas de la esquina inferior izquierda y `(xi2, yi2)` son las coordenadas de la esquina superior derecha.

Calcula el **área total** cubierta por todos los rectángulos en el plano. Cualquier área cubierta por dos o más rectángulos solo debe contarse **una vez**.

Devuelve el **área total**. Dado que la respuesta puede ser demasiado grande, devuélvela **módulo** 10^9 + 7.

## Ejemplo 1:

**Entrada:** rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
**Salida:** 6
**Explicación:** Un área total de 6 está cubierta por los tres rectángulos, como se ilustra en la imagen.
- Desde (1,1) hasta (2,2), los rectángulos verde y rojo se superponen.
- Desde (1,0) hasta (2,3), los tres rectángulos se superponen.

## Ejemplo 2:

**Entrada:** rectangles = [[0,0,1000000000,1000000000]]
**Salida:** 49
**Explicación:** La respuesta es 10^18 módulo (10^9 + 7), que es 49.

## Restricciones:

- 1 <= rectangles.length <= 200
- rectangles[i].length == 4
- 0 <= xi1, yi1, xi2, yi2 <= 10^9
- xi1 <= xi2
- yi1 <= yi2
- Todos los rectángulos tienen área no nula.

## Visualización del Ejemplo 1

El gráfico `rectangulos.png` ilustra los tres rectángulos del ejemplo 1:
- Rectángulo verde: (0,0) a (2,2)
- Rectángulo rojo: (1,0) a (2,3)
- Rectángulo azul: (1,0) a (3,1)

La superposición entre ellos genera regiones compartidas que deben contarse una sola vez. El área total única es 6.