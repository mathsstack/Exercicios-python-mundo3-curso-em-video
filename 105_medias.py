def media(*notas):
    
    """
    Calcs the media of the notes of a pupil
    
    *notas: notes
    """
    
    media = 0;
    
    for c in notas:
        for v in c:
            media += v
        
    media /= len(notas[0])
    
    return media
    

def notas(*notas, show_situation=False):
    
    """
    Makes a statistic of the notes of a pupil
    
    *notas: notes
    show_situation: shows the situation of the pupil
    """
    
    logs = dict()
    
    logs["qtde_notes"] = len(notas)
    logs["higher_note"] = sorted(notas)[-1]
    logs["lower_note"] = sorted(notas)[0]
    logs["media"] = media(notas)
    
    if show_situation == True:
        logs["situation"] = "Aproved" if logs["media"] > 5 else "Reproved"
    
    return logs
    
print(notas(10, 9, 9, 6))
help(notas)
