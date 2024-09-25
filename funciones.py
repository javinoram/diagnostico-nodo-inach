##Para facilitar el procesamiento de nombres, se decidio eliminar todos los
##tildes y caracteres especiales (dierecis).
def limpiar_caracteres_especiales( string ):
    string = string.lower().strip()
    if 'á' in string or 'ä' in string:
        string = string.replace('ä', 'a').replace('á', 'a')
    if 'é' in string or 'ë' in string: 
        string = string.replace('é', 'e').replace('ë', 'e')
    if 'í' in string or 'ï' in string:
        string = string.replace('í', 'i').replace('ï', 'i')
    if 'ó' in string or 'ö' in string:
        string = string.replace('ó', 'o').replace('ö', 'o')
    if 'ú' in string or 'ü' in string:
        string = string.replace('ú', 'u').replace('ü', 'u')
    return string

##La idea es que dada la descripcion de la funcion, buscar palabras claves que permitan
##determinar que cargo tuvo dentro de la expedicion, al final, se aplica una jerarquizacion para solo
##dejar un cargo
def limpiar_funciones(x):
    if type(x) != str:
        return x
    
    final = ""

    if 'noinf' == x:
        return 'noinf'

    if 'ingeniero' in x.lower():
        if final!="": final+="-"
        final+="ING"
     
    if 'jefe' in x.lower() or 'jefa' in x.lower() or 'leader' in x.lower():
        if final!="": final+="-"
        final+="COO"
        
    elif 'coordi' in x.lower():
        if final!="": final+="-"
        final+="COO"

    if 'invest' in x.lower() or 'cientifico' in x.lower() or 'botanico' in x.lower() or 'microbiologa' in x.lower() or 'oceanografia fisica' in x.lower():
        if final!="": final+="-"
        final+="INV"

    if 'montaña' in x.lower() or 'mountain' in x.lower():
        if final!="": final+="-"
        final+="TECN"
        
    elif 'tecnico' in x.lower() or 'tecnico' in x.lower() or 'technician' in x.lower() or 'encargado' in x.lower() or 'mantencion' in x.lower():
        if final!="": final+="-"
        final+="TECN"

    elif 'buzo' in x.lower() or 'buceo' in x.lower():
        if final!="": final+="-"
        final+="TECN"

    if 'estudiante' in x.lower() or 'posdoc' in x.lower():
        if final!="": final+="-"
        final+="EST"
        
    elif 'tesis' in x.lower():
        if final!="": final+="-"
        final+="EST"

    if 'asisten' in x.lower() or 'ayudante' in x.lower() or 'apoyo' in x.lower():
        if final!="": final+="-"
        final+="AST"
        
    elif ('toma' in x.lower() or 'colec' in x.lower()):
        if final!="": final+="-"
        final+="AST"
        
    elif 'muestr' in x.lower() or 'procesamiento' in x.lower() or 'analisis' in x.lower() or 'sampling' in x.lower():
        if final!="": final+="-"
        final+="AST"

    if final=="": return "OTRO"
    
    if 'INV' in final: return 'INV'
    elif 'COO' in final: return 'COO'
    elif 'EST' in final: return 'EST'
    elif 'ING' in final: return 'ING'
    elif 'AST' in final: return 'AST'
    else: return 'TECN'

##La idea que dependiendo del codigo, se determine que instrumento se uso 
##para su financiamiento
def instrumento_financiamiento( codigo ):
    final = 'noinf'
    if codigo in ["MT", "MG", "DT", "DG", "RG", "AMP", "RT", "AM"]:
        final = "INACH"
    elif codigo in ["FP", "FI", "FR", "PR"]:
        final = "FONDECYT"
    elif codigo in ["FOVI", "FV"]:
        final = "FOMENTO"
    elif codigo in ["INT", "IN"]:
        final = "INTER"
    elif codigo in ["FE"]:
        final = "FONDEQUIP"
    elif codigo in ["NE"]:
        final = "NODO"
    elif codigo in ["AN"]:
        final = "ANILLO"
    elif codigo in ["MI", "IM"]:
        final = "MILENIO"
    elif codigo in ["FD", "FO"]:
        final = "FONDAP"
    elif codigo in ["CI", "PC", "AG", "PCI", "FIC"]:
        final = "CONICYT"
    elif codigo in ["CE"]:
        final = "CECs"
    elif codigo in ["CO"]:
        final = "CORFO"
    elif codigo in ["MA"]:
        final = "UMAG"
    elif codigo in ["OA"]:
        final = "OPERADORES ANTARTICOS"
    elif codigo in ["GU"]:
        final = "GLACIAR UNION"
    return final

