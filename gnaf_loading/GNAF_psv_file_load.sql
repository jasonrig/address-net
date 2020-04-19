-- Load Authority psv files into Postgres:
select count(*) from FLAT_TYPE_AUT
	union all
	select count(*) from GEOCODE_TYPE_AUT
	union all
	select count(*) from GEOCODED_LEVEL_TYPE_AUT
	union all
	select count(*) from LEVEL_TYPE_AUT
	union all
	select count(*) from STREET_CLASS_AUT
	union all
	select count(*) from STREET_SUFFIX_AUT
	union all
	select count(*) from STREET_TYPE_AUT;
	
COPY FLAT_TYPE_AUT FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Authority Code/Authority_Code_FLAT_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY GEOCODE_TYPE_AUT FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Authority Code/Authority_Code_GEOCODE_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY GEOCODED_LEVEL_TYPE_AUT FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Authority Code/Authority_Code_GEOCODED_LEVEL_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY LEVEL_TYPE_AUT FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Authority Code/Authority_Code_LEVEL_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_CLASS_AUT FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Authority Code/Authority_Code_STREET_CLASS_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_SUFFIX_AUT FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Authority Code/Authority_Code_STREET_SUFFIX_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_TYPE_AUT FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Authority Code/Authority_Code_STREET_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;


-- Standard psv files into Postgres:
select count(*) from ADDRESS_DEFAULT_GEOCODE
	union all
	select count(*) from ADDRESS_DETAIL
	union all
	select count(*) from LOCALITY
	union all
	select count(*) from STATE
	union all
	select count(*) from STREET_LOCALITY;
	
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/ACT_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NSW_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NT_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/OT_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/QLD_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/SA_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/TAS_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/VIC_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/WA_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;

COPY ADDRESS_DETAIL FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/ACT_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NSW_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NT_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/OT_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/QLD_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/SA_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/TAS_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/VIC_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/WA_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;

COPY LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/ACT_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NSW_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NT_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/OT_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/QLD_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/SA_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/TAS_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/VIC_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/WA_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;

COPY STREET_LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/ACT_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NSW_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NT_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/OT_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/QLD_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/SA_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/TAS_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/VIC_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/WA_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;

COPY STATE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/ACT_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NSW_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/NT_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/OT_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/QLD_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/SA_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/TAS_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/VIC_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/Datasets/data.gov.au/gnaf_202002/feb20_gnaf_pipeseparatedvalue/G-NAF/G-NAF FEBRUARY 2020/Standard/WA_STATE_psv.psv' DELIMITER '|' CSV HEADER;

-- Export address_view to csv
COPY (SELECT * FROM address_view) TO '/Users/dylan/Datasets/data.gov.au/gnaf_202002/address_view.csv' WITH (FORMAT CSV, HEADER);
