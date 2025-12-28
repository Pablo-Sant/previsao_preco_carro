from pandas import Series
import pandas as pd
import re

  
    
def limpando_milhas(mileage: str):
    
    if not isinstance(mileage, str):
        return None
    
    try:
        mileage = mileage.lower()
        mileage = mileage.replace(',', '').replace('mi.', '').replace('mi', '')
        return float(mileage)
    
    except ValueError:
        return None

    
    
def feature_engine_size(engine: str):
    
    if not isinstance(engine, str):
        return None
    
    m = re.search(r'(\d\.\d)L', engine)
    
    return float(m.group(1)) if m else None

    
    
def feature_cilindros(engine: str):
    
    if not isinstance(engine, str):
        return None
    
    m = re.search(r'\b([0-9]{1,2})\b', engine)
    
    return int(m.group(1)) if m else None

    
    
def feature_turbo(engine: str):
    
    if not isinstance(engine, str):
        return False
    
    return 'turbo' in engine.lower()

        
    
def simplificando_cores(cor):
    
    if not isinstance(cor, str):
        return None
    
    cor = cor.lower()
    
    
    if 'black' in cor or 'ebony' in cor:
        return 'black'
    if 'white' in cor or 'ivory' in cor:
        return 'white'
    if 'gray' in cor or 'grey' in cor or 'charcoal' in cor or 'graphite' in cor:
        return 'gray'
    if 'silver' in cor:
        return 'silver'
    if 'red' in cor or 'rosso' in cor:
        return 'red'
    if 'yellow' in cor or 'giallo' in cor:
        return 'yellow'
    if 'blue' in cor:
        return 'blue'
    if 'orange' in cor or 'arancio' in cor:
        return 'orange'
    if 'beige' in cor or 'tan' in cor or 'carmel' in cor:
        return 'beige'
    if 'green' in cor:
        return 'green'
    return 'Other'
    
    
def metallic_ext(ext_color: str):
    
    if not isinstance(ext_color, str):
        return False
    
    return 'metallic' in ext_color.lower()

    
    
def encontrando_marcha(transmission: str):
    
    if not isinstance(transmission, str):
        return None

    transmission = transmission.upper()
    
    padrao = r'(\b[1-9]|10)\s*[- ]?\s*(SPEED|SPD|SP)?\b'

    m = re.search(padrao, transmission)
    
    return int(m.group(1)) if m else None



def type_transmission(t: str):
    
    if not isinstance(t, str):
        return None

    t = t.lower()

    if 'automatic' in t or 'a/t' in t:
        return 'Automatic'
    if 'cvt' in t:
        return 'CVT'
    if 'dual' in t or 'dct' in t:
        return 'DCT'
    if 'manual' in t or 'm/t' in t:
        return 'Manual'
    if 'single-speed' in t:
        return 'Single'
    return 'Other'



def build_features_single(data: dict) -> dict:
    
    return {
        "mileage": limpando_milhas(data.get("milage")),
        "engine_size": feature_engine_size(data.get("engine")),
        "engine_turbo": feature_turbo(data.get("engine")),
        "engine_cylinders": feature_cilindros(data.get("engine")),
        "color_simplified_int": simplificando_cores(data.get("int_color")),
        "color_simplified_ext": simplificando_cores(data.get("ext_color")),
        "is_metallic": metallic_ext(data.get("ext_color")),
        "speed_num": encontrando_marcha(data.get("transmission")),
        "type_transmission": type_transmission(data.get("transmission"))
    }
