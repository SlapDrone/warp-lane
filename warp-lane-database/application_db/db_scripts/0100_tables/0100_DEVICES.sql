create table public.DEVICES(
    "DEVICEID" integer NOT NULL,
    "USERID" integer NOT NULL,
    "DEVICENAME" text COLLATE pg_catalog."default",
    "JSONCONFIG" text COLLATE pg_catalog."default",
    "DATEMODIFIED" date,
    CONSTRAINT DEVICES_PK PRIMARY KEY ("DEVICEID")
);