# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command

1,17,33,49 9-17 1 4 * cd /home/ubuntu/SP25_DS5111_pvq8hv; . env/bin/activate; cd /home/ubuntu/SP25_DS5111_pvq8hv/scripts; make clean_yahoo; make yahoogain
ers.csv > /home/ubuntu/SP25_DS5111_pvq8hv/sample_data/logs/yahoo_$(date +\%Y-\%m-\%d_\%H-\%M).log 2>&1; python yahoo_timestamp.py

1,17,33,49 9-17 1 4 * cd /home/ubuntu/SP25_DS5111_pvq8hv; . env/bin/activate; cd /home/ubuntu/SP25_DS5111_pvq8hv/scripts; make clean_wsj; make wsjgainers.
csv > /home/ubuntu/SP25_DS5111_pvq8hv/sample_data/logs/wsj_$(date +\%Y-\%m-\%d_\%H-\%M).log 2>&1; python wsj_timestamp.py

1,17,33,49 9-17 1 4 * cd /home/ubuntu/SP25_DS5111_pvq8hv; . env/bin/activate; cd /home/ubuntu/SP25_DS5111_pvq8hv/scripts; make clean_sanalysis; make sanal
ysisgainers.csv > /home/ubuntu/SP25_DS5111_pvq8hv/sample_data/logs/sanalysis_$(date +\%Y-\%m-\%d_\%H-\%M).log 2>&1; python sanalysis_timestamp.py
