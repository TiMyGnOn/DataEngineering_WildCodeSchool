SET @ID_CLIENT_MAX_LOC = (SELECT customer_id FROM (
            SELECT customer_id, COUNT(*) AS num FROM rental GROUP BY customer_id ORDER BY num DESC LIMIT 1
        ) AS T
);

SELECT c.last_name, c.first_name,  a.address, count(r.customer_id) as nb_locations, a.postal_code, a.city,a.latitude,a.longitude

FROM customer c
INNER JOIN address a
on c.address_id = a.address_id
INNER JOIN rental r
on c.customer_id = r.customer_id

WHERE c.customer_id =  @ID_CLIENT_MAX_LOC;