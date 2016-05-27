"""
swat-s1 utils.py

sqlite and enip use name (string) and pid (int) has key and the state stores
values as strings.

sqlite uses float keyword and cpppo use REAL keyword.
"""

from minicps.utils import build_debug_logger

swat = build_debug_logger(
    name=__name__,
    bytes_per_file=10000,
    rotating_files=2,
    lformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    ldir='logs/',
    suffix='')

# physical process {{{1
# SPHINX_SWAT_TUTORIAL SET PROCESS
GRAVITATION = 9.81             # m.s^-2
TANK_DIAMETER = 1.38           # m
TIMEOUT = 10000                # s
PUMP_FLOWRATE_IN = 2.55        # m^3/h spec say btw 2.2 and 2.4
PUMP_FLOWRATE_OUT = 2.45       # m^3/h spec say btw 2.2 and 2.4

# periods in msec
# R/W = Read or Write
T_PLC_R = 100E-3
T_PLC_W = 100E-3

T_PP_R = 200E-3
T_PP_W = 200E-3
T_HMI_R = 100E-3

# ImageTk
DISPLAYED_SAMPLES = 14

# Control logic thresholds
LIT_101 = {  # raw water tank mm
    'LL': 250.0,
    'L': 500.0,
    'H': 800.0,
    'HH': 1200.0,
}

LIT_301 = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 800.0,
    'H': 1000.0,
    'HH': 1200.0,
}

TANK_HEIGHT = 1.600  # m

# m^3 / h
FIT_201 = 0.0
# SPHINX_SWAT_TUTORIAL END SET PROCESS


# topo {{{1
IP = {
    'plc1': '192.168.1.10',
    'plc2': '192.168.1.20',
    'plc3': '192.168.1.30',
    'plc4': '192.168.1.40',
    'plc5': '192.168.1.50',
    'plc6': '192.168.1.60',
    'attacker': '192.168.1.77',
}

MAC = {
    'plc1': '00:1D:9C:C7:B0:70',
    'plc2': '00:1D:9C:C8:BC:46',
    'plc3': '00:1D:9C:C8:BD:F2',
    'plc4': '00:1D:9C:C7:FA:2C',
    'plc5': '00:1D:9C:C8:BC:2F',
    'plc6': '00:1D:9C:C7:FA:2D',
    'attacker': 'AA:AA:AA:AA:AA:AA',
}


# others
PLC1_DATA = {
}
PLC2_DATA = {
}
PLC3_DATA = {
}

# protocol
PLC1_ADDR = IP['plc1']
# TODO
PLC1_TAGS = (
    ('SENSOR1', 1, 'INT'),
    ('SENSOR2', 1, 'REAL'),
    ('SENSOR3', 1, 'INT'),  # interlock with PLC2
    ('ACTUATOR1', 1, 'INT'),  # 0 means OFF and 1 means ON
    ('ACTUATOR2', 1, 'INT'))
PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC1_SERVER
}

PLC2_ADDR = IP['plc2']
# TODO
PLC2_TAGS = (
    ('SENSOR3', 2, 'INT'),)  # interlock with PLC1
PLC2_SERVER = {
    'address': PLC2_ADDR,
    'tags': PLC2_TAGS
}
PLC2_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC2_SERVER
}

PLC3_ADDR = IP['plc3']
# TODO
PLC3_TAGS = (
    ('SENSOR3', 3, 'INT'),)  # interlock with PLC1
PLC3_SERVER = {
    'address': PLC3_ADDR,
    'tags': PLC3_TAGS
}
PLC3_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC3_SERVER
}

# state {{{1
PATH = 'swat_s1_db.sqlite'
NAME = 'swat_s1'

STATE = {
    'name': NAME,
    'path': PATH
}

SCHEMA = """
CREATE TABLE swat_s1 (
    scope             TEXT NOT NULL,
    name              TEXT NOT NULL,
    datatype          TEXT NOT NULL,
    value             TEXT,
    pid               INTEGER NOT NULL,
    PRIMARY KEY (scope, name, pid)
);
"""

DATATYPES = [
    'INT',
    'DINT',
    'BOOL',
    'REAL',

    'FIT_UDT',
    'AIN_UDT',  # eg: LIT
    'MV_UDT',
    'PMP_UDT',
]
