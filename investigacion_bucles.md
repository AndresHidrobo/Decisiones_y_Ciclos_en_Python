# 1. Diferencias entre un bucle controlado por contador y un bucle controlado por condición.
    Un método se controla mediante un contador (que incrementa o decrece), normalmente en cada iteración del bucle, y este finaliza cuando el contador alcanza un límite conocido. Generalmente se trata de un bucle "for" o similar.

    El otro método se controla mediante una expresión condicional (que se evalúa como verdadera o falsa), la cual puede o no cambiar en cada iteración. Normalmente se trata de un bucle "while".

# 2. Ejempos cotidianos
# Bucle Controlado por Contador
    Contar cuántas páginas lees de un libro:
    “Voy a leer 5 páginas cada día.”
    -La entrada es (5) páginas
    -Entonces el proceso de leer la página se repitela hasta que leas las 5 páginas del libro.
# Bucle Controlado por Condición
    Repetir la tarea hasta que esté correcta
    -El preceso se repetirá hasta que se cumpla la condición

# 3. Situaciones favorables
    Los ciclos "for" son mas favorables de usar cuando sabes la cantidad de veces que se debe repetir el proceso, mientras que los ciclos "while" se usan cuando no sabes cuantas veces debes hacer el proceso hasta cumplirlo

# 4. Bucle Infinito
    De forma resumida un bucle infinito es cuando un bucle ya sea usando "for" o "while" nunca puede cumplir con su objetivo y se repite de forma infinita.
    Las mejores formas de prevenirlo son:
    -Asegurarse de que la condición cambie o se cumpla dentro del bucle.
    -Usar una "bandera" ya sea un contador o condición de salida clara.
    -Incluir un break cuando se cumpla cierta condición.

# 5. Break y Continue
    break: Interrumpe el ciclo inmediatamente, aunque la condición siga siendo verdadera.
    continue: se salta el resto del bloque actual y pasa a la siguiente iteración.

# 6. Error mas común
    El error más común al usar un ciclo "while" es cuando no cumple con su condicion probocando un bucle infinito.
    Para evitarlo leer punto #4.