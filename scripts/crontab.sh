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

1,31 9-16 * 4 2 cd /home/ubuntu/SP25_DS5111_pvq8hv/scripts && /home/ubuntu/SP25_DS5111_pvq8hv/env/bin/python -m make yahoogainers.csv >> /home/ubuntu/
SP25_DS5111_pvq8hv/sample_data/logs/yahoo.log 2>&1
1,31 9-16 * 4 2 cd /home/ubuntu/SP25_DS5111_pvq8hv/scripts && /home/ubuntu/SP25_DS5111_pvq8hv/env/bin/python -m make wsjgainers.csv >> /home/ubuntu/SP
25_DS5111_pvq8hv/sample_data/logs/wsj.log 2>&1
1,31 9-16 * 4 2 cd /home/ubuntu/SP25_DS5111_pvq8hv/scripts && /home/ubuntu/SP25_DS5111_pvq8hv/env/bin/python -m make sanalysisgainers.csv >> /home/ubu
ntu/SP25_DS5111_pvq8hv/sample_data/logs/sanalysis.log 2>&1
