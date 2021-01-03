-- Table: public.unmodifiedtracks

-- DROP TABLE public.unmodifiedtracks;

CREATE TABLE public.unmodifiedtracks
(
    "UNMODIFIEDTRACKID" serial,
    "UPLOADEDBYUSERID" integer NOT NULL,
    "TRACKLINK" text COLLATE pg_catalog."default",
    "TRACKNAME" text COLLATE pg_catalog."default",
    "DATEMODIFIED" timestamp,
    CONSTRAINT unmodifiedtracks_pk PRIMARY KEY ("UNMODIFIEDTRACKID"),
    CONSTRAINT "UNMODIFIEDTRACKS_USERS_FK" FOREIGN KEY ("UPLOADEDBYUSERID")
        REFERENCES public.users ("USERID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.unmodifiedtracks
    OWNER to admin;
-- Index: fki_UNMODIFIEDTRACKS_USERS_FK

-- DROP INDEX public."fki_UNMODIFIEDTRACKS_USERS_FK";

CREATE INDEX "fki_UNMODIFIEDTRACKS_USERS_FK"
    ON public.unmodifiedtracks USING btree
    ("UPLOADEDBYUSERID" ASC NULLS LAST)
    TABLESPACE pg_default;