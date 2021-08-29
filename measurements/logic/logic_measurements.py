from measurements.views import get_measurent
from ..models import Measurement

def get_all_measurements():
    measuremnts = Measurement.objects.all()
    return measuremnts

def get_measurement(identifier):
    return Measurement.objects.get(id=identifier)


def delete_measurement(identifier):
    return Measurement.objects.filter(id=identifier).delete()


def change_measurement(identifier,newObject):
    return Measurement.objects.filter(id=identifier).update(newObject)