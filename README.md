# IT Ticket Management System

Este proyecto implementa un **sistema modular de gestión de tickets IT**, utilizando tres patrones de diseño fundamentales:

* **Factory Method** (Creacional)
* **Decorator** (Estructural)
* **Observer** (Comportamiento)

El objetivo es mostrar cómo estos patrones permiten crear un sistema flexible, extensible y desacoplado.

---

## Funcionalidades principales

* Creación de distintos tipos de tickets (Network, Software).
* Notificaciones automáticas a usuarios cuando un ticket es resuelto.
* Decoración dinámica de tickets (por ejemplo, marcar como urgente).
* Sistema completamente modular y fácil de extender.

---

## Patrones de diseño utilizados

### **1. Factory Method**

Gestiona la creación de tickets mediante una fábrica centralizada (`TicketFactory`).
Permite instanciar distintos tipos de tickets sin acoplar el código principal.

### **2. Observer**

Permite que los usuarios (observadores) reciban notificaciones cuando un ticket cambia de estado.
El ticket actúa como `Subject` y los usuarios como `Observer`.

### **3. Decorator**

Permite extender dinámicamente la funcionalidad de un ticket (por ejemplo, añadir prioridad urgente) sin modificar la clase original.

---

## Estructura del proyecto

* **interfaces.py** → Define `Observer`, `Subject` y la clase abstracta `Ticket`.
* **implements.py** → Implementa `ITUser`, `NetworkTicket`, `SoftwareTicket`.
* **factory.py** → Implementa el patrón Factory Method.
* **decorators.py** → Implementa el patrón Decorator.
* **main.py** → Punto de entrada del programa.

---

## Cómo ejecutar

```bash
python main.py
```

