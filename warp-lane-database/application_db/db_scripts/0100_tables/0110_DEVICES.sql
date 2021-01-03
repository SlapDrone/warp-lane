-- Table: public.devices

-- DROP TABLE public.devices;

CREATE TABLE public.devices
(
    "DEVICEID" serial,
    "ADDEDBYUSERID" integer NOT NULL,
    "DEVICENAME" text COLLATE pg_catalog."default",
    "JSONCONFIGTEMPLATE" json,
    "DATEMODIFIED" timestamp,
    CONSTRAINT devices_pk PRIMARY KEY ("DEVICEID"),
    CONSTRAINT "DEVICES_USERS_FK" FOREIGN KEY ("ADDEDBYUSERID")
        REFERENCES public.users ("USERID") MATCH SIMPLE
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
    ("ADDEDBYUSERID" ASC NULLS LAST)
    TABLESPACE pg_default;