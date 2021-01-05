from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('category/new/', views.NewCategory.as_view(), name='NewCategory'),
    path('category/<int:pk>/update', views.CategoryUpdate.as_view(), name='CategoryUpdate'),
    path('category/<int:pk>/delete', views.CategoryDelete.as_view(), name='CategoryDelete'),
    path('category/', views.CategoryList.as_view(), name='CategoryList'),
    path('delivery/new/', views.NewDeliveryOrder.as_view(), name='NewDeliveryOrder'),
    path('delivery/new/modal/', views.NewDeliveryOrderModal.as_view(), name='NewDeliveryOrderModal'),
    # path('delivery/vendor/new/', views.NewDeliveryOrderSelectVendorView, name='NewDeliveryOrderSelectVendor'),
    path('delivery/items/', views.DeliveryItemList.as_view(), name='DeliveryItemList'),
    path('delivery/<int:delivery_id>/items/<int:pk>/delete/modal/', views.DeliveryItemDeleteModal.as_view(), name='DeliveryItemDeleteModal'),
    path('delivery/<int:delivery_id>/items/<int:pk>/update/modal/', views.DeliveryItemUpdateModal.as_view(), name='DeliveryItemUpdateModal'),
    # path('delivery/<int:delivery_id>/item/<int:cmsitem_id>/add/', views.DeliveryOrderAddDeliveryItem.as_view(), name='DeliveryOrderAddDeliveryItem'),
    path('delivery/<int:delivery_id>/item/add/', views.DeliveryOrderAddDeliveryItem.as_view(), name='DeliveryOrderAddDeliveryItem'),
    path('delivery/<int:pk>/update/modal/', views.DeliveryOrderUpdateModal.as_view(), name='DeliveryOrderUpdateModal'),
    path('delivery/<int:pk>/delete/modal/', views.DeliveryOrderDeleteModal.as_view(), name='DeliveryOrderDeleteModal'),
    # path('delivery/<int:delivery_id>/item/<int:cmsitem_id>/add/', views.DeliveryOrderAddItemView, name='DeliveryOrderAddItem'),
    # path('delivery/<int:delivery_id>/new/modal/', views.DeliveryOrderAddDrugModal.as_view(), name='DeliveryOrderAddDrugModal'),
    path('delivery/<int:delivery_id>/', views.DeliveryOrderDetail, name='DeliveryOrderDetail'),
    path('delivery/', views.DeliveryOrderList.as_view(), name='DeliveryOrderList'),
    # path('item/new/<int:vendor_id>', views.NewItemFromVendor.as_view(), name='NewItemFromVendor'),
    path('item/new/', views.NewItem.as_view(), name='NewItem'),
    # path('item/new/modal/<int:drug_id>', views.NewItemModal.as_view(), name='NewItemModal'),
    # path('item/selectdrug/', views.ItemSelectDrugView, name='ItemSelectDrugView'),
    path('item/<int:pk>/update/modal/', views.ItemUpdateModal.as_view(), name='ItemUpdateModal'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='ItemDelete'),
    path('item/<int:pk>', views.ItemDetail.as_view(), name='ItemDetail'),
    path('items/', views.ItemList.as_view(), name='ItemList'),
    # path('vendor/select/modal/', views.VendorSelectModal.as_view(), name='VendorSelectModal'),
    path('vendor/new/', views.NewVendor.as_view(), name='NewVendor'),
    # path('vendor/new/modal/', views.NewVendorModal.as_view(), name='NewVendorModal'),
    path('vendor/<int:pk>/update/modal', views.VendorUpdateModal.as_view(), name='VendorUpdateModal'),
    path('vendor/<int:pk>/update/', views.VendorUpdate.as_view(), name='VendorUpdate'),
    # path('vendor/<int:pk>/delete/', views.VendorDelete.as_view(), name='VendorDelete'),
    path('vendor/<int:pk>/delete/modal/', views.VendorDeleteModal.as_view(), name='VendorDeleteModal'),
    path('vendor/<int:pk>', views.VendorDetail.as_view(), name='VendorDetail'),
    path('vendors/', views.VendorList.as_view(), name='VendorList'),
]
