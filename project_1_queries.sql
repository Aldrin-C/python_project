
-- Users --
SELECT * FROM users;

-- Avatars --
SELECT * FROM avatars;

INSERT INTO avatars
	(name, attack, health, str, vit, defense, type, user_id)
VALUES
	('Ben', 45, 100, 25, 20, 30, 'samurai', 1);
    
    
-- JOIN --
SELECT * FROM avatars
LEFT JOIN users
ON avatars.user_id = users.id;
