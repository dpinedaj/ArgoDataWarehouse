CREATE SCHEMA raw;
CREATE SCHEMA processed;

-- TODO: PARTITION BY
CREATE TABLE IF NOT EXISTS raw.fire_incidents(
    "Incident Number" VARCHAR,
    "Exposure Number" VARCHAR,
    "ID" VARCHAR,
    "Address" VARCHAR,
    "Incident Date" VARCHAR,
    "Call Number" VARCHAR,
    "Alarm DtTm" VARCHAR,
    "Arrival DtTm" VARCHAR,
    "Close DtTm" VARCHAR,
    "City" VARCHAR,
    "zipcode" VARCHAR,
    "Battalion" VARCHAR,
    "Station Area" VARCHAR,
    "Box" VARCHAR,
    "Suppression Units" VARCHAR,
    "Suppression Personnel" VARCHAR,
    "EMS Units" VARCHAR,
    "EMS Personnel" VARCHAR,
    "Other Units" VARCHAR,
    "Other Personnel" VARCHAR,
    "First Unit On Scene" VARCHAR,
    "Estimated Property Loss" VARCHAR,
    "Estimated Contents Loss" VARCHAR,
    "Fire Fatalities" VARCHAR,
    "Fire Injuries" VARCHAR,
    "Civilian Fatalities" VARCHAR,
    "Civilian Injuries" VARCHAR,
    "Number of Alarms" VARCHAR,
    "Primary Situation" VARCHAR,
    "Mutual Aid" VARCHAR,
    "Action Taken Primary" VARCHAR,
    "Action Taken Secondary" VARCHAR,
    "Action Taken Other" VARCHAR,
    "Detector Alerted Occupants" VARCHAR,
    "Property Use" VARCHAR,
    "Area of Fire Origin" VARCHAR,
    "Ignition Cause" VARCHAR,
    "Ignition Factor Primary" VARCHAR,
    "Ignition Factor Secondary" VARCHAR,
    "Heat Source" VARCHAR,
    "Item First Ignited" VARCHAR,
    "Human Factors Associated with Ignition" VARCHAR,
    "Structure Type" VARCHAR,
    "Structure Status" VARCHAR,
    "Floor of Fire Origin" VARCHAR,
    "Fire Spread" VARCHAR,
    "No Flame Spead" VARCHAR,
    "Number of floors with minimum damage" VARCHAR,
    "Number of floors with significant damage" VARCHAR,
    "Number of floors with heavy damage" VARCHAR,
    "Number of floors with extreme damage" VARCHAR,
    "Detectors Present" VARCHAR,
    "Detector Type" VARCHAR,
    "Detector Operation" VARCHAR,
    "Detector Effectiveness" VARCHAR,
    "Detector Failure Reason" VARCHAR,
    "Automatic Extinguishing System Present" VARCHAR,
    "Automatic Extinguishing Sytem Type" VARCHAR,
    "Automatic Extinguishing Sytem Perfomance" VARCHAR,
    "Automatic Extinguishing Sytem Failure Reason" VARCHAR,
    "Number of Sprinkler Heads Operating" VARCHAR,
    "Supervisor District" VARCHAR,
    "neighborhood_district" VARCHAR,
    "point" VARCHAR,
    "CurrentDate" VARCHAR
);


-- TODO: PARTITION BY
CREATE TABLE IF NOT EXISTS processed.fire_incidents(
    "Incident Number" NUMERIC,
    "Exposure Number" NUMERIC,
    "ID" VARCHAR,
    "Address" VARCHAR,
    "Incident Date" VARCHAR,
    "Call Number" VARCHAR,
    "Alarm DtTm" VARCHAR,
    "Arrival DtTm" VARCHAR,
    "Close DtTm" VARCHAR,
    "City" VARCHAR,
    "zipcode" VARCHAR,
    "Battalion" VARCHAR,
    "Station Area" VARCHAR,
    "Box" VARCHAR,
    "Suppression Units" NUMERIC,
    "Suppression Personnel" NUMERIC,
    "EMS Units" NUMERIC,
    "EMS Personnel" NUMERIC,
    "Other Units" NUMERIC,
    "Other Personnel" NUMERIC,
    "First Unit On Scene" VARCHAR,
    "Estimated Property Loss" NUMERIC,
    "Estimated Contents Loss" NUMERIC,
    "Fire Fatalities" NUMERIC,
    "Fire Injuries" NUMERIC,
    "Civilian Fatalities" NUMERIC,
    "Civilian Injuries" NUMERIC,
    "Number of Alarms" NUMERIC,
    "Primary Situation" VARCHAR,
    "Mutual Aid" VARCHAR,
    "Action Taken Primary" VARCHAR,
    "Action Taken Secondary" VARCHAR,
    "Action Taken Other" VARCHAR,
    "Detector Alerted Occupants" VARCHAR,
    "Property Use" VARCHAR,
    "Area of Fire Origin" VARCHAR,
    "Ignition Cause" VARCHAR,
    "Ignition Factor Primary" VARCHAR,
    "Ignition Factor Secondary" VARCHAR,
    "Heat Source" VARCHAR,
    "Item First Ignited" VARCHAR,
    "Human Factors Associated with Ignition" VARCHAR,
    "Structure Type" VARCHAR,
    "Structure Status" VARCHAR,
    "Floor of Fire Origin" NUMERIC,
    "Fire Spread" VARCHAR,
    "No Flame Spead" VARCHAR,
    "Number of floors with minimum damage" NUMERIC,
    "Number of floors with significant damage" NUMERIC,
    "Number of floors with heavy damage" NUMERIC,
    "Number of floors with extreme damage" NUMERIC,
    "Detectors Present" VARCHAR,
    "Detector Type" VARCHAR,
    "Detector Operation" VARCHAR,
    "Detector Effectiveness" VARCHAR,
    "Detector Failure Reason" VARCHAR,
    "Automatic Extinguishing System Present" VARCHAR,
    "Automatic Extinguishing Sytem Type" VARCHAR,
    "Automatic Extinguishing Sytem Perfomance" VARCHAR,
    "Automatic Extinguishing Sytem Failure Reason" VARCHAR,
    "Number of Sprinkler Heads Operating" NUMERIC,
    "Supervisor District" VARCHAR,
    "neighborhood_district" VARCHAR,
    "point" Point,
    "CurrentDate" VARCHAR
);