from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
import json

from .models import Item
from .config import ITEM_FIELDS


def _success(data=None):
    response_dict = {'ok': True, 'errors': {}}
    if data is not None:
        response_dict['data'] = data
    return JsonResponse(response_dict)


def _error(errors, status=400):
    return JsonResponse({'ok': False, 'errors': errors}, status=status)


@csrf_exempt
@require_http_methods(['POST'])
def add_item(request):
    params = json.loads(request.body.decode())
    item_fields = {field: params.get(field, '') for field in ITEM_FIELDS}
    item = Item(**item_fields)
    item.save()

    return _success({'item': item.to_dict()})


@require_http_methods(['GET'])
def get_items(request):
    items = Item.objects.all()
    return _success({'items': [item.to_dict() for item in items]})
