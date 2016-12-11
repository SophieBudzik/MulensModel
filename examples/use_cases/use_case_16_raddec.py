import MulensModel 
from astropy.coordinates import SkyCoord
from astropy import units as u
"""
Use cases for passing RA, DEC to MulensDAta, Model, and Event
"""

#Specifying coordinates to calculate HJD from JD
data_1 = MulensModel.MulensData(file_name='data_file_1.dat', date_fmt="jdprime",
                              coords='18:00:00 -30:00:00')
data_2 = MulensModel.MulensData(file_name='data_file_2.dat', date_fmt="jdprime",
                              ra='18:00:00', dec='-30:00:00')
coords = SkyCoord('18:00:00 -30:00:00', unit=(u.hourangle, u.deg))
data_3 = MulensModel.MulensData(file_name='data_file_2.dat', coords=coords, date_fmt="jdprime")


#Specifiying coordinates to calculate a model with parallax
model = MulensModel.Model()
t_0 = 5000.
u_0 = 0.1
t_E = 10.
model.parameters(t_0=t_0, u_0=u_0, t_E=t_E, pi_E=[0.1,-1.2],
                 coords='18:00:00 -30:00:00', observatory='Kepler')
#Should also be able to specify the coordinates in the same 3 ways as
#for the data case.

#Access Galactic and ecliptic coordinates:
print(model.galactic_l)
print(model.galactic_b)
print(model.ecliptic_lon)
print(model.ecliptic_lat)

#Sepcifying coordinates for an event
my_data = MulensModel.MulensData(file_name='test.data', date_fmt='HJD')
model_params = MulensModel.ModelParameters(
    t_0=7500., u_0=0.2, t_E=32., pi_E_N=0.1, pi_E_E=-0.2)
event = MulensModel.Event(datasets=[my_data], 
                          model=MulensModel.Model(parameters=model_params), 
                          coords='18:00:00 -30:00:00')

#Given these three different cases, it will be possible to specify
#conflicting sets of coordinates at different stages of model
#definition. Do we care?

