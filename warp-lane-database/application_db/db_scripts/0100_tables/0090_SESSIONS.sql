-- Table: public.sessions

-- DROP TABLE public.sessions;

CREATE TABLE public.sessions
(
    "SESSIONID" serial,
    "USERID" integer NOT NULL,
    "EXPIRYTIME" date,
    "DATEMODIFIED" timestamp,
    CONSTRAINT sessions_pk PRIMARY KEY ("SESSIONID")
)

TABLESPACE pg_default;

ALTER TABLE public.sessions
    OWNER to admin;
