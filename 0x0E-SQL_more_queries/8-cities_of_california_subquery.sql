-- Create list of al cities of Carlifornia that can be found in the hbtn_0d_usa database
-- Results are sorted in ascending order using cities_id
SELECT `id` `name`
       FROM `cities`
WHERE `state_id` IN
      (SELECT `id`
      	 FROM `states`
	 WHERE `name` = "California")

ORDER BY `id`;
