-- 1. Rank car models based on the number of bids.
SELECT
  p.product_model AS model,
  COUNT(DISTINCT p.product_id) AS count_product,
  COUNT(b.bid_id) AS count_bid
FROM product p
LEFT JOIN bid b ON p.product_id = b.advertisement_id
GROUP BY p.product_model
ORDER BY count_bid DESC;

-- 2. Compare car prices based on the average price per city.
SELECT
  c.city_name AS nama_kota,
  p.product_brand AS merk,
  p.product_model AS model,
  p.product_year AS year,
  p.product_price AS price,
  AVG(p.product_price) OVER (PARTITION BY c.city_name) AS avg_car_city
FROM product p
JOIN user_data u ON p.user_id = u.user_id
JOIN city c ON u.city_id = c.city_id;

-- 3. From the offers of a car model, find the comparison of the date the user made the bid with the next bid and the bid price given.
SELECT
  p.product_model AS model,
  b.user_id AS user_id,
  b.bid_time AS first_bid_date,
  LEAD(b.bid_time) OVER (PARTITION BY b.user_id ORDER BY b.bid_time) AS next_bid_date,
  b.bid_amount AS first_bid_price,
  LEAD(b.bid_amount) OVER (PARTITION BY b.user_id ORDER BY b.bid_time) AS next_bid_price
FROM bid b
JOIN product p ON p.product_id = b.advertisement_id
WHERE p.product_model = 'march';

-- 4. Compare the percentage difference between the average car price based on the model and the average bid price offered by the customer in the last 6 months.
SELECT
  p.product_model AS model,
  AVG(p.product_price) AS avg_price,
  AVG(b.bid_amount) FILTER (WHERE b.bid_time > NOW() - INTERVAL '6 month') AS avg_bid_6month,
  AVG(p.product_price) - AVG(b.bid_amount) FILTER (WHERE b.bid_time > NOW() - INTERVAL '6 month') AS difference,
  ((AVG(p.product_price) - AVG(b.bid_amount) FILTER (WHERE b.bid_time > NOW() - INTERVAL '6 month')) * 100) / AVG(p.product_price) AS difference_percent
FROM product p
JOIN bid b ON p.product_id = b.advertisement_id
GROUP BY p.product_model;

-- 5. Create a window function for the average bid price of a brand and car model for the last 6 months. Let's use Nissan March as an example.
SELECT
  p.product_brand AS merk,
  p.product_model AS model,
  AVG(b.bid_amount) OVER (
    PARTITION BY p.product_brand, p.product_model
    ORDER BY b.bid_time DESC
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS avg_bid_amount
FROM
  product p
  INNER JOIN bid b ON p.product_id = b.product_id
WHERE
  p.product_brand = 'nissan' AND
  p.product_model = 'march';

SELECT
  p.product_brand AS merk,
  p.product_model AS model,
  AVG(b.bid_amount) OVER (
    PARTITION BY p.product_brand, p.product_model
    ORDER BY b.bid_time DESC
    RANGE BETWEEN INTERVAL '6 MONTHS' PRECEDING AND CURRENT ROW
  ) AS avg_bid_amount
FROM
  product p
INNER JOIN
  bid b ON p.product_id = b.product_id
WHERE
  b.bid_time >= CURRENT_DATE - INTERVAL '6 MONTHS'
  AND p.product_brand = 'nissan'
  AND p.product_model = 'notes';
