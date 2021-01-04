-- Table: public.unmodifiedtracks

-- DROP TABLE public.unmodifiedtracks;

CREATE TABLE public.unmodifiedtracks
(
    unmodifiedtrackid serial,
    uploadedbyuserid integer NOT NULL,
    tracklink text COLLATE pg_catalog."default",
    trackname text COLLATE pg_catalog."default",
    datemodified timestamp,
    datecreated timestamp default current_timestamp,
    CONSTRAINT unmodifiedtracks_pk PRIMARY KEY (unmodifiedtrackid),
    CONSTRAINT "UNMODIFIEDTRACKS_USERS_FK" FOREIGN KEY (uploadedbyuserid)
        REFERENCES public.users (userid) MATCH SIMPLE
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
    (uploadedbyuserid ASC NULLS LAST)
    TABLESPACE pg_default;