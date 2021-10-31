create table if not exists users
(
	id int auto_increment,
	user_id int null,
	phone int null,
	first_name varchar(255) null,
	last_name varchar(255) null,
	blog BIT null,
	dt datetime default CURRENT_TIMESTAMP null,
	constraint users_pk
		primary key (id)
);