-- 1. Finding cars made in 2015 and onwards:
SELECT
  product_id,
  product_brand AS merk,
  product_model AS model,
  product_year AS year,
  product_price AS price
FROM
  product
WHERE
  product_year >= 2015;

-- 2. Adding a new bid to a product:
-- Join the bid table with the advertisement table and the product table, view the tabble first
SELECT b.bid_id, b.bid_amount, b.bid_time, b.user_id, b.advertisement_id, a.product_id
FROM bid b
JOIN advertisement a ON b.advertisement_id = a.advertisement_id
JOIN product p ON a.product_id = p.product_id
ORDER BY bid_id ASC;

-- Insert a new bid data with a different bid_id, for example a new bid_id 51
INSERT INTO bid (bid_id, bid_amount, bid_time, user_id, advertisement_id)
VALUES (51, 185500000, '2022-03-04', 7, 3);

-- 3. Viewing all cars sold by a specific account, ordered by the newest:
SELECT
  p.product_id,
  p.product_brand AS merk,
  p.product_model AS model,
  p.product_year AS year,
  p.product_price AS price,
  a.post_date AS date_post
FROM
  product p
JOIN
  advertisement a ON a.product_id = p.product_id
JOIN
  user_data u ON u.user_id = p.user_id
WHERE
  u.user_name = 'Titin Wijaya'
ORDER BY
  a.post_date DESC;

-- 4. Searching for the cheapest used car based on a keyword:
SELECT
  product_id,
  product_brand AS merk,
  product_model AS model,
  product_year AS year,
  product_price AS price
FROM
  product
WHERE
  product_model LIKE '%mpv%'
ORDER BY
  product_price ASC
LIMIT 1;

-- 5. Finding the nearest used car based on a city id. For example, we will look for the nearest car in city_id = 1
SELECT
  product.product_id,
  product.product_brand AS merk,
  product.product_model AS model,
  product.product_year AS year,
  product.product_price AS price,
  SQRT(
    POWER(city.latitude - user_city.latitude, 2) +
    POWER(city.longitude - user_city.longitude, 2)
  ) AS distance
FROM
  product
JOIN
  user_data ON product.user_id = user_data.user_id
JOIN
  city AS user_city ON user_data.city_id = user_city.city_id
CROSS JOIN
  (
    SELECT
      latitude,
      longitude
    FROM
      city
    WHERE
      city_id = 1
  ) AS city
WHERE
  user_city.city_id <> 1
ORDER BY
  distance ASC
LIMIT 10;
