
# Create your views here. To display views
#Query the database for all customers
#Pass that database queryset into the serializer we just created,
# so that it gets converted into JSON and rendered
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CustomerSerializer
from .models import Customer



class CustomerViewSet(viewsets.ModelViewSet):


    #queryset = Customer.objects.all().order_by('name')
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

@api_view(['GET', 'POST'])
def customer_list(request, format=None):
    """
    List all customers, or create a new customer.
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def customer_detail(request, name, format=None):
    """
    Retrieve a customer.
    """
    try:
        customer = Customer.objects.get(name=name)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
