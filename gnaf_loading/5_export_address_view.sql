-- Export address_view to csv
COPY (SELECT * FROM address_view) TO '/Users/dylan/_data/gnaf/address_view_aug2022.csv' WITH (FORMAT CSV, HEADER);