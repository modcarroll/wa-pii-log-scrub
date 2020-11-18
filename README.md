# Watson Assistant PII Log Scrubber

Rudimentary Python PII scrubbing for Watson Assistant logs using (scrubadub)[https://pypi.org/project/scrubadub/]

1.) Clone the repository

2.) Replace `morgantownlogs.json` with your Watson Assistant log file in the `data` folder. If you change the name of the file, you will need to update line 4 in `main.py` with your new filename.

3.) `pip3 install scrubadub`

4.) `python3 main.py`
