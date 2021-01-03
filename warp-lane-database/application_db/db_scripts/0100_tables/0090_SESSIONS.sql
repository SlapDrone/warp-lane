-- Table: public.sessions

-- DROP TABLE public.sessions;

CREATE TABLE public.sessions
(
    "SESSIONID" integer NOT NULL,
    "USERID" integer NOT NULL,
    "EXPIRYTIME" date,
    "DATEMODIFIED" date,
    CONSTRAINT sessions_pk PRIMARY KEY ("SESSIONID")
)

TABLESPACE pg_default;

ALTER TABLE public.sessions
    OWNER to admin;