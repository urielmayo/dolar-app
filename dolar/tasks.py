from dolar_app.celery import app
from celery.utils.log import get_task_logger
import requests
from dolar.models import Dolar

logger = get_task_logger(__name__)


@app.task
def update_dolar_vals():
    url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
    api = requests.get(url)
    dolares = {
        'Dolar Oficial',
        'Dolar Blue',
        'Dolar Bolsa',
        'Dolar Contado con Liqui',
        'Dolar turista',
    }
    if api.status_code == 200:
        dolar_vals = {
            dolar['casa']['nombre']: {
                'compra': dolar['casa']['compra'],
                'venta': dolar['casa']['venta'],
            }
            for dolar in api.json()
            if dolar['casa']['nombre'] in dolares
        }
    dolares = Dolar.objects.all()
    for dolar in dolares:
        logger.info(f"updating dolar: {dolar.name}")
        if dolar.name in dolar_vals.keys():
            try:
                venta = float(
                    dolar_vals[dolar.name]['venta'].replace(',', '.')
                )
            except ValueError:
                venta = 0
            try:
                compra = float(
                    dolar_vals[dolar.name]['compra'].replace(',', '.')
                )
            except ValueError:
                venta = 0

            dolar.buy_price = compra
            dolar.sell_price = venta
        dolar.save()
    return True
