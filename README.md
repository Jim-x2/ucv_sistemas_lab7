

# Laboratorio UCV: Minimax y Poda Alfa-Beta

## 1. Descripción

Este proyecto implementa los algoritmos Minimax y Poda Alfa-Beta
para resolver árboles de decisión de un juego simplificado.

## 2. Objetivo

Comparar los resultados de ambos algoritmos y analizar la
cantidad de hojas evaluadas durante la búsqueda.

## 3. Tecnologías utilizadas

- Python
- Git y GitHub
- pytest
- pytest-cov
- GitHub Actions

## 4. Estructura del proyecto

- `src/game_tree.py`: definición de los árboles.
- `src/minimax.py`: implementación de Minimax.
- `src/alpha_beta.py`: implementación de Poda Alfa-Beta.
- `src/main.py`: ejecución y comparación de los algoritmos.
- `tests/test_algorithms.py`: pruebas automatizadas.
- `.github/workflows/ci.yml`: integración continua.

## 5. Instalación

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Git Bash:

```bash
source .venv/Scripts/activate
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## 6. Ejecución

```bash
python -m src.main
```

## 7. Pruebas

```bash
pytest -v
```

Ejecutar las pruebas con cobertura:

```bash
pytest --cov=src --cov-report=term-missing --cov-report=xml
```

## 8. Preguntas de análisis

### 1. ¿Por qué Minimax y Alfa-Beta devuelven el mismo valor?

Porque ambos buscan la mejor decisión considerando las jugadas
de MAX y MIN. Alfa-Beta descarta ramas que no pueden cambiar
el resultado final.

### 2. ¿Qué representa alpha dentro del algoritmo?

Representa el mejor valor que MAX puede garantizar hasta el
momento durante la búsqueda.

### 3. ¿Qué representa beta dentro del algoritmo?

Representa el mejor límite que MIN puede garantizar hasta el
momento durante la búsqueda.

### 4. ¿En qué casos la Poda Alfa-Beta ahorra más trabajo?

Cuando el orden de exploración permite encontrar pronto límites
que hacen innecesario evaluar otras ramas.

### 5. ¿Por qué el orden de exploración afecta el rendimiento?

Porque encontrar buenas opciones primero permite realizar más
podas y reducir las hojas evaluadas.

### 6. ¿Qué pasaría si el rival no juega de manera racional?

La decisión basada en Minimax podría no representar el
comportamiento real del rival, porque supone que este elige
jugadas que minimizan el beneficio de MAX.

### 7. ¿Cómo se relaciona este algoritmo con motores de ajedrez?

Se utiliza como base para explorar movimientos y anticipar
respuestas del oponente. Los motores reales pueden combinarlo
con otras técnicas para reducir la búsqueda.

### 8. ¿Qué limitaciones tiene frente a redes neuronales o
aprendizaje por refuerzo?

Minimax depende del árbol de búsqueda y de sus valores de
evaluación. En problemas grandes, explorar muchas jugadas
puede ser costoso. Las redes neuronales y el aprendizaje por
refuerzo pueden aprender patrones o políticas, aunque también
tienen sus propias limitaciones.

## 9. Resultados obtenidos

Las cinco pruebas unitarias finalizaron correctamente.
La cobertura total registrada fue del 76 %.

Los árboles evaluados produjeron los valores 3, 7 y 8,
respectivamente, para los ejemplos pequeño, mediano y ordenado.

## 10. Integración continua

El flujo Python CI se ejecutó correctamente en GitHub Actions
sobre la rama `feature/lab7`.
