class tmi_pujo():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'TimetableVersionCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'OrganizationalUnitCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'PeriodGroupCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'SpecificDayCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'DayType', 'aard': '#', 'type': 'N', 'length': 7 },
            {'name': 'LinePlanningNumber', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'JourneyNumber', 'aard': '#', 'type': 'N', 'length': 6 },
            {'name': 'TimeDemandGroupCode', 'aard': '+', 'type': 'A', 'length': 10 },
            {'name': 'JourneyPatternCode', 'aard': '+', 'type': 'A', 'length': 10 },
            {'name': 'DepartureTime', 'aard': '+', 'type': 'T', 'length': 8 },
            {'name': 'WheelChairAccessible', 'aard': '+', 'type': 'B', 'length': 5 },
            {'name': 'DataOwnerIsOperator', 'aard': '+', 'type': 'B', 'length': 5 },
        ]

    def parse(self, version, implicit, data_owner_code, elements):
        timetable_version_code, organizational_unit_code, period_group_rode, specific_day_code, day_type, line_planning_number, journey_number, time_demand_group_code, journey_pattern_code, departure_time, wheel_chair_accessible, data_owner_is_operator = elements
        if (wheel_chair_accessible == 'ACCESSIBLE'):
            wheel_chair_accessible = 'true'
        elif (wheel_chair_accessible == 'NOTACCESSIBLE'):
            wheel_chair_accessible = 'false'
        else:
            wheel_chair_accessible = ''
        self.data.append([version, implicit, data_owner_code, timetable_version_code, organizational_unit_code, period_group_rode, specific_day_code, day_type, line_planning_number, journey_number, time_demand_group_code, journey_pattern_code, departure_time, wheel_chair_accessible, data_owner_is_operator])
