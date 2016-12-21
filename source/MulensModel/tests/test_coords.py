import sys
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u

from MulensModel.model import Model
from MulensModel.mulensdata import MulensData
from MulensModel.event import Event

for path in sys.path:
    if path.find("MulensModel/source") > 0:
        MODULE_PATH = "/".join(path.split("/source")[:-1])
SAMPLE_FILE_01 = MODULE_PATH + "/data/phot_ob08092_O4.dat"

def test_model_coords():
    coords = SkyCoord('18:00:00 -30:00:00', unit=(u.hourangle, u.deg))
    model_1 = Model(coords='18:00:00 -30:00:00')
    assert isinstance(model_1.coords, SkyCoord)
    assert model_1.coords.ra == coords.ra
    assert model_1.coords.dec == coords.dec
    assert  model_1.dec.deg == -30.00

    ra_2 = '17:00:00'
    dec_2 = '40:03:01'
    coords_2 = SkyCoord(
        '{0} {1}'.format(ra_2, dec_2), unit=(u.hourangle, u.deg))
    model_2 = Model()
    model_2.ra = ra_2
    model_2.dec = dec_2
    assert model_2.coords.ra == coords_2.ra
    assert model_2.coords.dec == coords_2.dec
    assert model_2.coords.to_string('hmsdms') == '17h00m00s +40d03m01s'

    model_3 = Model()
    model_3.coords = '17:00:00 -27:32:14'
    assert model_3.coords.to_string('hmsdms') == '17h00m00s -27d32m14s'

def test_data_coords():
    coords = SkyCoord('18:00:00 -30:00:00', unit=(u.hourangle, u.deg))
    data_1 = MulensData(
        file_name=SAMPLE_FILE_01, date_fmt='jdprime',
        coords='18:00:00 -30:00:00')
    assert isinstance(data_1.coords, SkyCoord)
    assert data_1.coords.ra == coords.ra
    assert data_1.coords.dec == coords.dec
    assert data_1.dec.deg == -30.00

    ra_2 = '17:00:00'
    dec_2 = '40:03:01'
    coords_2 = SkyCoord(
        '{0} {1}'.format(ra_2, dec_2), unit=(u.hourangle, u.deg))
    data_2 = MulensData(file_name=SAMPLE_FILE_01, date_fmt='jdprime')
    data_2.ra = ra_2
    data_2.dec = dec_2
    assert data_2.coords.ra == coords_2.ra
    assert data_2.coords.dec == coords_2.dec
    assert data_2.coords.to_string('hmsdms') == '17h00m00s +40d03m01s'
    assert data_2._time._target.to_string('hmsdms') == '17h00m00s +40d03m01s'

    data_3 = MulensData(file_name=SAMPLE_FILE_01, date_fmt='jdprime')
    data_3.coords = '17:00:00 -27:32:14'
    assert data_3.coords.to_string('hmsdms') == '17h00m00s -27d32m14s'

"""
Function not yet implemented
def test_event_coords():
    coord_str_data = '00h00m15s -75d30m15s'
    coord_str_event = '15h30m00s 45d00m00s'
    data = MulensData(
        file_name=SAMPLE_FILE_01, date_fmt='jdprime', 
        coords='00:00:15 -75:30:15')

    model = Model()
    event = Event(data=data, model=model, coords='15:30:00 45:00:00')
    assert event.coords.to_string('hmsdms') == coord_str_event
    assert event.model.coords.to_string('hmsdms') == coord_str_event
    assert event.data.coords.to_string('hmsdms') == coord_str_event

    event_2 = Event(coords='15:30:00 45:00:00')
    event_2.datasets = [data]
    assert event_2.coords.to_string('hmsdms') == coord_str_data
    assert event_2.data.coords.to_string('hmsdms') == coord_str_data
"""