##Aca se agrupan los instrumentos segun la institucion que las entrega
def institucion_instrumento( codigo ):
    sigla = codigo.split('-')[0]
    if sigla in ['GU']:
        return 'GLACIAR UNION'
    if sigla in ['OA']:
        return 'OP. ANTART'
    if sigla in ['CO']:
        return 'CORFO'
    if sigla in ['MA']:
        return 'UMAG'
    if sigla in ['CE']:
        return 'CECs'
    if sigla in ["AM", "DG", "DT", "MG", "MT", "RG", "RT", "AMP"]:
        return 'INACH'
    if sigla in ['AG', 'AN', 'CI', 'FD', 'FE', 'FI', 'FO', 'FOVI', 'FP', 'FR', 
        'FV', 'IM', 'IN', 'INT', 'NE', 'PC', 'PR', 'MI', "PCI", "FIC"]:
        return 'ANID'
    return 'noinf'

##La idea de esta funcion es determinar si el codigo es de un proyecto
##de magister, doctorado, regular, internacional, externo
def descripcion_codigo_inach( codigo ):
    sigla = codigo.split('-')[0]
    if sigla in ['MT', 'MG']:
        if sigla == 'MG':
            return 'magister', 'tesis', 'gabinete'
        else:
            return 'magister', 'tesis', 'terreno'
    elif sigla in ['DT', 'DG']:
        if sigla == 'DG':
            return 'doctorado', 'tesis', 'gabinete'
        else:
            return 'doctorado', 'tesis', 'terreno'
    elif sigla in ['RG', 'RT']:
        if sigla == 'RG':
            return 'regular', 'noinf', 'gabinete'
        else:
            return 'regular', 'noinf', 'terreno'
    elif sigla in ['INT', 'IN']:
        return 'internacional', 'noinf', 'noinf'
    else:
        return 'externo', 'noinf', 'noinf'
    
##La idea es categorizar los proyectos concursables de los que no lo son
def proyecto_concursable( string ):
    if string in ['AMP', 'CE', 'INT', 'IN', 'MA', 'OA']:
        return 'no concursable'
    return 'concursable'


