# electric-ireland-hassio
A sort of good enough way to add electricity data from Electric Ireland's smart meters to Home Assistant.

![Lovelace Screenshot](https://raw.githubusercontent.com/brunostjohn/electric-ireland-hassio/main/lovelace_screenshot.png)

## How it works
It's a bunch of scripts that use Selenium to drive a Firefox docker container (to bypass the need for a Window Server) to download a CSV from Your Account Online -> View Account -> Details -> Download your smart meter data. It makes a bunch of assumptions that may not be true for your use case but could serve as a foundation to make something that actually works for you. It definitely works for me but YMMV. For any issues, open an issue on GitHub and I'll try to sort it but can't promise much.

## Installation
Warning: this requires *some* sysadmin experience to set up properly. I'm running this on a Home Assistant Supervised on Debian Bullseye setup so YMMV but the setup steps should stay rougly the same between systems.

### Things you will need
Python dependencies:
- Selenium
The rest should be covered by default Python packages.
OS dependencies:
- Cron
- Docker
- Python

### Actual install steps
1. Download this repo: `git clone https://github.com/brunostjohn/electric-ireland-hassio.git`
2. Create a folder named `electricireland` in your `/root/` directory. You can also change the `download_electricity.sh` script to use a directory that suits you better.
3. Copy the repo's contents there.
4. Copy `process_electricity.py` to your Home Assistant config directory.
5. If your Home Assistant config directory isn't `/usr/share/hassio/homeassistant`, please change it to the appropriate directory in the `download_electricity.sh` script.
6. Download the selenium/standalone-firefox docker container.
7. Get an API key from co2signal.com if you want to get a carbon footprint sensor.
8. Update the `download_electricity.py` script to contain the correct email and password for your Electric Ireland account.
9. Ensure that the download directory for the script has the appropriate permissions: `chown 1200:1201 /root/electricireland/downloads`.
10. Ensure that the scripts have appropriate permissions: `chmod +x *.sh && chmod +x *.py`.
11. Try running the script `./download_electricity.sh` and check that the CSV file downloaded makes sense `cat ./latest_electricity.csv`.
12. If it works correctly, add the script to your crontab using `crontab -e`. Try running it 3 times as the Electric Ireland site and script suck and sometimes don't work correctly. I run it at 5:30am, 6:00am, and 6:30 am. Check `crontab-sample.txt` for what you should add to your crontab for it to work like that. Make sure to use the correct directory.
13. Once you've done that, open up your Home Assistant config and add the `configuration-snippet.yaml` to it.
14. Update `process_electricity.py` to contain an appropriate rate for your electricity contract. It's at line 21. You can also modify the code to support the appropriate Day/Night rate. `last_line` contains values of your total usage in kWh for every 30 minutes of yesterday. If you have basic python knowledge, should be 10-15 minutes.
15. Restart Home Assistant.
16. Once that's done, you should have sensors for yesterday's electricity usage, carbon footprint, and how much money you paid.