create table if not exists users
(
	id int auto_increment,
	user_id bigint not null ,
	phone bigint null,
	first_name varchar(255) null,
	last_name varchar(255) null,
	news TINYINT default 0,
	dt datetime default CURRENT_TIMESTAMP null,
	constraint users_pk
		primary key (id)
);

create unique index users_user_id_uindex
	on users (user_id);