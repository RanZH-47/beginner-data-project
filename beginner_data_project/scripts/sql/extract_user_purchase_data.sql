COPY (
    SELECT
        invoice_number,
        stock_code,
        detail,
        quantity,
        invoice_date,
        unit_price,
        customer_id,
        country
    FROM
        retail.user_purchase
) TO '{{ params.user_purchase }}' WITH (FORMAT CSV, HEADER);