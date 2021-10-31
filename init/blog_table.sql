create table if not exists blog
(
	id int auto_increment,
	title varchar(255) null,
	link varchar(255) null,
	date_post date null,
	constraint blog_pk
		primary key (id)
);