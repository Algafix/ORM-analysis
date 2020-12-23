# ORM-analysis
Project to extract and analyse data after ORM executions.


## Python data extraction

This part will generate a csv file containing the domain id, the domain name, the number of cookies not interacting
with the website, the number of cookies trying to accept cookies and if we were successful on clicking the button.

| domain_ID | domain_name | cookies_default | cookies_accepted | clicked |
|-----------|-------------|-----------------|------------------|---------|
|           |             |                 |                  |         |
|           |             |                 |                  |         |


### Configure your own database

To configure your own databases you need to modify the file [db_manager](db_manager.py) the function get_dbs().
In the case that you only have one database with more than one model, change the "db" parameter to point to both models.

### Requirements

Only mysqlclient package is required, install with:
```bash
pip install -r requirements.txt
```
### Execution

To generate the csv file execute the script `main.py [-limit <limit>]`.

If no `-limit` parameter is specified, the script will analyse all the domains included in the *domain* table.


## R data treatment and plotting

This part of the project will read the previously generated csv file and generate meaningful statistics using R language.

### Executing

The R project is under [R_analysis/](R_analysis) folder, and the script [plots_generator.R](R_analysis/plots_generator.R)
is the one that needs to be executed in order to analyse the data and generate the charts.

### Charts generated

Currently, 3 charts are generated:

- Pie chart with the percentage of pages where cookies were accepted.
- Pie chart with the percentage of pages with the same number cookies accepting and not interacting.
- Bar plot with the overheating of cookies accepting versus not interacting.