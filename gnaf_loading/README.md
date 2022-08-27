# Loading GNAF into Postgres

Source GNAF data can be downloaded from https://data.gov.au/data/dataset/geocoded-national-address-file-g-naf

These scripts tested with Aug 2022 data.

Copies of the GNAF create tables/views/constraints supplied for convienience.  
Use the GNAF psv file loader script to load into a Postgres DB.  

Run these scripts, editing paths as you need:
1) 1_create_tables_ansi.sql  (copy from G-NAF/Extras/)
2) 2_GNAF_psv_file_load.sql
3) 3_add_fk_constraints.sql  (optional, can throw constraint errors; copy from G-NAF/Extras/)
4) 4_create_address_view.sql
5) 5_export_address_view.sql

Some easy tools for running Postgres on OSX are:
1) https://postgresapp.com/ for running a local Postgres DB (or just `brew install postgresql` instead.)
2) https://www.pgadmin.org/ for browsing your DB and executing SQL scripts.
