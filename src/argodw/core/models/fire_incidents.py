from sqlalchemy import Column, VARCHAR, NUMERIC
from geoalchemy2 import Geometry

from argodw.core.models.base import Raw, Processed, MapeableBase

class RawFireIncidentsModel(Raw, MapeableBase):
    __tablename__ = 'fire_incidents'
    
    IncidentNumber = Column("Incident Number", VARCHAR, nullable=True)
    ExposureNumber = Column("Exposure Number", VARCHAR, nullable=True)
    ID = Column("ID", VARCHAR, nullable=True)
    Address = Column("Address", VARCHAR, nullable=True)
    IncidentDate = Column("Incident Date", VARCHAR, nullable=True)
    CallNumber = Column("Call Number", VARCHAR, nullable=True)
    AlarmDtTm = Column("Alarm DtTm", VARCHAR, nullable=True)
    ArrivalDtTm = Column("Arrival DtTm", VARCHAR, nullable=True)
    CloseDtTm = Column("Close DtTm", VARCHAR, nullable=True)
    City = Column("City", VARCHAR, nullable=True)
    zipcode = Column("zipcode", VARCHAR, nullable=True)
    Battalion = Column("Battalion", VARCHAR, nullable=True)
    StationArea = Column("Station Area", VARCHAR, nullable=True)
    Box = Column("Box", VARCHAR, nullable=True)
    SuppressionUnits = Column("Suppression Units", VARCHAR, nullable=True)
    SuppressionPersonnel = Column("Suppression Personnel", VARCHAR, nullable=True)
    EMSUnits = Column("EMS Units", VARCHAR, nullable=True)
    EMSPersonnel = Column("EMS Personnel", VARCHAR, nullable=True)
    OtherUnits = Column("Other Units", VARCHAR, nullable=True)
    OtherPersonnel = Column("Other Personnel", VARCHAR, nullable=True)
    FirstUnitOnScene = Column("First Unit On Scene", VARCHAR, nullable=True)
    EstimatedPropertyLoss = Column("Estimated Property Loss", VARCHAR, nullable=True)
    EstimatedContentsLoss = Column("Estimated Contents Loss", VARCHAR, nullable=True)
    FireFatalities = Column("Fire Fatalities", VARCHAR, nullable=True)
    FireInjuries = Column("Fire Injuries", VARCHAR, nullable=True)
    CivilianFatalities = Column("Civilian Fatalities", VARCHAR, nullable=True)
    CivilianInjuries = Column("Civilian Injuries", VARCHAR, nullable=True)
    NumberofAlarms = Column("Number of Alarms", VARCHAR, nullable=True)
    PrimarySituation = Column("Primary Situation", VARCHAR, nullable=True)
    MutualAid = Column("Mutual Aid", VARCHAR, nullable=True)
    ActionTakenPrimary = Column("Action Taken Primary", VARCHAR, nullable=True)
    ActionTakenSecondary = Column("Action Taken Secondary", VARCHAR, nullable=True)
    ActionTakenOther = Column("Action Taken Other", VARCHAR, nullable=True)
    DetectorAlertedOccupants = Column("Detector Alerted Occupants", VARCHAR, nullable=True)
    PropertyUse = Column("Property Use", VARCHAR, nullable=True)
    AreaofFireOrigin = Column("Area of Fire Origin", VARCHAR, nullable=True)
    IgnitionCause = Column("Ignition Cause", VARCHAR, nullable=True)
    IgnitionFactorPrimary = Column("Ignition Factor Primary", VARCHAR, nullable=True)
    IgnitionFactorSecondary = Column("Ignition Factor Secondary", VARCHAR, nullable=True)
    HeatSource = Column("Heat Source", VARCHAR, nullable=True)
    ItemFirstIgnited = Column("Item First Ignited", VARCHAR, nullable=True)
    HumanFactorsAssociatedwithIgnition = Column("Human Factors Associated with Ignition", VARCHAR, nullable=True)
    StructureType = Column("Structure Type", VARCHAR, nullable=True)
    StructureStatus = Column("Structure Status", VARCHAR, nullable=True)
    FloorofFireOrigin = Column("Floor of Fire Origin", VARCHAR, nullable=True)
    FireSpread = Column("Fire Spread", VARCHAR, nullable=True)
    NoFlameSpead = Column("No Flame Spead", VARCHAR, nullable=True)
    Numberoffloorswithminimumdamage = Column("Number of floors with minimum damage", VARCHAR, nullable=True)
    Numberoffloorswithsignificantdamage = Column("Number of floors with significant damage", VARCHAR, nullable=True)
    Numberoffloorswithheavydamage = Column("Number of floors with heavy damage", VARCHAR, nullable=True)
    Numberoffloorswithextremedamage = Column("Number of floors with extreme damage", VARCHAR, nullable=True)
    DetectorsPresent = Column("Detectors Present", VARCHAR, nullable=True)
    DetectorType = Column("Detector Type", VARCHAR, nullable=True)
    DetectorOperation = Column("Detector Operation", VARCHAR, nullable=True)
    DetectorEffectiveness = Column("Detector Effectiveness", VARCHAR, nullable=True)
    DetectorFailureReason = Column("Detector Failure Reason", VARCHAR, nullable=True)
    AutomaticExtinguishingSystemPresent = Column("Automatic Extinguishing System Present", VARCHAR, nullable=True)
    AutomaticExtinguishingSytemType = Column("Automatic Extinguishing Sytem Type", VARCHAR, nullable=True)
    AutomaticExtinguishingSytemPerfomance = Column("Automatic Extinguishing Sytem Perfomance", VARCHAR, nullable=True)
    AutomaticExtinguishingSytemFailureReason = Column("Automatic Extinguishing Sytem Failure Reason", VARCHAR,nullable=True)
    NumberofSprinklerHeadsOperating = Column("Number of Sprinkler Heads Operating", VARCHAR, nullable=True)
    SupervisorDistrict = Column("Supervisor District", VARCHAR, nullable=True)
    neighborhooddistrict = Column("neighborhood_district", VARCHAR, nullable=True)
    point = Column("point", VARCHAR, nullable=True)

