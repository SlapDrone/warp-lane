CREATE TABLE public.USERS
(
    "USERID" integer NOT NULL,
    "USERNAME" text COLLATE pg_catalog."default",
    "PASSWORD" text COLLATE pg_catalog."default",
    "EMAILADDRESS" text COLLATE pg_catalog."default",
    "DATEMODIFIED" date,
    CONSTRAINT USERS_PK PRIMARY KEY ("USERID")
);