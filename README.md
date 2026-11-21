# Práctica: Préstamo de equipo en Odoo
**Estudiante:** Astrid Jissel Giron Diaz  
**Número de cuenta:** 0801200708358  

# Preguntas: Todas las Preguntas Respondidas

PASO 1. CATÁLOGO DE EQUIPOS
1. ¿Qué pasa con un equipo cuando se desmarca el campo Activo? ¿Por qué es mejor que borrarlo?
Respuesta: El equipo deja de aparecer normalmente en las listas, pero sus datos siguen guardados. Es mejor porque conserva el historial y no se pierde información.

2. ¿Para qué sirve copy=False en el campo codigo?
Respuesta: Evita que al duplicar un equipo se copie también su código. Así no se repite el mismo código de inventario.

PASO 2. REGISTRO DE PRÉSTAMOS
1. Este modelo usa _name y _inherit al mismo tiempo. ¿Qué hace cada uno aquí?
Respuesta: _name crea el modelo de préstamo y _inherit agrega las funciones del historial de mensajes de Odoo.

2. ¿Qué hace tracking=True en el campo state?
Respuesta: Guarda los cambios del estado en el chatter para poder ver cuándo cambió y cuál era el estado anterior.

PASO 3. EQUIPOS DEL PRÉSTAMO
1. En fields.One2many("prestamo.linea", "prestamo_id"), ¿qué indica cada parámetro?
Respuesta: El primero indica el modelo de las líneas y el segundo el campo que conecta cada línea con su préstamo.

2. ¿Qué pasa con las líneas cuando se borra un préstamo? ¿Qué parte del código lo define?
Respuesta: Las líneas también se borran. Lo define ondelete="cascade" en el campo prestamo_id.

PASO 4. FLUJO DE ESTADOS
1. Los botones ya se ocultan según el estado. ¿Por qué los métodos vuelven a validar el estado?
Respuesta: Porque así se evita ejecutar una acción incorrecta aunque alguien intente llamarla por otra vía.

2. ¿Qué hace prestamo.linea_ids.equipo_id.write(...)? ¿Por qué no hace falta un for para cada equipo?
Respuesta: Cambia el estado de todos los equipos relacionados de una sola vez. Odoo permite aplicar write a varios registros juntos.

PASO 5. REGLAS DEL PRÉSTAMO
1. El campo equipo_id ya filtra los equipos disponibles. ¿Por qué hace falta el TODO 5?
Respuesta: El filtro ayuda al elegir el equipo, pero el estado puede cambiar después. La validación comprueba otra vez que siga disponible al prestar.

2. ¿En qué momento se ejecuta un método con @api.constrains? ¿Y la validación de action_prestar?
Respuesta: @api.constrains se ejecuta al guardar cambios en los campos indicados. action_prestar se valida cuando se pulsa el botón Prestar.

PASO 6. CONTACTO, KANBAN Y BÚSQUEDA
1. ¿Qué pasa si arrastra una tarjeta del kanban a otra columna? ¿Por qué?
Respuesta: El equipo pasa a la columna nueva y cambia su estado, porque las columnas representan los valores del campo estado.

2. El campo prestamo_ids se agregó a res.partner. ¿Se crea una columna nueva en la tabla de contactos? Explique.
Respuesta: No. Es un campo One2many que muestra los préstamos relacionados. La relación se guarda desde el Many2one partner_id del préstamo.

# RETO
1. Marcar atrasado.
Respuesta: Se agregó un botón que cambia el estado a Atrasado solo si el préstamo sigue Prestado y la fecha de devolución ya pasó.

2. Colores en la lista.
Respuesta: Se agregó color rojo para los préstamos atrasados y gris para los devueltos.

3. Veces prestado.
Respuesta: Se agregó un contador que muestra cuántos registros de línea tiene el equipo en los préstamos.

4. Mantenimiento.
Respuesta: Se agregaron botones para enviar un equipo a mantenimiento y volver a marcarlo disponible. No permite enviar a mantenimiento un equipo prestado.
