-- Table: public.devices

-- DROP TABLE public.devices;

CREATE TABLE public.devices
(
    deviceid serial,
    addedbyuserid integer NOT NULL,
    devicename text COLLATE pg_catalog."default",
    jsonconfigtemplate json,
    lastmodifiedby integer,
    datemodified timestamp,
    datecreated timestamp default current_timestamp,
    CONSTRAINT devices_pk PRIMARY KEY (deviceid),
    CONSTRAINT "DEVICES_USERS_FK" FOREIGN KEY (addedbyuserid)
        REFERENCES public.users (userid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.devices
    OWNER to admin;
-- Index: fki_DEVICES_USERS_FK

-- DROP INDEX public."fki_DEVICES_USERS_FK";

CREATE INDEX "fki_DEVICES_USERS_FK"
    ON public.devices USING btree
    (addedbyuserid ASC NULLS LAST)
    TABLESPACE pg_default;