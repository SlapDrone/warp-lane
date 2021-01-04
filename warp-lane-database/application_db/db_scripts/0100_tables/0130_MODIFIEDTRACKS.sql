-- Table: public.modifiedtracks

-- DROP TABLE public.modifiedtracks;

CREATE TABLE public.modifiedtracks
(
    modifiedtrackid serial,
    unmodifiedtrackid integer NOT NULL,
    modifiedbyuserid integer NOT NULL,
    tracklink text COLLATE pg_catalog."default",
    datemodified timestamp,
    datecreated timestamp default current_timestamp,
    ingestedbymodel boolean,
    CONSTRAINT modifiedtracks_pk PRIMARY KEY (modifiedtrackid),
    CONSTRAINT "MODIFIEDTRACKS_UNMODIFIEDTRACKS_FK" FOREIGN KEY (unmodifiedtrackid)
        REFERENCES public.unmodifiedtracks (unmodifiedtrackid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "MODIFIEDTRACKS_USERS_FK" FOREIGN KEY (modifiedbyuserid)
        REFERENCES public.users (userid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.modifiedtracks
    OWNER to admin;
-- Index: fki_MODIFIEDTRACKS_UNMODIFIEDTRACKS_FK

-- DROP INDEX public."fki_MODIFIEDTRACKS_UNMODIFIEDTRACKS_FK";

CREATE INDEX "fki_MODIFIEDTRACKS_UNMODIFIEDTRACKS_FK"
    ON public.modifiedtracks USING btree
    (unmodifiedtrackid ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: fki_MODIFIEDTRACKS_USERS_FK

-- DROP INDEX public."fki_MODIFIEDTRACKS_USERS_FK";

CREATE INDEX "fki_MODIFIEDTRACKS_USERS_FK"
    ON public.modifiedtracks USING btree
    (modifiedbyuserid ASC NULLS LAST)
    TABLESPACE pg_default;