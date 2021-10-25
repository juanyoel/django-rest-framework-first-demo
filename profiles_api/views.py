from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloApiView(APIView):
    """ Api View de Prueba """

    def get(self, request, format=None):
        """ Retornar lista de caracteristicas del APIView """
        an_apiview = [
            'Usamos metodos http como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmente a los URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})


