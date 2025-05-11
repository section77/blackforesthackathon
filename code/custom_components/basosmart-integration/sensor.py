import logging
import datetime
from datetime import timedelta
import requests
import json

from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
from homeassistant.const import PERCENTAGE
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.helpers import entity_registry as er


_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=10)

API_URL = (
    "https://api.stromgedacht.de/v1/states?zip={zip}&from={from_time}&to={to_time}"
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Stromgedacht Sensor platform."""
    zip_code = config["zip"]
    stromgedacht_api = StromgedachtAPI(zip_code)

    sensors = [
        StromgedachtSensor("Current State", stromgedacht_api),
        StromgedachtSensor("Minutes Until State >= 2", stromgedacht_api, True),
        StromgedachtSensor("Minutes Until State Returns to 1 or 2", stromgedacht_api, False),
    ]

    async_add_entities(sensors, True)


class StromgedachtSensor(Entity):
    """Stromgedacht Sensor mit optionaler Batterieanzeige."""

    def __init__(self, name, stromgedacht_api, count_minutes=None) -> None:
        self._name = name
        self._state = None
        self._stromgedacht_api = stromgedacht_api
        self._count_minutes = count_minutes
        self._battery_sensor_name = "sensor.battery_level"
        self._battery_state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {
            "battery_level": self._battery_state
        }

    async def async_added_to_hass(self):
        """Log all known entities once the sensor is added."""
        
        # Log all entities to see available sensors
        # Problem: The Charge Sensor from the battery is not available
        _LOGGER.info("=== async_added_to_hass(): Dumping all entity IDs ===")
        for entity in self.hass.states.async_all():
            _LOGGER.info("Entity: %s | State: %s", entity.entity_id, entity.state)
        _LOGGER.info("=== End of entity dump ===")


    @Throttle(SCAN_INTERVAL)
    async def async_update(self):
        if self.hass is None:
            _LOGGER.error("self.hass is None – cannot access other entities")
            return

        # Get the battery sensor
        battery_state = self.hass.states.get(self._battery_sensor_name)
        if battery_state and battery_state.state not in ("unknown", "unavailable"):
            try:
                self._battery_state = float(battery_state.state)
            except ValueError:
                _LOGGER.warning("Invalid battery state: %s", battery_state.state)
                self._battery_state = None
        else:
            _LOGGER.warning("Battery sensor not found or unavailable")
            self._battery_state = None

        # get Stromgedacht-API-Data 
        await self.hass.async_add_executor_job(self._stromgedacht_api.update)

        # set sensor data
        if self._name == "Current State":
            self._state = self._stromgedacht_api.current_state
        elif self._count_minutes is not None:
            self._state = self._stromgedacht_api.count_minutes(self._count_minutes)


class StromgedachtAPI:
    def __init__(self, zip_code) -> None:
        self._zip = zip_code
        self._states = None
        self.current_state = None

    def update(self):
        now = datetime.datetime.now().isoformat()
        to = (datetime.datetime.now() + timedelta(days=1)).isoformat()
        try:
            url = API_URL.format(zip=self._zip, from_time=now, to_time=to)
            _LOGGER.debug("Requesting Stromgedacht API: %s", url)
            response = requests.get(url)
            data = json.loads(response.text)
            self._states = data["states"]
            self.current_state = self._states[0]["state"]
        except Exception as e:
            _LOGGER.error(f"Error fetching data from Stromgedacht API: {e}")
            self.current_state = None

    def count_minutes(self, until_state_ge_2):
        minutes = 0
        for state_info in self._states:
            from_time = datetime.datetime.fromisoformat(state_info["from"])
            to_time = datetime.datetime.fromisoformat(state_info["to"])
            state = state_info["state"]

            if until_state_ge_2:
                if state >= 2:
                    break
            else:
                if state < 3:
                    break

            minutes += int((to_time - from_time).total_seconds() / 60)

        return minutes


