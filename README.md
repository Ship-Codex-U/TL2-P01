# Practica 01

Crea un analizador léxico que valide varias cadenas dadas por el usuario.
El programa debe identificar los siguientes Token y asignar su correspondiente categoría

- 0 --- Tipo de dato
- 1 --- Identificador
- 2 --- constante
- 3 ---   ;
- 4 ---   ,
- 5 ---   (
- 6 ---   )
- 7 ---   {
- 8 ---   }
- 9 ---   =
- 10 ---  if
- 11 ---  while
- 12 ---  return
- 13 ---  else
- 14 ---  for
- 15 ---  opAdición
- 16 ---  opMultiplicacion
- 17 ---  opLogico
- 18 ---  opRelacional
- 19 ---  $


Siendo:
- opAdision: + -
- opMultiplicacion: * / << >>
- opLogico: &&  ||
- opelacional: < > >= <= == !=
- constante: cualquier numero #, y pi
- tipo de dato: int float char void string 

recuerda mostrar al final la cantidad de tokens encontrados de cada categoría o si encontró algún error.


## Descarga he instalación/configuración del proyecto

Clonar  repositorio

```bash
git clone
```

## Settear ambiente local
(Version de python: 3.12.1)

1. Crear un entorno virtual con **venv** dentro de la nueva carpeta que se creo al clonar el proyecto.

```bash
python -m venv nombre-entorno-virtual
```

2. Activar el entorno virtual creado.
```bash
nombre-entorno-virtual\Scripts\activate
```

3. Instalar los paquetes necesarios que requiere el proyecto para funcionan que vienen indicados en el archivo **requirements.txt**.
```bash
pip install -r requirements.txt
```

Nota: la aplicación para realizar y editar la interfaz del proyecto (Qt Design - design.exe) lo podras encontrar dentro de tu entorno virtual en la siguiente ruta
```bash
entorno-virtual-creado/Lib/Pyside6/
```

## Antes de realizar tu primer push.......
Asegurate que en tu archivo **.gitignore** aparezca por lo menos el siguiente renglon:

nombre-entorno-virtual-creado/  <------------ para que al momento de subir tus cambios no subas paquetes y librerias innecesarios a la repo que hagan que pese de mas.