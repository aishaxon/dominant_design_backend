from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import filters, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

from .models import *
from .serializers import *

class BaseListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class AdminOnlyMixin:
    permission_classes = [IsAdminUser]


class ServiceList(BaseListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(AdminOnlyMixin, RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class PortfolioList(BaseListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioDetail(AdminOnlyMixin, RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class VideoProjectList(BaseListAPIView):
    queryset = VideoProject.objects.all()
    serializer_class = VideoProjectSerializer


class VideoProjectDetail(AdminOnlyMixin, RetrieveUpdateDestroyAPIView):
    queryset = VideoProject.objects.all()
    serializer_class = VideoProjectSerializer

class GalleryList(BaseListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryDetail(AdminOnlyMixin, RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class PartnerList(BaseListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerDetail(AdminOnlyMixin, RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class PricingList(BaseListAPIView):
    serializer_class = PricingSerializer

    def get_queryset(self):
        queryset = Pricing.objects.all()

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class PricingDetail(AdminOnlyMixin, RetrieveUpdateDestroyAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

class TeamList(BaseListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ContactCreate(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        try:
            send_mail(
                subject="Yangi murojaat",
                message=str(request.data),
                from_email="aishaxon0010@gmail.com",
                recipient_list=["aishaxon0010@gmail.com"],
                fail_silently=False,
            )
        except Exception :
            return Response(
                {"error": "Xatolik mavjud"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return response


class TeamDetail(AdminOnlyMixin, RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer