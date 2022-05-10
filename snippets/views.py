######################################################################################
''' 
    utilisation de du decorateur @api_view basé sur les fonctions
'''
######################################################################################
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import *
from snippets.serializers import *


@api_view(['GET','POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request, id, format=None):
    try:
        snippet = Snippet.objects.get(id=id)
    except snippet.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializers = ProductSerializers(queryset, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("INSERTION EFFECTUEE AVEC SUCCES")
        return Response("SAISIE INCORRECT")

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except product.DoesNotExist:
        return Response("le produit que vous demander n'existe pas...")

    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Modification effectuée avec succès")
        return Response("Données invalide")
    
    elif request.method == 'DELETE':
        product.delete()
        return Response("Vous venez de supprimer un produit")



############################################################################################
'''
    utilisation de la classe APIView (vue basé sur les classe)
'''
############################################################################################
from rest_framework.views import APIView
from django.http import Http404 

class list_produit(APIView):

    def get(self, request, format=None):
        queryset = Product.objects.all()
        serializers = ProductSerializers(queryset, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("produit ajouter avec succes!!!!")
        return Response("Erreur d'insertion....")

class update_product(APIView):

    def get_object(self, pk):
        try:
            obj=Product.objects.get(pk=pk)
        except obj.DoesNotExist:
            raise Http404
             
        
    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = ProductSerializers(obj)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        serializer = ProductSerializers(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

############################################################################################
'''
    utilisation des vue generique (vue basé sur les classe)
'''
############################################################################################
from rest_framework import generics

class snippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
class snippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer