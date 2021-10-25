# django-rest-framework-first-demo

## INSTALACION:
* Debemos instalar el paquete *django* --> pip install django
* Debemos instalar el paquete *djangorestframework* --> pip install djangorestframework
* Iniciamos el proyecto django-admin startproject [nombreProject]
* Creamos la app django startapp [nombreApp]
* Inlcuimos el nombre de la app en el archivo settings.py en la sección INSTALLED_APPS
* También debemos incluir los siguientes namespaces en ese archivo --> *rest_framework, rest_framework.authtoken*

![image](https://user-images.githubusercontent.com/84333525/138706688-e29a15ae-ba9d-47b3-ad6e-90b3975c8f90.png)

## MODELOS:
* Nota: Django trae por defecto un modelo para trabajar con los usuarios (En este ejemplo se va a sobre-escribir). La diferencia está que al sobre escribirlo nos permitirá hacer login con email, y con django deberíamos hacerlo con el usuario.
* Debemos importar en el archivo models.py *from django.contrib.auth.models import AbstractBaseUser*
* Debemos importar en el archivo models.py *from django.contrib.auth.models import PermissionsMixin*
* * Debemos importar en el archivo models.py *from django.contrib.auth.models import BaseUserManager*

![image](https://user-images.githubusercontent.com/84333525/138712202-f96f9398-6161-4d59-9314-e7ea92fd9357.png)

* En este caso creamos el model UserProfile que contendrá los campos con los que guardaremos un nuevo usuario en la BD, debemos pasarle como parámetro AbstractBaseUser, que nos permitirá heredar las principales funciones del trabajo con usuario que tiene Django, además PermissionsMixin que nos permite heredar propiedades que veremos a continuación como en la creación del super usuario la propiedad *is_superuser*

* Luego de ya haber determinado que campos tendrá el usuario entonces en el archivo *settings.py* le especificamos que modelo de usuario utilizar:

![image](https://user-images.githubusercontent.com/84333525/138713565-a2e330cc-0661-4b2c-9ae1-8a95d1e33597.png)

Así de esta manera se utilizará ese modelo para registro y autenticación.

* De este modo ya podemos primero crear las migraciones necesarias *python mange.py makemigrations* y luego corremos la migración: *python manage.py migrate*.
* Luego pasamos a crear un super usuario con el siguiente comando en el cli: *python manage.py createsuperuser*
* Para dar permisos en el módulo de administración de Django sobre la "administración" de usuarios recordemos que debemos agregar los modelos a los que queramos tener acceso desde el modulo de adminitración en el archivo *admin.py* 

![image](https://user-images.githubusercontent.com/84333525/138716885-5d685f37-16b6-4785-a3d0-9df987f4afad.png)

## VISTAS DE DJANGO REST FRAMEWORK:
* Tenemos dos maneras de mostrar la información de nuestros modelos en el API:
 - API View
 - View Set
* En este caso de estudio utilizaremos API View por:
 - Nos permite más control sobre la lógica.
 - Es bueno para lógicas complejas.
 - Es utilizado para llamar a otros APIs.
 - Es utilizado para trabajar con archivos locales.
 * Qué es?:
   - Usa métodos HTTP estandard
     * get()
     * post()
 * Cuándo usar APIView?:
   - Si necesitas control de lógica.
   - Proceso de archivos y renderizar respuesta sincronizada.
   - Llamada a otros APIs / servicios.
   - Acceso a archivos locales o datos.


## CREACION DE NUESTRO PRIMER APIVIEW:
* En el archivo *views.py* de nuestra app, ya no necesitaremos el import *from django.shortcuts import render* que viene por defecto en su lugar lo sustituimos por los siguientes:
 - from rest_framework.views import APIView
 - from rest_framework.response import Response

* Creamos la clase con el APIView deseado y dentro las funciones que se estarán ejecutando.
* Nota: Cada función que se cree debe retornar un response object.
* Esta respuesta va a covertir la información en formato json y para ello esta iformación debe ser una lista o un diccionario.
* Así nos quedaría definida nuestra APIView báscia Hola mundo!:

![image](https://user-images.githubusercontent.com/84333525/138725069-ae6b5aa3-30bf-4f52-82c6-0bffcfd0013c.png)

## CREACION DE LA URL:
* Luego de haber creado el APIView anterior debemos crear una url para tener acceso a dicha APIView
* Para ello creamos el archivo *urls.py* de nuestra app (Esto ya lo vimos en el curso anterior de Django).
* En el archivo *urls.py* general recordar que tenemos que adicionar *include* en las importaciones para poder adicionar las rutas urls de nuestra app, como señalaré en el la próxima imagen.

![image](https://user-images.githubusercontent.com/84333525/138726405-d183dde5-7906-40f0-9a6d-9daf56135278.png)

* Ya con esto tenemos acceso a las urls de nuestra app, la cuál modificaremos de la siguiente manera para tener acceso mediante la url al APIView creado con aterioridad:

![image](https://user-images.githubusercontent.com/84333525/138727459-f9e82a9a-4ae9-4fd6-9b73-80d11bc71886.png)


## CREACION DEL SERIALIZADOR
* Luego de creado los modelos, el APIView, y una vez definidas las urls de acceso a las mismas, pasamos a la creación de los serializadores.
* --El serializador nos permite convertir objetos de python en json y viceversa.--
* Un serializador es similar a un formulario de django dónde lo defines y tienes los diferentes campos que quieres ingresar para convertir en información json en este caso.
* Es a través de nuestro serializador que agregamos el *input* a nuestro API, por lo que si se qiere agregar algún tipo de post o update es a través del serializados para poder recivir el contenido.
* Para ello creamos un nuevo archivo en la app, llamada *serializers.py*.
* Es buena práctica mantener todos los serializers en un mismo archivo.
* Dentro del archivo creado anteriormente ponemos el código de nuestro serializer de prueba: como observación no olvidar que hereda de serializer.Serializer

![image](https://user-images.githubusercontent.com/84333525/138729345-2e673b2c-2224-4595-be11-1ea36f019b7c.png)

*Nota: cuando creamos un campo de tipo CharField siempre tenemos que definirle una longitud.

* Luego de todos los pasos anteriores pasamos a crear nuestro método post para nuestro APIView
 - Para ello creamos los imports necesarios:

  ![image](https://user-images.githubusercontent.com/84333525/138730084-c4490f7e-d66c-4950-89ed-86ae99ba418d.png)
 
 - status tiene varios códigos http que podemos usar cuando estamos haciendo uso de nuestro api, por lo que usaremos esos códigos en las respuestas.
 - Le adicionamos la clase que vincula el APIView con el serializer que vimos anteriormente:

  ![image](https://user-images.githubusercontent.com/84333525/138730545-e20f6f47-d443-4222-826e-1bd4a062e126.png)


 -  Para hacer el método post primero creamos la variable serializer y ahí almacenamos la info que nos llega a través de la petición, como veremos en la próxima imagen:
    *self.serializer_class* ese método es una clase que viene con el APIView y configura nuestra clase para trabaja con el APIView.
    - Esta sería la manera standard para obtener el serializdor cuando estamos trabando en un view basado en clases.
    - Luego siempre tenemos que validar la data del serializer *if serializer.is_valid():*
    - Dentro guardamos la información que necesitamos de la siguiente forma --> *name = serializer.validated_data.get('name')*
    - Este *name* hace referencia al mismo name definido en el *HelloSerializer*, (supongo que si tuviera más campos se debería hacer lo mismo)

## Otros métodos:
  
  ![image](https://user-images.githubusercontent.com/84333525/138735723-dd02c858-e0e8-48b6-b5c3-d8fac43e0214.png)
  
  - Nota: en estos casos en los argumentos el *pk* representa el primary key, porque para la utilzación de estos métodos al momento de estar vinculados a una BD, se necesita una llave por la cual actualizar o realizar la operación correspondiente en la BD.
  - En este caso como no utilizaremos el id, ponemos pk=None, supongo que más adelante en el curso ya si lo vincules con alguna BD.

## PRUEBA DE LOS METODOS ANTERIORES:

