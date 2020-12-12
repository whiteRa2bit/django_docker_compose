import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Item
from .config import ITEM_FIELDS


def _success(data=None):
    response_dict = {'ok': True, 'errors': {}}
    if data is not None:
        response_dict['data'] = data
    return JsonResponse(response_dict)


def _error(errors, status=400):
    return JsonResponse({'ok': False, 'errors': errors}, status=status)


def _validate_fields(params, required_fields=ITEM_FIELDS, require_all=True):
    has_all_fields = all([field in params for field in required_fields])
    has_no_other_fields = all([field in required_fields for field in params])
    return has_no_other_fields and (not require_all or has_all_fields)


@require_http_methods(['GET'])
def get_items(request):
    items = Item.objects.all()
    return _success([item.to_dict() for item in items])


@require_http_methods(['GET'])
def get_item(request, id):
    try:
        item = Item.objects.get(pk=id)
        response = _success(item.to_dict())
    except Item.DoesNotExist:
        response = _error("No item with such id: {}".format(id), 404)
    return response


@csrf_exempt
@require_http_methods(['POST'])
def add_item(request):
    params = json.loads(request.body.decode())
    is_valid = _validate_fields(params)
    if is_valid:
        item_fields = {field: params.get(field) for field in ITEM_FIELDS}
        item = Item(**item_fields)
        item.save()
        response = _success(item.to_dict())
    else:
        response = _error("Invalid item format, provide an item with the following fields: {}".format(ITEM_FIELDS))
    return response


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_item(request, id):
    try:
        item = Item.objects.get(pk=id)
        item.delete()
        response = _success()
    except Item.DoesNotExist:
        response = _error("No item with such id: {}".format(id), 404)
    return response


@csrf_exempt
@require_http_methods(['PATCH'])
def update_item(request, id):
    try:
        item = Item.objects.get(pk=id)
        params = json.loads(request.body.decode())
        is_valid = _validate_fields(params, require_all=False)
        if is_valid:
            for field in params:
                setattr(item, field, params[field])
            item.save(update_fields=params.keys())
            response = _success(item.to_dict())
        else:
            response = response = _error("Invalid item format, provide an item with the following fields: {}".format(ITEM_FIELDS))
    except Item.DoesNotExist:
        response = _error("No item with such id: {}".format(id), 404)
    return response

