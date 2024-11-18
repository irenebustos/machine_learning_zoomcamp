@@ -0,0 +1,13 @@
El onjetivo de este proyecto es predecir el tiempo que un animal va a tardar en ser adoptado. 

1. Source de los datos
Intakes de los animales de un shelter en Austine
Outcomes de los animales de ese mismo shelter 
En el Archivo llamado ¨time_shelter_dataset¨se detalla cual ha sido el proceso de creacion del dataset que se va a usar. 
Como summary: 
- Los datos han sido mergeados entre intakes y outcomes, habiendo por el medio una serie de ajustes:
    - cuando hay mas de un intake por animal lo que se hace es atribuir el outcome basandonos en el outcome mas proximo a este income datetime. 
    - cuando un intake se ha producido en el medio de otro intake-outcome del mismo animal se elimina este ya que se considera un error de la base de datos.
    - solo nos quedamos con el outcome_type = Adoption por simplificar, ya que los otros tipos de outcomes no son relevantes para este ejercicio de prediccion (mas detalles en el archivo)
