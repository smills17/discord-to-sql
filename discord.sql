CREATE TABLE IF NOT EXISTS user(id,name, UNIQUE(id));
CREATE TABLE IF NOT EXISTS message(id,user_id,content);
CREATE TABLE IF NOT EXISTS react(message_id,emoji_name,quantity, UNIQUE(message_id, emoji_name));
