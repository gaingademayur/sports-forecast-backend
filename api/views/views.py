from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from rest_framework.decorators import api_view
from django.db.models import F

from django.core.serializers import serialize
# from rest_framework.response import Response
from sportsForecastBackend.models import WarehouseModel
from sportsForecastBackend.models import Sales
from sportsForecastBackend.serializers import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import logging

logger = logging.getLogger(__name__)

class Warehouse:
    @csrf_exempt
    def getAllWarehouseData(request):
        queryset = WarehouseModel.objects.all()
        data_list=[]
        print(queryset)
        for item in queryset:
            field_dict = {
                'product_name': item.product_name,
                'available_qty': item.available_qty
            }
            data_list.append(field_dict)

        return JsonResponse(data_list, safe=False)

    @api_view(['POST'])
    def addNewProduct(request):
        if(request.method == 'POST'):
            try:
                product_name = request.data.get("name")
                quantity = request.data.get("quantity")
                res = WarehouseModel(product_name= product_name, available_qty= quantity)
                res.save()
                return JsonResponse({'status_code': 201, 'message': 'data inserted successfully'})
            except Exception as e:
                return JsonResponse({'error': str(e)})

    def getYearlySalesReport(request, id):
        try:
            res = Sales.objects.filter(sale_date__year = id) \
                                .values('product__product_name') \
                                .annotate(overall_sale=Sum('quantity_sold')) \
                                .order_by('product__product_name')
            salesResult = []
            print(res)
            for sale in res:
                field_dict = {
                    "product_name": sale.get("product__product_name"),
                    "overall_sale": sale.get("overall_sale")
                }
                salesResult.append(field_dict)
            return JsonResponse({"result": salesResult})
        except Exception as e:
            return JsonResponse({"error": ""})

    @api_view(['POST'])
    def updateInventory(request):
        try:
            product_name = request.data.get("name")
            quantity = request.data.get("quantity")
            updated_count = WarehouseModel.objects.filter(product_name=product_name).update(available_qty=F('available_qty') + quantity)


            return JsonResponse({"res": updated_count})
        except Exception as e:
            return JsonResponse({"res": str(e)})
