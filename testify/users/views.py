from .serializers.registration_serializers import RegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema, inline_serializer


class RegisterView(APIView):
    """API endpoint for user registration."""
    permission_classes = [AllowAny]  # Allow access to all

    @extend_schema(
        summary="Register a new user",
        description=(
            "This endpoint allows new users to register by providing their username, "
            "password, and email. If the registration is successful, a token is returned."
        ),
        request=RegisterSerializer,
        responses={
            201: inline_serializer(
                name="RegistrationSuccess",
                fields={
                    "token": serializers.CharField(help_text="The authentication token for the newly registered user"),
                },
            ),
            400: inline_serializer(
                name="RegistrationError",
                fields={
                    "error": serializers.JSONField(help_text="Details of the validation errors."),
                },
            ),
        },
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Create user
            token, created = Token.objects.get_or_create(user=user)  # Create token
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """API endpoint for user login."""
    permission_classes = [AllowAny]  # Allow access to all users

    @extend_schema(
        summary="User Login",
        description=(
            "This endpoint allows users to log in by providing their username and password. "
            "If the credentials are valid, an authentication token is returned."
        ),
        request=inline_serializer(
            name="LoginRequest",
            fields={
                "username": serializers.CharField(help_text="The username of the user."),
                "password": serializers.CharField(
                    write_only=True, help_text="The password of the user."
                ),
            },
        ),
        responses={
            200: inline_serializer(
                name="LoginSuccess",
                fields={
                    "token": serializers.CharField(help_text="The authentication token for the logged-in user."),
                },
            ),
            401: inline_serializer(
                name="LoginError",
                fields={
                    "detail": serializers.CharField(help_text="Error message if login fails."),
                },
            ),
        },
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(
                {'detail': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(APIView):
    """API endpoint for user logout."""
    permission_classes = [IsAuthenticated]  # User must be authenticated

    @extend_schema(
        summary="User Logout",
        description=(
            "This endpoint allows authenticated users to log out by deleting their authentication token. "
            "The token is retrieved from the `Authorization` header."
        ),
        responses={
            200: inline_serializer(
                name="LogoutSuccess",
                fields={
                    "detail": serializers.CharField(help_text="Confirmation that the user has logged out."),
                },
            ),
            400: inline_serializer(
                name="LogoutError",
                fields={
                    "detail": serializers.CharField(help_text="Error message if logout fails."),
                },
            ),
        },
    )
    def post(self, request):
        try:
            # Retrieve token from Authorization header
            token = request.auth

            if token:
                # Delete token
                token.delete()
                return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
            return Response({'detail': 'No token provided.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
