## file for SI units and physical constants

## fundamental units - use 1.0 to make them floats
meter = 1.0;
sec =   1.0;
mol =   1.0;
amp =   1.0;  # Fix later, should use Coulomb
volt=   1.0;
kelvin= 1.0;
kg =    1.0;

## derived units
C =      sec*amp;
joule  = kg * meter**2 * sec**-2

kJ     = 10**3 * joule;
cm     = 10**-2 * meter;
mm     = 10**-3 * meter;
micron = 10**-6 * meter;
nm     = 10**-9 * meter;
liter  = 1000 * cm**3;
mC     = 10**-3;   # implied coulomb here

mA     = 10**-3 * amp;
mV     = 10**-3 * volt;

minute = 60.0 * sec;
hour   = 3600.0  * sec;

molar  = mol/liter;
mM     = 10**-3 * molar;


## Physical constants
R      = 8.3144598;               # in SI units, J mol-1 K-1
q      = 1.60217662*10**-19 * C   # Elementary charge
NA     = 6.02214076*10**23        # Avogadro number
F      = NA * q;                  # Faraday constant
hbar   = 1.0545718*10**-34 * meter**2 * kg * sec**-1;

## Other units
eV     = 1.602176634*1e-19 * joule
meV    = 1e-3 * eV
kB     = R/NA