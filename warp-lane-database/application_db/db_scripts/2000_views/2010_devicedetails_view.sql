-- View: public.devicedetails_view

-- DROP VIEW public.devicedetails_view;

CREATE OR REPLACE VIEW public.devicedetails_view
 AS
 SELECT 
    devices.deviceid,
    users.username as deviceownerusername,
    devices.devicename,
    devices.jsonconfigtemplate
FROM devices
LEFT JOIN users 
ON devices.addedbyuserid = users.userid;

ALTER TABLE public.devicedetails_view
    OWNER TO admin;

