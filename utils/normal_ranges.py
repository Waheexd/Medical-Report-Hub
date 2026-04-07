# Reference dictionary for common lab tests
# Range is (low, high)
# Sections categorize tests (CBC, Lipid, BMP)
# Icons indicate status visually

NORMAL_RANGES = {
    # CBC Components
    "Hemoglobin": {"min": 13.5, "max": 17.5, "unit": "g/dL", "section": "COMPLETE BLOOD COUNT (CBC)"},
    "WBC": {"min": 4500, "max": 11000, "unit": "cells/µL", "section": "COMPLETE BLOOD COUNT (CBC)"},
    "RBC": {"min": 4.5, "max": 5.9, "unit": "million/µL", "section": "COMPLETE BLOOD COUNT (CBC)"},
    "Platelets": {"min": 150000, "max": 450000, "unit": "cells/µL", "section": "COMPLETE BLOOD COUNT (CBC)"},
    "Hematocrit": {"min": 41, "max": 50, "unit": "%", "section": "COMPLETE BLOOD COUNT (CBC)"},
    "MCV": {"min": 80, "max": 100, "unit": "fL", "section": "COMPLETE BLOOD COUNT (CBC)"},

    # Lipid Profile
    "Total Cholesterol": {"min": 0, "max": 200, "unit": "mg/dL", "section": "LIPID PROFILE"},
    "LDL": {"min": 0, "max": 100, "unit": "mg/dL", "section": "LIPID PROFILE"},
    "HDL": {"min": 60, "max": 100, "unit": "mg/dL", "section": "LIPID PROFILE", "higher_is_better": True},
    "Triglycerides": {"min": 0, "max": 150, "unit": "mg/dL", "section": "LIPID PROFILE"},

    # BMP Components
    "Glucose": {"min": 64, "max": 100, "unit": "mg/dL", "section": "BASIC METABOLIC PANEL (BMP)"},
    "Calcium": {"min": 8.5, "max": 10.2, "unit": "mg/dL", "section": "BASIC METABOLIC PANEL (BMP)"},
    "BUN": {"min": 6, "max": 20, "unit": "mg/dL", "section": "BASIC METABOLIC PANEL (BMP)"},
    "Creatinine": {"min": 0.6, "max": 1.3, "unit": "mg/dL", "section": "BASIC METABOLIC PANEL (BMP)"},
    "Sodium": {"min": 136, "max": 145, "unit": "mEq/L", "section": "BASIC METABOLIC PANEL (BMP)"},
    "Potassium": {"min": 3.5, "max": 5.2, "unit": "mEq/L", "section": "BASIC METABOLIC PANEL (BMP)"},
    "Chloride": {"min": 96, "max": 106, "unit": "mEq/L", "section": "BASIC METABOLIC PANEL (BMP)"},
    "CO2": {"min": 23, "max": 29, "unit": "mmol/L", "section": "BASIC METABOLIC PANEL (BMP)"},
}

STATUS_ICONS = {
    "Normal": "🟢",
    "High": "🔴",
    "Low": "🔵",
    "Unknown": "❓"
}

def check_value(test_name, value):
    """
    Check if a value is within the normal range.
    Returns: "Normal", "Low", "High"
    """
    if test_name not in NORMAL_RANGES:
        return "Unknown"
    
    ref = NORMAL_RANGES[test_name]
    
    if value < ref["min"]:
        return "Low"
    elif value > ref["max"]:
        return "High"
    else:
        return "Normal"
