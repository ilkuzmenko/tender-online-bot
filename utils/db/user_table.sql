create table if not exists users
(
	id serial
		constraint users_pk
			primary key,
	user_id bigint,
	phone bigint,
	first_name text,
	last_name text,
	blog boolean,
	reg_date date
);

alter table users
    owner to postgres;

alter table users alter column blog set default false;

create unique index if not exists users_user_id_uindex
	on users (user_id);

