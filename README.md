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
---- Cuando levantas el servidor ya es muy intuitivo como hacer las pruebas hasta este punto.

## CREACION DE NUESTRO PRIMER VIEWSET:
* Usan funciones de operadores de modelo:
  - def list(): enlista objetos.
  - create(): crea.
  - retrive(): obtiene un objeto específico.
  - partial_update()
  - destroy(): elimina
* Qué son los Viewsets?
 - Se encarga de la lógica común.
 - Buenos para operaciones standard de BD.
 - Forma más rápida de hacer una interfaz con una BD.
* Cuándo usamos viewsets?
 - CRUD simple.
 - API simple.
 - poca personalización de la lógica.
 - Trabaja con estructuras de datos normales.

* Para hacer uso de *viewsets* primero importamos *from rest_framework import viewsets* en nuestro archivo *views.py*
* Tener en cuenta que cuando vamos a crear la clase del view set heredamos ViewSet por lo que pasamos como parámetro *viewsets.ViewSet*

# Funcionamieto (SUPER IMPORTANTE):
- En el APIView definimos las funciones basados en el método que queremos correr, por ejemplo un get, put, patch, post, delete.... para el viewset corres funciones que normalmente representan acciones que normalmente se correrían en un API típico.

## CONTINUACION DE LOS VIEWSETS:
* Ya definido el viewset de prueba nos quedaría de la siguiente manera:

