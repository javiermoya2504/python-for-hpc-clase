\# Proyecto HPC — Procesamiento de datos



\## 1. Descripción del proyecto



Este proyecto tiene como propósito comparar el rendimiento de un procesamiento secuencial y uno paralelo utilizando Python. Se procesará una cantidad considerable de datos mediante una función matemática y se medirán los tiempos de ejecución para analizar el comportamiento del procesamiento con diferentes cantidades de trabajadores.



\## 2. Problema



El procesamiento de grandes cantidades de datos puede requerir un tiempo considerable cuando se ejecuta de manera secuencial. Por esta razón, se busca analizar si la ejecución en paralelo permite reducir el tiempo de procesamiento y mejorar el rendimiento.



\## 3. Objetivo



Comparar el tiempo de ejecución de un procesamiento secuencial con diferentes configuraciones de procesamiento paralelo, utilizando 1, 2 y 4 trabajadores.



\## 4. Metodología



Se generó un conjunto de 2,000,000 valores positivos para realizar el procesamiento.



La función matemática utilizada es:



f(x) = √x + x² + sin(x) + cos(x) + log(x)



El procesamiento secuencial realiza la operación sobre todos los datos uno por uno.



Para la versión paralela se utilizará procesamiento mediante múltiples trabajadores, distribuyendo los datos entre ellos para realizar las operaciones de manera simultánea.



\## 5. Procesamiento secuencial



El procesamiento secuencial se implementó en el notebook `secuencial.ipynb`.



Se realizaron tres ejecuciones para obtener una medición más representativa del tiempo de procesamiento.



| Ejecución    | Tiempo        |

| 1            | 1.380441 s    |

| 2            | 1.320341 s    |

| 3            | 1.357313 s    |

| \*\*Promedio\*\* | \*\*1.352698 s\*\*|



La cantidad de datos procesados fue de 2,000,000 registros.



Además, se realizó una validación para comprobar que se obtuviera la cantidad esperada de resultados y que los valores generados fueran válidos.



\## 6. Procesamiento paralelo



La implementación paralela se desarrollará en `paralelo.ipynb`.



Se realizarán pruebas utilizando:



\- 1 worker.

\- 2 workers.

\- 4 workers.



Para cada configuración se realizarán tres ejecuciones y se registrará el tiempo obtenido.



Los resultados se agregarán posteriormente.



\## 7. Resultados



\### 7.1 Tiempos de ejecución



| Configuración | Ejecución 1 | Ejecución 2 | Ejecución 3 | Promedio  |

| Secuencial    | 1.380441 s  | 1.320341 s  | 1.357313 s  | 1.35269 s |

| 1 worker      | Pendiente   | Pendiente   | Pendiente   | Pendiente |

| 2 workers     | Pendiente   | Pendiente   | Pendiente   | Pendiente |

| 4 workers     | Pendiente   | Pendiente   | Pendiente   | Pendiente |



\### 7.2 Speedup





\### 7.3 Eficiencia





\## 8. Análisis





\## 9. Conclusiones







\## 10. Integrantes



\- Daniela Sánchez

\- Karina Pérez

\- Axel Quevedo

