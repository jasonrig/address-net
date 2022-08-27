head -10000 /Users/dylan/_data/gnaf/address_view_aug2022.csv > /Users/dylan/_data/gnaf/address_view_aug2022_top10K.csv
head -1000000 /Users/dylan/_data/gnaf/address_view_aug2022.csv > /Users/dylan/_data/gnaf/address_view_aug2022_top1M.csv
head -5000000 /Users/dylan/_data/gnaf/address_view_aug2022.csv > /Users/dylan/_data/gnaf/address_view_aug2022_top5M.csv

gzip /Users/dylan/_data/gnaf/address_view_aug2022_top10K.csv
gzip /Users/dylan/_data/gnaf/address_view_aug2022_top1M.csv
gzip /Users/dylan/_data/gnaf/address_view_aug2022_top5M.csv
gzip /Users/dylan/_data/gnaf/address_view_aug2022.csv
