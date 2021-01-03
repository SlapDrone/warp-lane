-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
    "USERID" serial,
    "USERNAME" text COLLATE pg_catalog."default",
    "PASSWORD" text COLLATE pg_catalog."default",
    "EMAILADDRESS" text COLLATE pg_catalog."default",
    "DATEMODIFIED" date,
    CONSTRAINT users_pk PRIMARY KEY ("USERID")
)

TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to admin;
