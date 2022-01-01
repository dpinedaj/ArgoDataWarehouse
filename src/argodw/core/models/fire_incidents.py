from argodw.core.models.base import Base

class RawFireIncidentsModel(Base):
    pass

class ProcessedFireIncidentsModel(Base):
    pass


{
    "Incident Number": "numeric",
    "Exposure Number": "numeric",
    "ID": "varchar",
    "Address": "varchar",
    "Incident Date": "varchar",
    "Call Number": "varchar",
    "Alarm DtTm": "varchar",
    "Arrival DtTm": "varchar",
    "Close DtTm": "varchar",
    "City": "varchar",
    "zipcode": "varchar",
    "Battalion": "varchar",
    "Station Area": "varchar",
    "Box": "varchar",
    "Suppression Units": "numeric",
    "Suppression Personnel": "numeric",
    "EMS Units": "numeric",
    "EMS Personnel": "numeric",
    "Other Units": "numeric",
    "Other Personnel": "numeric",
    "First Unit On Scene": "varchar",
    "Estimated Property Loss": "numeric",
    "Estimated Contents Loss": "numeric",
    "Fire Fatalities": "numeric",
    "Fire Injuries": "numeric",
    "Civilian Fatalities": "numeric",
    "Civilian Injuries": "numeric",
    "Number of Alarms": "numeric",
    "Primary Situation": "varchar",
    "Mutual Aid": "varchar",
    "Action Taken Primary": "varchar",
    "Action Taken Secondary": "varchar",
    "Action Taken Other": "varchar",
    "Detector Alerted Occupants": "varchar",
    "Property Use": "varchar",
    "Area of Fire Origin": "varchar",
    "Ignition Cause": "varchar",
    "Ignition Factor Primary": "varchar",
    "Ignition Factor Secondary": "varchar",
    "Heat Source": "varchar",
    "Item First Ignited": "varchar",
    "Human Factors Associated with Ignition": "varchar",
    "Structure Type": "varchar",
    "Structure Status": "varchar",
    "Floor of Fire Origin": "numeric",
    "Fire Spread": "varchar",
    "No Flame Spead": "varchar",
    "Number of floors with minimum damage": "numeric",
    "Number of floors with significant damage": "numeric",
    "Number of floors with heavy damage": "numeric",
    "Number of floors with extreme damage": "numeric",
    "Detectors Present": "varchar",
    "Detector Type": "varchar",
    "Detector Operation": "varchar",
    "Detector Effectiveness": "varchar",
    "Detector Failure Reason": "varchar",
    "Automatic Extinguishing System Present": "varchar",
    "Automatic Extinguishing Sytem Type": "varchar",
    "Automatic Extinguishing Sytem Perfomance": "varchar",
    "Automatic Extinguishing Sytem Failure Reason": "varchar",
    "Number of Sprinkler Heads Operating": "numeric",
    "Supervisor District": "varchar",
    "neighborhood_district": "varchar",
    "point": "point"
}