class ProcessedFireIncidentsModel(Processed, MapeableBase):
    __tablename__ = 'fire_incidents'

    IncidentNumber = Column("Incident Number", NUMERIC, nullable=True)
    ExposureNumber = Column("Exposure Number", NUMERIC, nullable=True)
    ID = Column("ID", VARCHAR, nullable=True)
    Address = Column("Address", VARCHAR, nullable=True)
    IncidentDate = Column("Incident Date", VARCHAR, nullable=True)
    CallNumber = Column("Call Number", VARCHAR, nullable=True)
    AlarmDtTm = Column("Alarm DtTm", VARCHAR, nullable=True)
    ArrivalDtTm = Column("Arrival DtTm", VARCHAR, nullable=True)
    CloseDtTm = Column("Close DtTm", VARCHAR, nullable=True)
    City = Column("City", VARCHAR, nullable=True)
    zipcode = Column("zipcode", VARCHAR, nullable=True)
    Battalion = Column("Battalion", VARCHAR, nullable=True)
    StationArea = Column("Station Area", VARCHAR, nullable=True)
    Box = Column("Box", VARCHAR, nullable=True)
    SuppressionUnits = Column("Suppression Units", NUMERIC, nullable=True)
    SuppressionPersonnel = Column("Suppression Personnel", NUMERIC, nullable=True)
    EMSUnits = Column("EMS Units", NUMERIC, nullable=True)
    EMSPersonnel = Column("EMS Personnel", NUMERIC, nullable=True)
    OtherUnits = Column("Other Units", NUMERIC, nullable=True)
    OtherPersonnel = Column("Other Personnel", NUMERIC, nullable=True)
    FirstUnitOnScene = Column("First Unit On Scene", VARCHAR, nullable=True)
    EstimatedPropertyLoss = Column("Estimated Property Loss", NUMERIC, nullable=True)
    EstimatedContentsLoss = Column("Estimated Contents Loss", NUMERIC, nullable=True)
    FireFatalities = Column("Fire Fatalities", NUMERIC, nullable=True)
    FireInjuries = Column("Fire Injuries", NUMERIC, nullable=True)
    CivilianFatalities = Column("Civilian Fatalities", NUMERIC, nullable=True)
    CivilianInjuries = Column("Civilian Injuries", NUMERIC, nullable=True)
    NumberofAlarms = Column("Number of Alarms", NUMERIC, nullable=True)
    PrimarySituation = Column("Primary Situation", VARCHAR, nullable=True)
    MutualAid = Column("Mutual Aid", VARCHAR, nullable=True)
    ActionTakenPrimary = Column("Action Taken Primary", VARCHAR, nullable=True)
    ActionTakenSecondary = Column("Action Taken Secondary", VARCHAR, nullable=True)
    ActionTakenOther = Column("Action Taken Other", VARCHAR, nullable=True)
    DetectorAlertedOccupants = Column("Detector Alerted Occupants", VARCHAR, nullable=True)
    PropertyUse = Column("Property Use", VARCHAR, nullable=True)
    AreaofFireOrigin = Column("Area of Fire Origin", VARCHAR, nullable=True)
    IgnitionCause = Column("Ignition Cause", VARCHAR, nullable=True)
    IgnitionFactorPrimary = Column("Ignition Factor Primary", VARCHAR, nullable=True)
    IgnitionFactorSecondary = Column("Ignition Factor Secondary", VARCHAR, nullable=True)
    HeatSource = Column("Heat Source", VARCHAR, nullable=True)
    ItemFirstIgnited = Column("Item First Ignited", VARCHAR, nullable=True)
    HumanFactorsAssociatedwithIgnition = Column("Human Factors Associated with Ignition", VARCHAR, nullable=True)
    StructureType = Column("Structure Type", VARCHAR, nullable=True)
    StructureStatus = Column("Structure Status", VARCHAR, nullable=True)
    FloorofFireOrigin = Column("Floor of Fire Origin", NUMERIC, nullable=True)
    FireSpread = Column("Fire Spread", VARCHAR, nullable=True)
    NoFlameSpead = Column("No Flame Spead", VARCHAR, nullable=True)
    Numberoffloorswithminimumdamage = Column("Number of floors with minimum damage", NUMERIC, nullable=True)
    Numberoffloorswithsignificantdamage = Column("Number of floors with significant damage", NUMERIC, nullable=True)
    Numberoffloorswithheavydamage = Column("Number of floors with heavy damage", NUMERIC, nullable=True)
    Numberoffloorswithextremedamage = Column("Number of floors with extreme damage", NUMERIC, nullable=True)
    DetectorsPresent = Column("Detectors Present", VARCHAR, nullable=True)
    DetectorType = Column("Detector Type", VARCHAR, nullable=True)
    DetectorOperation = Column("Detector Operation", VARCHAR, nullable=True)
    DetectorEffectiveness = Column("Detector Effectiveness", VARCHAR, nullable=True)
    DetectorFailureReason = Column("Detector Failure Reason", VARCHAR, nullable=True)
    AutomaticExtinguishingSystemPresent = Column("Automatic Extinguishing System Present", VARCHAR, nullable=True)
    AutomaticExtinguishingSytemType = Column("Automatic Extinguishing Sytem Type", VARCHAR, nullable=True)
    AutomaticExtinguishingSytemPerfomance = Column("Automatic Extinguishing Sytem Perfomance", VARCHAR, nullable=True)
    AutomaticExtinguishingSytemFailureReason = Column("Automatic Extinguishing Sytem Failure Reason", VARCHAR,nullable=True)
    NumberofSprinklerHeadsOperating = Column("Number of Sprinkler Heads Operating", NUMERIC, nullable=True)
    SupervisorDistrict = Column("Supervisor District", VARCHAR, nullable=True)
    neighborhooddistrict = Column("neighborhood_district", VARCHAR, nullable=True)
    point = Column("point", Geometry('POINT'), nullable=True)
