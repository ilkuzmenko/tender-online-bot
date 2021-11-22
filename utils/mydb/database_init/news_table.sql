create table if not exists news
(
	id int auto_increment,
	title varchar(255) null,
	link varchar(255) null,
	date_post date null,
	constraint blog_pk
		primary key (id)
);

create unique index news_link_uindex
	on news (link);