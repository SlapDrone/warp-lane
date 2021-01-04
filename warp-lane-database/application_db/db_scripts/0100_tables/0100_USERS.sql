-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
    userid serial,
    username text COLLATE pg_catalog."default" unique,
    password text COLLATE pg_catalog."default",
    emailaddress text COLLATE pg_catalog."default",
    datemodified timestamp,
    datecreated timestamp default current_timestamp,
    CONSTRAINT users_pk PRIMARY KEY (userid)
)

TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to admin;
