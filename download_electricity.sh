#!/bin/sh
cd /root/electricireland
docker run --rm --name firefox_selenium -v /root/electricireland/downloads:/home/seluser/Downloads -d -p 4444:4444 --shm-size=2g selenium/standalone-firefox
sleep 3
python3 download_electricity.py
docker stop firefox_selenium
cp -p "`ls -dtr1 "/root/electricireland/downloads"/* | tail -1`" "/root/electricireland/latest_electricity.csv"
curl "https://api.co2signal.com/v1/latest?countryCode=IE" -H "auth-token: yourAuthToken" > carbonfootprint.json
cp latest_electricity.csv /usr/share/hassio/homeassistant/latest_electricity.csv
cp carbonfootprint.json /usr/share/hassio/homeassistant/carbonfootprint.json