



def get_severity_code(severity: int | str):
    """
    Following RFC 5424 Specs :
    0       Emergency: system is unusable
    1       Alert: action must be taken immediately
    2       Critical: critical conditions
    3       Error: error conditions
    4       Warning: warning conditions
    5       Notice: normal but significant condition
    6       Informational: informational messages
    7       Debug: debug-level messages
    """
    code_map = {
        0:"emergency",
        1:"alert",
        2:"critical",
        3:"error",
        4:"warning",
        5:"notice" ,
        6:"informational",
        7:"debug"
    }
    if isinstance(severity, str):
        for code_key, code_text in code_map.items():
            if severity.lower() == code_text:
                return code_key
        # If we reach this point then the input str is not correct
        raise ValueError(f"Input str is valid, must be within the following map {code_map}")
    elif isinstance(severity, int):
        return code_map[severity]
    else:
        raise TypeError("Input type must be int or str !")