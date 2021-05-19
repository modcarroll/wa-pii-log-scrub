# Watson Assistant PII Log Scrubber

Rudimentary Python PII scrubbing for Watson Assistant logs using [scrubadub](https://pypi.org/project/scrubadub/)

This script will overwrite your existing logs files by replacing selected PII with `REDACTED`. Depending on the number of logs you have, this may take some time to run.

1.) Clone the repository

2.) Place your Watson Assistant log file(s) in the `data` folder. The name of the log file(s) will not matter.

3.) `pip3 install scrubadub`

4.) `chmod 755 run.sh`

5.) `./run.sh`

#### Warning: Always manually verify the redactions before transferring possible PII to any other individual or server.
