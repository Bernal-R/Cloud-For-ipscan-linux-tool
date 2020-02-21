create table Tags (
	timestam VARCHAR(50) NOT NULL,
	hostname VARCHAR(50) NOT NULL,
	tag_id SERIAL PRIMARY KEY
);

create table Categories (
	bots boolean NOT NULL,
	crypto_mining boolean NOT NULL,
	ip_scan boolean NOT NULL,
	ip_dynamic boolean NOT NULL,
	malware boolean NOT NULL,
	anonymization boolean NOT NULL,
	botnets_command_center boolean NOT NULL,
	spam boolean NOT NULL,
	id_categories SERIAL PRIMARY KEY
);

create table Analysis (
	ip VARCHAR (50) PRIMARY KEY,
	score INT NOT NULL,
	country VARCHAR(50) NOT NULL,
    tag_id SERIAL NOT NULL,
	id_categories SERIAL NOT NULL,
	FOREIGN KEY (tag_id) REFERENCES tags(tag_id),
	FOREIGN KEY (id_categories) REFERENCES categories(id_categories)
);
