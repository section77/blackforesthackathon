# blackforesthackathon
Repo for Code and Docs around the #blackforesthackathon 2025

documentation
- [general](https://balkon.solar/dateien)
- HomeAssistant specific
  - how to install integration Forecast.Solar
    - log into home assistant
    - Settings
    - Devices & services
    - Add integration
    - Search "Forecast.Solar"
  - [how to generate a long lived access token](https://community.home-assistant.io/t/how-to-get-long-lived-access-token/162159)
    - log into home assistant
    - click on your profile icon on the bottom left
    - click on the tab "Security"
    - section: "Long-lived access tokens"
    - create token

tools
- [HomeAssistant](https://www.home-assistant.io/)
  - [documentation for download](https://www.home-assistant.io/installation/raspberrypi#downloading-the-home-assistant-image)
- [StromGedacht API endpoint for Freiburg](https://api.stromgedacht.de/v1/now?zip=79110)
  - [integration for StromGedacht into HomeAssistant](https://community.home-assistant.io/t/stromgedacht-api-integration/568465)
- [PV-Leistungsprognose](https://www.photovoltaikforum.com/wissen/entry/39-kostenfreie-photovoltaik-leistungsprognose-f%C3%BCr-10-tageszeitfenster-mit-kostenfre/)
- [Solar energy prediction](https://openweathermap.org/api/solar-energy-prediction)
- [Meteoblue API](https://content.meteoblue.com/de/unternehmensloesungen/wetter-apis)

hardware for prosumers
- Rasperry Pi
- Radio-controlled sockets
- [Optical Readout Head for Smartmeter](https://www.ebay.de/sch/i.html?_nkw=hichi&_odkw=hitchi)


optimized buffer use (to be included in the control):
The charging and discharging process should be carried out as follows: At midnight, the battery storage system should be half charged so that it can serve the load until the start of the day. After sunrise, solar production quickly exceeds the load and the storage system, which is empty at this point, is gradually charged. If the daily yield corresponds to the annual average, the battery storage is filled to its capacity limit by the surplus electricity at sunset. On very high-yield days, the additional surplus electricity must be curtailed or utilised elsewhere once the capacity limit is exceeded. After darkness falls, the load is covered by the discharging current. At midnight, the battery is exactly half charged again and the cycle can begin anew. On low-yield days, the battery is only charged to a fraction of its capacity. The daily balance is negative and in this case must be compensated for by residual power plants or load reductions.
