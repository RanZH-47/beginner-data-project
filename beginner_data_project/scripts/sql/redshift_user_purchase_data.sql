-- The Data Catalog consists of database and tables.
-- A table can be in only one database. 
-- Your database can contain tables from many different sources that AWS Glue supports.
CREATE EXTERNAL SCHEMA spectrum_schema
FROM
    DATA CATALOG DATABASE 'spectrumdb' IAM_ROLE 'arn:aws:iam::"$AWS_ID":role/"$IAM_ROLE_NAME"' CREATE DATABASE IF NOT EXISTS;

DROP EXTERNAL TABLE IF EXISTS spectrum_schema.user_purchase;

CREATE EXTERNAL TABLE spectrum_schema.user_purchase_staging (
    invoice_number varchar(10),
    stock_code varchar(20),
    detail varchar(1000),
    quantity int,
    invoice_date timestamp,
    unit_price Numeric(8, 3),
    customer_id int,
    country varchar(20)
) PARTITION BY range(insert_date DATE) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS textfile LOCATION 's3://$bucket_name/stage/user_purchase/' TABLE PROPERTIES ('skip.header.line.count' = '1');