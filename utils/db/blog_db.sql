create table if not exists blog
(
    id        serial
        constraint blog_pk
            primary key,
    title     text,
    link      text,
    date_post date
);

alter table blog
    owner to postgres;