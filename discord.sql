CREATE TABLE IF NOT EXISTS user(id,name, UNIQUE(id));
CREATE TABLE IF NOT EXISTS message(id,user_id,content);
