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
    


def simplificar_cores(color_int: str, color_ext: str) -> dict:
    
    return {
        
        "color_simplified_int": simplificando_cores(color_int),
        "color_simplified_ext": simplificando_cores(color_ext)   
    }
