-- Table: public.sessions

-- DROP TABLE public.sessions;

CREATE TABLE public.sessions
(
    sessionid UUID,
    userid integer NOT NULL,
    expirytime timestamp,
    datecreated timestamp default current_timestamp,
    CONSTRAINT sessions_pk PRIMARY KEY (sessionid)
)

TABLESPACE pg_default;

ALTER TABLE public.sessions
    OWNER to admin;
