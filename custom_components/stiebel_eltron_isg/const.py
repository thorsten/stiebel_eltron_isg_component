"""Constants for stiebel_eltron_isg."""
from homeassistant.const import Platform

# Base component constants
DEFAULT_NAME = "Stiebel Eltron ISG"
NAME = DEFAULT_NAME
ATTR_MANUFACTURER = "Stiebel Eltron"
DOMAIN = "stiebel_eltron_isg"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.3.0"
ISSUE_URL = "https://github.com/pail23/stiebel_eltron_isg/issues"
DEFAULT_HOST_NAME = ""
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_PORT = 502

# Platforms
PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.NUMBER,
    Platform.SWITCH,
    Platform.SELECT,
]

ACTUAL_TEMPERATURE = "actual_temperature"
TARGET_TEMPERATURE = "target_temperature"
ACTUAL_TEMPERATURE_FEK = "actual_temperature_fek"
TARGET_TEMPERATURE_FEK = "target_temperature_fek"
ACTUAL_HUMIDITY = "actual_humidity"
DEWPOINT_TEMPERATURE = "dew_point_temperature"
OUTDOOR_TEMPERATURE = "outdoor_temperature"
ACTUAL_TEMPERATURE_HK1 = "actual_temperature_hk1"
TARGET_TEMPERATURE_HK1 = "target_temperature_hk1"
ACTUAL_TEMPERATURE_HK2 = "actual_temperature_hk2"
TARGET_TEMPERATURE_HK2 = "target_temperature_hk2"
ACTUAL_TEMPERATURE_BUFFER = "actual_temperature_buffer"
TARGET_TEMPERATURE_BUFFER = "target_temperature_buffer"
ACTUAL_TEMPERATURE_WATER = "actual_temperature_water"
TARGET_TEMPERATURE_WATER = "target_temperature_water"
SOURCE_TEMPERATURE = "source_temperature"
HEATER_PRESSURE = "heating_pressure"
VOLUME_STREAM = "volume_stream"
SG_READY_STATE = "sg_ready_state"
CONTROLLER_TYPE = "controller_type"
SG_READY_ACTIVE = "sg_ready_active"
SG_READY_INPUT_1 = "sg_ready_input_1"
SG_READY_INPUT_2 = "sg_ready_input_2"

OPERATION_MODE = "operation_mode"


PRODUCED_HEATING_TODAY = "produced_heating_today"
PRODUCED_HEATING_TOTAL = "produced_heating_total"
PRODUCED_WATER_HEATING_TODAY = "produced_water_heating_today"
PRODUCED_WATER_HEATING_TOTAL = "produced_water_heating_total"

CONSUMED_HEATING_TODAY = "consumed_heating_today"
CONSUMED_HEATING_TOTAL = "consumed_heating_total"
CONSUMED_WATER_HEATING_TODAY = "consumed_water_heating_today"
CONSUMED_WATER_HEATING_TOTAL = "consumed_water_heating_total"


IS_HEATING = "is_heating"
IS_HEATING_WATER = "is_heating_water"
IS_SUMMER_MODE = "is_summer_mode"
IS_COOLING = "is_cooling"

COMFORT_TEMPERATURE_TARGET = "comfort_temperature_target"
ECO_TEMPERATURE_TARGET = "eco_temperature_target"
HEATING_CURVE_RISE = "heating_curve_rise"
COMFORT_WATER_TEMPERATURE_TARGET = "comfort_water_temperature_target"
ECO_WATER_TEMPERATURE_TARGET = "eco_water_temperature_target"


FAN_LEVEL = "fan_level"