##Llaves son instituciones chilenas con nombres normalizados
region_institucion = {
    #otros
    '': 'noinf',
    'otro': 'noinf',
    'noinf': 'noinf',
    'fundacion bioceanica': 'noinf',
    'extranjero': 'extranjero',
    #metropolitana
    'fundacion cientifica y cultural biociencia': 'metropolitana',
    'consejo de monumentos nacionales': 'metropolitana',
    'univ. autonoma': 'metropolitana',
    'univ. de santiago de chile': 'metropolitana',
    'univ. de chile': 'metropolitana',
    'univ. del desarrollo': 'metropolitana',
    'univ. andres bello': 'metropolitana',
    'univ. catolica de chile': 'metropolitana',
    'univ. mayor': 'metropolitana',
    'univ. metropolitana': 'metropolitana',
    'univ. santo tomas': 'metropolitana',
    'univ. adolfo ibañez': 'metropolitana',
    'univ. arturo prat': 'metropolitana',
    'univ. san sebastian': 'metropolitana',
    'inst. milenio base': 'metropolitana',
    'univ. de las americas': 'metropolitana',
    'inst. de ecologia y biodiversidad': 'metropolitana',
    'inst. de nutricion y tecnologia de los alimentos': 'metropolitana',
    'museo natural de historia natural': 'metropolitana',
    'min. de obras publicas': 'metropolitana',
    'meteochile': 'metropolitana',
    'univ. bernardo ohiggins': 'metropolitana',
    'universidad de las americas': 'metropolitana',
    'comision chilena de energia nuclear': 'metropolitana',
    #valparaiso
    'univ. de valparaiso': 'valparaiso',
    'univ. catolica de valparaiso': 'valparaiso',
    'univ. de viña del mar': 'valparaiso',
    'univ. de playa ancha': 'valparaiso',
    'univ. tecnica federico santa maria': 'valparaiso',
    #magallanes
    'univ. de magallanes': 'magallanes',
    'inst. antartico chileno': 'magallanes',
    'centro internacional cabo de hornos': 'magallanes',
    'fundacion cequa': 'magallanes',
    #antofagasta
    'univ. de antofagasta': 'antofagasta',
    'univ. catolica del norte': 'antofagasta',
    #atacama
    'univ. de atacama': 'atacama',
    #coquimbo
    'centro de estudios avanzados en zonas aridas': 'coquimbo',
    #bio bio
    'univ. del bio bio': 'bio bio',
    'univ. de concepcion': 'bio bio',
    'univ. catolica de la santisima concepcion': 'bio bio',
    #maule
    'univ. de talca': 'maule',
    'univ. catolica del maule': 'maule',
    #araucania
    'univ. de la frontera': 'araucania',
    'univ. catolica de temuco': 'araucania',
    #los lagos
    'univ. de los lagos': 'los lagos',
    #los rios
    'univ. austral de chile': 'los rios',
    'centro de estudios cientificos de valdivia': 'los rios',
    #aysen
    'centro de investigacion en ecosistemas de la patagonia': 'aysen',
    #ohiggins
    'univ. de ohiggins': 'ohiggins'
}


##Llaves son regiones de chile con nombres normalizados
macrozona_region = {
    'arica': 'norte',
    'antofagasta': 'norte',
    'tarapaca': 'norte',
    'atacama': 'norte',
    'coquimbo': 'centro',
    'valparaiso': 'centro',
    'ohiggins': 'centro sur',
    'maule': 'centro sur',
    'ñuble': 'centro sur',
    'bio bio': 'centro sur',
    'araucania': 'sur',
    'los rios': 'sur',
    'los lagos': 'sur',
    'aysen': 'austral',
    'magallanes': 'austral',
    'metropolitana': 'metropolitana',
    'extranjero': 'extranjero',
    'noinf': 'noinf'
}

##Las llaves son todas las formas en que aparecen los nombres de las ciudades
normalizacion_ciudad = {
    'viña del mar': 'viña del mar',
    'valparaiso': 'valparaiso',
    'valpariso': 'valparaiso',
    'puerto montt': 'puerto montt',
    'pto. montt': 'puerto montt',
    'pto montt': 'puerto montt',
    'pto. williams': 'puerto williams',
    'puerto williams': 'puerto williams',
    'la serena': 'la serena',
    'coquimbo': 'coquimbo',
    'los angeles': 'los angeles',
    'talca': 'talca',
    'valdivia': 'valdivia',
    'antofagasta': 'antofagasta',
    'noinf': 'noinf',
    'santiago': 'santiago',
    'chillan': 'chillan',
    'talcahuano': 'talcahuano',
    'temuco': 'temuco',
    'punta arenas': 'punta arenas',
    'concepcion': 'concepcion',
}

##En base a las ciudades anteriores, estas se asocian a una region del pais
ciudad_a_region = {
    'viña del mar': 'valparaiso',
    'valparaiso': 'valparaiso',
    'puerto montt': 'los lagos',
    'puerto williams': 'magallanes',
    'la serena': 'coquimbo',
    'coquimbo': 'coquimbo',
    'los angeles': 'bio bio',
    'talca': 'maule',
    'valdivia': 'los rios',
    'antofagasta': 'antofagasta',
    'noinf': 'noinf',
    'santiago': 'metropolitana',
    'chillan': 'ñuble',
    'talcahuano': 'bio bio',
    'temuco': 'araucania',
    'punta arenas': 'magallanes',
    'concepcion': 'bio bio',
}