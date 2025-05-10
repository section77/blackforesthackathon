# blackforesthackathon
Repo for Code and Docs around the #blackforesthackathon 2025

documentation
- [Presentation](https://new.express.adobe.com/publishedV2/urn:aaid:sc:EU:c7f514e3-6e40-4c48-baa8-d4dd70234a42?promoid=Y69SGM5H&mv=other)
- [General](https://balkon.solar/dateien)
- HomeAssistant specific
  - how to install integrations
    - integration "Forecast.Solar"
        - log into HomeAssistant
        - Settings
        - Devices & services
        - Add integration
        - Search "Forecast.Solar"
    - [integration "Python Scripts"](https://www.home-assistant.io/integrations/python_script)
        - edit your configuration.yaml
        - add "python_script:"
        - create the folder <config>/python_scripts
        - Create a file <config>/python_scripts/hello_world.py in the folder and give it this content:
            ```Python
            # `data` is available as builtin and is a dictionary with the input data.
            name = data.get("name", "world")
            # `logger` and `time` are available as builtin without the need of explicit import.
            logger.info("Hello {} at {}".format(name, time.time()))
            ```
        - Start Home Assistant to reload the script configuration.
        - Call your new python_script.hello_world action (with parameters) from the Actions, using the YAML mode.
            ```YAML
            action: python_script.hello_world
            data:
                name: "Input-Text"
            ```
  - [how to generate a long lived access token](https://community.home-assistant.io/t/how-to-get-long-lived-access-token/162159)
    - log into HomeAssistant
    - click on your profile icon on the bottom left
    - click on the tab "Security"
    - section: "Long-lived access tokens"
    - create token
  - [how to integrate python scripts into HomeAssistant](https://www.home-assistant.io/integrations/python_script/)
- Forecast.Solar
  - how to create an 
- battery charing algorithm
    - optimized buffer use (to be included in the control):
        The charging and discharging process should be carried out as follows: At midnight, the battery storage system should be half charged so that it can serve the load until the start of the day. After sunrise, solar production quickly exceeds the load and the storage system, which is empty at this point, is gradually charged. If the daily yield corresponds to the annual average, the battery storage is filled to its capacity limit by the surplus electricity at sunset. On very high-yield days, the additional surplus electricity must be curtailed or utilised elsewhere once the capacity limit is exceeded. After darkness falls, the load is covered by the discharging current. At midnight, the battery is exactly half charged again and the cycle can begin anew. On low-yield days, the battery is only charged to a fraction of its capacity. The daily balance is negative and in this case must be compensated for by residual power plants or load reductions.

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

MVP
- HomeAssistant (HassOS)
- RaspberryPi

future improvements
- create a more generic solution, that is independent of HomeAssistant
- use APIs that provide a CO2 index and enery flow like [Grünstromindex](https://gruenstromindex.de/assets/js/)(prfered) or [Energy Charts](https://energy-charts.info/api.html?l=de&c=DE)
- Add more sophisticated prediction model e.g. AC charging, forcast with nonlinear-optimization algorithem and intraday optimization.  

Hurdles
- access to the ecoflow api
  - requires a developer account; activation takes a few days
  - registration is tricky (codes valid for 1 minute only, mail takes around 1 minute)
