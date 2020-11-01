from django.shortcuts import render
from .utilities import get_json_data, loop_through_dict


URL = 'http://data.fixer.io/api/latest?access_key=fe3a9b3f9ac173a3e51d8ea22951cf95'
ADDED_VALUE = 10.0002


def index(request):
    json_data = get_json_data(URL)

    context = None
    if json_data:
        rates =  json_data.get('rates')
        loop_through_dict(rates, ADDED_VALUE)

        context = {
            'date': json_data.get('date'),
            'base': json_data.get('base'),
            'added_val': ADDED_VALUE,
            'rates': rates
            }

    return render(request, 'viewer/index.html', context )