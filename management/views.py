from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from management.models import Company
from management.serializers import CompanySerializer
from management.queries import company_query


class CompanyViewNoPK(generics.ListAPIView):
    model = Company
    queryset = company_query()
    serializer_class = CompanySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CompanyView(generics.RetrieveUpdateAPIView):
    queryset = company_query()
    serializer_class = CompanySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CreateCompanyCreateCompany(generics.CreateAPIView):
    model = Company
    serializer_class = CompanySerializer
    queryset = company_query()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class DeleteCompanyById(generics.DestroyAPIView):
    model = Company
    serializer_class = CompanySerializer
    queryset = company_query()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Company successfully deleted"}, status=status.HTTP_200_OK)