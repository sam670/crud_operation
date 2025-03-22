from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Item
from .serializers import ItemSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


################## token creation api
@api_view(['POST'])
def create_token(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {"message": "Username and password are required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticate(username=username, password=password)

    if user is None:
        return Response(
            {"message": "Invalid credentials.","status":status.HTTP_401_UNAUTHORIZED},
            status=status.HTTP_401_UNAUTHORIZED
        )

    refresh = RefreshToken.for_user(user)
    return Response(
        {'refresh': str(refresh), 'access': str(refresh.access_token),"status":status.HTTP_200_OK},
        status=status.HTTP_200_OK
    )


############## data creation api 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_item(request):
    
    if isinstance(request.data, list):
        serializer = ItemSerializer(data=request.data, many=True)
    else:
        serializer = ItemSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save() 
        
        return Response(
            {"message": "All items inserted successfully", "status":status.HTTP_201_CREATED},
        )
    else:
        return Response(
            {"message": "Failed to insert items","status":status.HTTP_400_BAD_REQUEST},
            
        )

class CustomPagination(PageNumberPagination):
    page_size = 5 
    page_size_query_param = 'page_size'
    max_page_size = 50


######### getting data api
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_items(request):
    try:
        items = Item.objects.all()
        
        if not items.exists():
            return Response(
                {
                    "data": [],
                    "count_of_data": 0,
                    "count_of_pages": 0,
                    "status": status.HTTP_200_OK,
                    "message": "No items found."
                },
                status=status.HTTP_200_OK
            )
        
        paginator = CustomPagination()
        paginated_items = paginator.paginate_queryset(items, request)
        serializer = ItemSerializer(paginated_items, many=True)
        
        total_items = items.count()
        page_size = paginator.page_size
        count_of_pages = (total_items + page_size - 1) // page_size
        
        return Response(
            {
                "data": serializer.data,
                "count_of_data": total_items,
                "count_of_pages": count_of_pages,
                "status": status.HTTP_200_OK,
                "message": "Items retrieved successfully."
            },
            status=status.HTTP_200_OK
        )
    
    except Exception as e:
        return Response(
            {
                "data": [],
                "count_of_data": 0,
                "count_of_pages": 0,
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": f"An error occurred: {str(e)}"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
        
###### deleting data api
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_item(request, pk):
    try:
        item = Item.objects.get(id=pk)        
        item.delete()
        
        return Response(
            {"message": "Item successfully deleted.","status":status.HTTP_204_NO_CONTENT},
            status=status.HTTP_204_NO_CONTENT
        )
    except Item.DoesNotExist:
        return Response(
            {"error": "Item not found.","status":status.HTTP_404_NOT_FOUND},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {"error": f"An error occurred: {str(e)}","status":status.HTTP_500_INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


### updating data api
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_item(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(
            {"error": "Item not found.", "status": status.HTTP_404_NOT_FOUND},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = ItemSerializer(item, data=request.data)
    
    if serializer.is_valid():
        if serializer.validated_data == serializer.initial_data:
            return Response(
                {"message": "No changes detected. Item is already up-to-date.", "status": status.HTTP_200_OK},
                status=status.HTTP_200_OK
            )

        serializer.save()
        return Response(
            {"message": "Item successfully updated.", "data": serializer.data, "status": status.HTTP_200_OK},
            status=status.HTTP_200_OK
        )
    
    return Response(
        {"error": "Invalid data", "details": serializer.errors, "status": status.HTTP_400_BAD_REQUEST},
        status=status.HTTP_400_BAD_REQUEST
    )

