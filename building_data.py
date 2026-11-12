def hints_db(filepath):
    """Reads the data file a creates databse of building names and hints that correspond to them. 
    
    Args:
        filepath(str): path to file that contains building names and hints 
        
    Side effects: 
        Reads the file at filepath, Creates a dictionary that holds each building and the hints that go with it 
        
    Returns: 
        dict: maps each building name to a list of 5 hints
    
    """
    
    building_data = {}
    
    with open(filepath, "r", encoding="utf-8") as f:
        
        for line in f:
            if not line:
                continue 
            info = line.strip("\n").split("|")
            building_data[info[0]] = info[1:6]
            
    return building_data



