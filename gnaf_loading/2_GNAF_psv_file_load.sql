--  
-- SQL script to Load GNAF data
-- Run me after creating tables, see:
-- https://data.gov.au/data/dataset/geocoded-national-address-file-g-naf
-- 

-- Drop to clear tables
-- select 'drop table if exists "' || tablename || '" cascade; -- ' || schemaname from pg_tables where schemaname = 'public';
-- drop table if exists "address_detail" cascade;
-- drop table if exists "address_alias" cascade;
-- drop table if exists "address_alias_type_aut" cascade;
-- drop table if exists "address_default_geocode" cascade;
-- drop table if exists "geocode_type_aut" cascade;
-- drop table if exists "address_site" cascade;
-- drop table if exists "flat_type_aut" cascade;
-- drop table if exists "geocoded_level_type_aut" cascade;
-- drop table if exists "level_type_aut" cascade;
-- drop table if exists "locality" cascade;
-- drop table if exists "street_locality" cascade;
-- drop table if exists "address_change_type_aut" cascade;
-- drop table if exists "address_feature" cascade;
-- drop table if exists "address_mesh_block_2016" cascade;
-- drop table if exists "mb_2016" cascade;
-- drop table if exists "mb_match_code_aut" cascade;
-- drop table if exists "address_mesh_block_2021" cascade;
-- drop table if exists "mb_2021" cascade;
-- drop table if exists "address_type_aut" cascade;
-- drop table if exists "address_site_geocode" cascade;
-- drop table if exists "geocode_reliability_aut" cascade;
-- drop table if exists "locality_class_aut" cascade;
-- drop table if exists "state" cascade;
-- drop table if exists "locality_alias_type_aut" cascade;
-- drop table if exists "locality_alias" cascade;
-- drop table if exists "locality_neighbour" cascade;
-- drop table if exists "locality_point" cascade;
-- drop table if exists "primary_secondary" cascade;
-- drop table if exists "ps_join_type_aut" cascade;
-- drop table if exists "street_class_aut" cascade;
-- drop table if exists "street_suffix_aut" cascade;
-- drop table if exists "street_type_aut" cascade;
-- drop table if exists "street_locality_alias_type_aut" cascade;
-- drop table if exists "street_locality_alias" cascade;
-- drop table if exists "street_locality_point" cascade;

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
	
COPY FLAT_TYPE_AUT FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Authority Code/Authority_Code_FLAT_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY GEOCODE_TYPE_AUT FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Authority Code/Authority_Code_GEOCODE_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY GEOCODED_LEVEL_TYPE_AUT FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Authority Code/Authority_Code_GEOCODED_LEVEL_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY LEVEL_TYPE_AUT FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Authority Code/Authority_Code_LEVEL_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_CLASS_AUT FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Authority Code/Authority_Code_STREET_CLASS_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_SUFFIX_AUT FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Authority Code/Authority_Code_STREET_SUFFIX_AUT_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_TYPE_AUT FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Authority Code/Authority_Code_STREET_TYPE_AUT_psv.psv' DELIMITER '|' CSV HEADER;


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
	
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/ACT_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NSW_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NT_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/OT_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/QLD_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/SA_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/TAS_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/VIC_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DEFAULT_GEOCODE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/WA_ADDRESS_DEFAULT_GEOCODE_psv.psv' DELIMITER '|' CSV HEADER;

COPY ADDRESS_DETAIL FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/ACT_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NSW_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NT_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/OT_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/QLD_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/SA_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/TAS_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/VIC_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;
COPY ADDRESS_DETAIL FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/WA_ADDRESS_DETAIL_psv.psv' DELIMITER '|' CSV HEADER;

COPY LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/ACT_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NSW_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NT_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/OT_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/QLD_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/SA_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/TAS_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/VIC_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/WA_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;

COPY STREET_LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/ACT_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NSW_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NT_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/OT_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/QLD_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/SA_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/TAS_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/VIC_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;
COPY STREET_LOCALITY FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/WA_STREET_LOCALITY_psv.psv' DELIMITER '|' CSV HEADER;

COPY STATE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/ACT_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NSW_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/NT_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/OT_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/QLD_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/SA_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/TAS_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/VIC_STATE_psv.psv' DELIMITER '|' CSV HEADER;
COPY STATE FROM '/Users/dylan/_data/gnaf/g-naf_aug22_allstates_gda2020_psv_108/G-NAF/G-NAF AUGUST 2022/Standard/WA_STATE_psv.psv' DELIMITER '|' CSV HEADER;
