# urban-living-nuernberg flat availibility monitor
Checks the website every n minutes/hours if an apartment is available to reserve

crontab runs every 30 minutes:
*/30 * * * * <path_to_virtualenv>/flatmonitor/bin/python <path_to_virtualenv>/flatmonitor/bot.py

You need:
python3.x
python3-virtualenv
pip:
  bs4
  time
  re
  html
  urllib