![image](https://user-images.githubusercontent.com/84333525/138752882-d1bf4e2e-b37f-4c7a-91ec-31d6f5486b4e.png)

* Después de creado debemos pasar a crear la ruta por la cual el viewset será accedido esto en el archico *urls.py*
* ## IMPORTANTE --> Las rutas en el archivo *urls.py* en los viewsets se manejan de forma distina a las APIViews debido a que los viewsets se manejan mediante *routers*
* Por lo que primero importamos *from rest_framework.routers import DefaultRouter*

![image](https://user-images.githubusercontent.com/84333525/138754517-0a3df1b4-ef04-4446-a648-ecd50b9a6810.png)

* Luego tenemos que crear una variable router (por convención el nombre) donde inicializmos la clase DefaultRouter.
* Luego ya podemos registrar todos los viewsets que necesitemos.
* Por último en los *urlpatterns* agregamos un nuevo path, en el que utilizamos el include para adicionar todas las urls que esten registradas en el router.

** En este ejemplo podemos usar el mismo serializer utilizado por el APIView porque estaremos realizando las mismas funciones, o sea convirtiendo el mismo json que solo tiene nombre, igual en todo caso de dudas ver video en el minuto 1h:00.
- Recordar que al igual que en el APIView debemos crear la variable serializer y vincularla con el serializer que ya tenemos hecho.

![image](https://user-images.githubusercontent.com/84333525/138759450-e36fd72b-b968-44e5-a6bb-a4706aa74bc8.png)

![image](https://user-images.githubusercontent.com/84333525/138759667-a946188e-21b6-4110-918e-aa97178473a6.png)

# NOTA IMPORTANTE *** EN EL EJEMPLO DEL VIDEO EN EL MINUTO 1H:04M NO ME FUNCIONO EL METODO GET COMO EN EL EJEMPLO.

## API PARA PERFIL DE USUARIOS
### Qué debemos hacer?
- Manejar registro nuevo de usuarios.
- Validar datos de perfil.

### Enlistar perfiles existentes
- Buscar perfiles.
- Email y nombre.

### Ver perfil específico
- Id del perfil

### Actualiza perfil de usuarios loguiados.
- Cambiar nombre, email y password.

### Borrar perfil

## El próximo paso lógico cuando ya sabemos que debemos hacer es definir las urls.
* URLs del API
 - /api/profile/ --> enlistar perfiles en http GET, crear en http POST
 - /api/profile/<profile_id> --> ver perfil específico en http GET, actualiza objeto en http PUT, borrar en http DELETE

* Como estaremos trabajando con el perfil de usuario es momento de crear el serializer de perfil de usuario que es el que nos permitirá interactuar con la información (ver definición de serializer).
* Ya ubicados en el archivo *serializer.py* creamos la clase UserProfileSerializer

![image](https://user-images.githubusercontent.com/84333525/138761776-172a4719-4631-4926-add5-7f25fca21c86.png)

Tener en cuenta que heredamos en este caso de *serializers.ModelSerializer* porque partiremos a partir de un modelo determinado.

![image](https://user-images.githubusercontent.com/84333525/138762032-24b87fcb-4888-4dcb-8610-dd417d3362d2.png)

Importamos los modelos para poder trabajar con ellos.

* Creamos una clase META, este es un feature de python que ya vi antes en el curso de Django, no olvidar estudiar nuevamente el código y readme.md de ese curso. En esa clase Meta es donde vinculamos el modelo con el serializer (segun recuerdo en esa clase meta en el curso de django vinculabamos el modelo con un formulario :/)
* Para el método create del serializer sobre escribimos el método create del modelo, para ello creamos una variable usuario en la que guardamos la llamada al método create del modelo.

* Una vez que ya tenemos los métodos que necesitamos en el serializer pasamos a crear el viewset en en el archivo *views.py*
* Tener en cuenta que en la nueva clase que se crea para el nuevo viewset de la gestion de usuario se le pasa como parámetro *viewsets.ModelViewSet* porque se estará trabajando con un modelo determinado.
* Creamos el serializer_class para poder vincular la data que nos llega del request con el serializer
* Luego hacemos un query para traer todos los objetos de ese tipo que han sido creados
* Registramos una url para poder acceder al serializer desde el buscador.
 
 ![image](https://user-images.githubusercontent.com/84333525/138783464-63b5484d-dc1a-4eb1-ad80-f6cc8c9d692b.png)

No tenemos que especificarle un basename debido a el *UserProfileViewSet* esta usando queryset, cuando ya estamos llamando a los objetos de por si, no es necesario definir los nombres.

![image](https://user-images.githubusercontent.com/84333525/138783573-b0458369-ab51-4e53-9f35-bf73e1945376.png)

* Luego ya podemos verificar al correr el servidor que esta funcionando correctamente

![image](https://user-images.githubusercontent.com/84333525/138784181-47b2dd82-b67e-440b-98f1-d20248838fe6.png)

*** EN ESTE PUNTO TENEMOS QUE ASEGURAR QUE NO TODOS LOS USUARIOS PUEDAN CREAR USUARIOS ***

## PERMISOS

* Para ello creamos en nuestra app un nuevo archivo *permissions.py*

![image](https://user-images.githubusercontent.com/84333525/138785708-7a64036e-d30a-4db0-8fdc-28343aea35b7.png)

Se logra que los usuarios loguiados puedan ver otros perfiles de usuario pero solo puedan cambiar su propio perfil.

**De esta manera ya tenemos nuestro primer permiso personaizado, que debemos utilizar en nuestro viewset.

* Para ello vamos al archivo *views.py* e importamos *from rest_framework.authentication import TokenAuthentication*
 - TokenAuthentication es lo que vamos usar para que nuestros usuarios puedan autenticarse en nuestra API. Funiona generando un random token string, cada vez que un usuario se crea o hace login, cada ves que el usuario hace un request debemos verificarlo.
* También importamos de nuestra app el archivo de permissions.py

![image](https://user-images.githubusercontent.com/84333525/138786588-a11c0f98-25db-4d91-8957-569f03d2c44c.png)

Aquí le estaoms diciendo por el metódo que utilizará para autenticarse y los permisos que tendrá.
- Luego ya podemos correr el servidor y verificar que ya no podemos editar un usuario, solo verlo.

## FILTROS
* Para poder usar los filtros importamos filter desde el django_restframework.
* NOTA: Es obligatorio poner las comas que señalo en la próxima imagen porque Python necesita saber que es una tupla.

![image](https://user-images.githubusercontent.com/84333525/138787114-e1028049-eab3-4851-a8a1-a5e7b72425cc.png)


## MODULO DE LOGIN
* Para hacer la autenticación por token, importamos *from rest_framework.authtoken.views import ObtainAuthToken* 
 
 ![image](https://user-images.githubusercontent.com/84333525/138790505-f2ca40a4-71ef-4e44-9429-eab6674f26db.png)

* Creamos la clase que se va a encargar de la autenticación del usuario

![image](https://user-images.githubusercontent.com/84333525/138790815-f2083a20-37af-4eeb-bfe6-bc2926f6f24e.png)

Lo que esto hace es que le adiciona las clases de renderer a nuestro ObtainAuthToken que va habilitarlo en el admin de Django

* Luego que ya tenemos la clase debemos adicionar una nueva url para poder acceder a ese método:
  
  ![image](https://user-images.githubusercontent.com/84333525/138791095-64c00328-aea1-4479-8d06-af535cae2615.png)


## API FEED DEL PERFIL DEL USUARIO
Qué necesitamos poder hacer?

1. Crear nuevos items para el feed.
2. Actualizar feed (sólo si está logueado).
3. Borrar items.
4. Ver todos los usuarios status updates.

### API URLs
* /api/feed/ --> list items, get, post
* /api/feed/<feed_item_id> --> maneja items específicos, get, put, delete

## CREACION DEL FEED
* El primer paso para crear un feed es definir el modelo, todos los datos que contendrá un feed.
  - Importamos los settings para obtener la configuración que ya tenemos establecida allí
  
  ![image](https://user-images.githubusercontent.com/84333525/138792251-6a82af15-2f6d-4b2a-ab68-93c4c3db630b.png)

  ![image](https://user-images.githubusercontent.com/84333525/138792590-c6ada9ec-f320-4f57-b5ad-0a82e1104566.png)

Lo hacemos de esa manera porque cuando actualizamos el AUTH_USER_MODEL en settings se actualiza automático en todas partes y así evitamos otros problemas ...

* Siempre que hacemos una relación uno a uno además del foreignKey tenemos que definir la acción a tomar en *on_delete*

* Así quedaría nuestra clase:

![image](https://user-images.githubusercontent.com/84333525/138793138-acb54bcf-a17b-4688-8cd1-3e0eb13d136b.png)

* Luego de haber creado el nuevo modelo, debemos pasar a correr las migraciones.
* Justo después lo agregamos al admin de django para poder manejarlo desde el panel de administración.

![image](https://user-images.githubusercontent.com/84333525/138793450-1c2ae00c-cb3f-48c5-a5e1-93bdeff29e58.png)

* Luego como estaremos recibiendo información debemos crear un serializer para manejar esos datos, para ello vamos al archivo *serializer.py* y creamos la clase *ProfileFeedItemSerializer*

![image](https://user-images.githubusercontent.com/84333525/138793804-4a562ed3-be57-48d0-9263-a7f94658dbc0.png)

Esto configura el serializador para que trabaje con el modelo indicado.

* Una vez definidos todos los pasos anteriores pasamos a crear el ViewSet:
 
 ![image](https://user-images.githubusercontent.com/84333525/138794959-6a3accbf-ce15-41c1-a3f5-11ed42a5b674.png)

- Usamos *authentication_classes* porque solo queremos realizar la acción si el usuario está autenticado.
- En el serializer pusimos el *user_profile* a read_only porque queremos configurarlo basado en el usuario que está autenticado.
- Luego creamos una función que se encarga de setear el perfil de usuario, para el usuario que está logeado.

![image](https://user-images.githubusercontent.com/84333525/138795325-00e3d811-638c-4adc-a141-e1901361d60c.png)


* Por último configuramos el router en el archivo *urls.py*:

![image](https://user-images.githubusercontent.com/84333525/138795522-e4ebd0ff-d3c0-419e-86c8-a579748c954a.png)

* Adicionamos un nuevo permiso que nos permita que solo el propio usuario pueda actualizar su feed:

![image](https://user-images.githubusercontent.com/84333525/138795952-8bd24426-19c2-4fa9-ade3-11e73b6787cb.png)

* Para agregar el nuevo permiso en nuestro viewset primero importamos *from rest_framework.permissions import IsAuthenticatedOrReadOnly*

![image](https://user-images.githubusercontent.com/84333525/138796394-b4328a3b-ee42-40c6-a807-784ac4bd2b1d.png)

Con esto permitimos que los usuarios que no estan loguiados también puedan leer del endpoint, para evitar esto podemos cambiar el import por *IsAuthenticated*




