BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `healthy_day` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`file_id`	TEXT NOT NULL,
	`type`	TEXT NOT NULL
);
INSERT INTO `healthy_day` VALUES (1,'CgADAgADOQADIOtJST9Yy5-yQNSkAg','spine');
INSERT INTO `healthy_day` VALUES (2,'CgADAgADOwADIOtJSbpzjNcvDAO_Ag','legs');
INSERT INTO `healthy_day` VALUES (3,'CgADAgADOAADIOtJSWQOzKjzQeCuAg','spine');
INSERT INTO `healthy_day` VALUES (4,'CgADAgADPQADIOtJScwbg0BiIBz7Ag','abs');
COMMIT;