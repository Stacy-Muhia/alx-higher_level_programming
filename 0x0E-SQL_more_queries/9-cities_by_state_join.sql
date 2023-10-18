-- A script that  lists all cities contained in the database hbtn_0d_usa.
SELECT `C`.`id`, `C`.`name`, `S`.`name`
	FROM `cities` AS `C`
	INNER JOIN `states` AS `S`
		ON `C`.`state_id` = `S`.`id`
		ORDER BY `C`.`id` ASC;
