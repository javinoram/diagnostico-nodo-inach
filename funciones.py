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

    if 'invest' in x.lower() or 'cientifico' in x.lower() or 'botanico' in x.lower() or 'microbiologa' in x.lower() or 'oceanografia fisica' in x.lower() or 'posdoc' in x.lower():
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

    if 'estudiante' in x.lower():
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

    if final=="": return "Otro"
    
    if 'INV' in final: return 'Investigador'
    elif 'COO' in final: return 'Coordinador'
    elif 'EST' in final: return 'Estudiante'
    elif 'ING' in final: return 'Ingeniero'
    elif 'AST' in final: return 'Asistente'
    else: return 'Tecnico'

##La idea que dependiendo del codigo, se determine que instrumento se uso 
##para su financiamiento
def instrumento_financiamiento( codigo ):
    final = 'noinf'
    if codigo in ["MT", "MG", "DT", "DG", "RG", "AMP", "RT", "AM", "PR"]:
        final = "INACH"
    elif codigo in ["FP", "FI", "FR"]:
        final = "FONDECYT"
    elif codigo in ["FOVI", "FV"]:
        final = "FOMENTO"
    elif codigo in ["INT", "IN", "AG"]:
        final = "INTER"
    elif codigo in ["FE"]:
        final = "FONDEQUIP"
    elif codigo in ["NE"]:
        final = "NODO"
    elif codigo in ["AN"]:
        final = "ANILLO"
    elif codigo in ["MI", "IM"]:
        final = "MILENIO"
    elif codigo in ["FD"]:
        final = "FONDAP"
    elif codigo in ["FO"]:
        final = "FONDEF"
    elif codigo in ["CI", "PC", "PCI", "FIC"]:
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
    if sigla in ["AM", "DG", "DT", "MG", "MT", "RG", "RT", "AMP", "PR"]:
        return 'INACH'
    if sigla in ['AN', 'CI', 'FD', 'FE', 'FI', 'FO', 'FOVI', 'FP', 'FR', 
        'FV', 'IM', 'IN', 'INT', 'NE', 'PC', 'MI', "PCI", "FIC"]:
        return 'ANID'
    return 'noinf'

##La idea de esta funcion es determinar si el codigo es de un proyecto
##de magister, doctorado, regular, internacional, externo
def descripcion_codigo_inach( codigo ):
    sigla = codigo.split('-')[0]
    if sigla in ['PR']:
        return 'pregrado', 'tesis', 'terreno'
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


##La idea es categorizar el texto del funding de los papers en una de las
##categorias definidas
def categorizacion_fondos_wos( string ):
    string = limpiar_caracteres_especiales( string ).lower().strip()
    
    ##Categoria INACH
    if 'inach' in string or 'eca' in 'string' or 'chilean antarctic institute' in string or 'instituto antartico chileno' in string:
        return 'inach'
    elif 'instituto chileno antartico' in string or 'chilean antarctic program' in string or 'instituto antarctico chileno' in string:
        return 'inach'
    elif 'chilean antarctic scientific program' in string or 'antarctic chilean institute' in string:
        return 'inach'
    
    ##Categoria CORFO
    elif 'corfo' in string or 'innova' in string:
        return 'corfo'
    
    ##Categoria UNIVERSIDADES
    elif 'universidad' in string or 'usach' in string or 'uach' in string or 'unab' in string or 'umag' in string:
        return 'universidad'
    elif 'universidad de chile' in string or 'universidad de magallanes' in string or 'utfsm' in string:
        return 'universidad'
    elif 'ucsc' in string or 'university of chile' in string or 'university of magellan' in string:
        return 'universidad'
    elif 'university of santiago' in string or 'universidad de santiago' in string or 'university of temuco' in string:
        return 'universidad'
    elif 'university of los lagos' in string or 'university of tarapaca' in string or 'u. chile' in string:
        return 'universidad'
    elif 'university of magallanes' in string or 'university of la serena' in string or 'university of concepcion' in string:
        return 'universidad'
    elif 'university of valparaiso' in string or 'ucsc' in string or 'pucv' in string or 'puc' in string:
        return 'universidad'
    elif 'la frontera university' in string or 'ufro' in string or 'univeridad de talca' in string or 'usm' in string:
        return 'universidad'
    elif 'university andres bello' in string:
        return 'universidad'

    ##Categoria otros
    elif 'fondart' in string or 'copas' in string or 'conaf' in string or 'cimaa' in string or 'mineduc' in string:
        return 'otro'
    elif 'ministry of education of chile' in string or 'armada de chile' in string or 'chilean fisheries research' in string:
        return 'otro'
    elif 'chilean air force' in string or 'chilean navy' in string or 'chilean army' in string:
        return 'otro'
    elif 'correos de chile' in string or 'chilean government' in string or "chile's government" in string:
        return 'otro'
    elif 'institute of ecology and biodiversity' in string or 'cequa' in string or 'cecs' in string:
        return 'otro'

    ##Categoria ANID
    elif 'anid' in string or 'conicyt' in string or 'fondap' in string or 'fondecyt' in string or 'millenium' in string:
        return 'anid'
    elif 'comision nacional de investigacion cientifica y tecnologica' in string or 'conicet' in string:
        return 'anid'
    elif 'agencia nacional de investigacion y desarrollo' in string or 'fonde- cyt' in string:
        return 'anid'
    elif 'programa bicentenario de ciencia y tecnologia' in string or 'fonde-cyt' in string:
        return 'anid'
    elif 'basal' in string or 'fondep' in string or 'fondequip' in string or 'ideal' in string:
        return 'anid'
    elif 'milenio' in string or 'millennium' in string or 'pecha' in string or 'anillo' in string:
        return 'anid'
    elif 'pia' in string or 'becas chile' in string or 'pai' in string or 'chilean ministry' in string:
        return 'anid'
    elif 'fondo nacional de desarrollo cientifico y tecnologico' in string or 'fonecyt' in string:
        return 'anid'
    elif 'fondef' in string or 'comision nacional de ciencia y tecnologia' in string or 'conacyt' in string:
        return 'anid'
    elif 'becas-chile' in string or 'becaschile' in string:
        return 'anid'
    elif 'consejo nacional de investigaciones cientificas y tecnologicas' in string or 'agencia nacional de promocion cientifica y tecnologica' in string:
        return 'anid'
    
    ##Categoria extranjero
    elif 'china' in string or 'uruguay' in string or 'italia' in string or 'russia' in string or 'japan' in string:
        return 'extranjero'
    elif 'french' in string or 'belgium' in string or 'bulgaria' in string or 'brazil' in string or 'german' in string:
        return 'extranjero'
    elif 'nasa' in string or 'danish' in string or 'australia' in string or 'africa' in string or 'new zealand' in string:
        return 'extranjero'
    elif 'spanish' in string or 'european' in string or 'chinese' in string or 'brasil' in string or 'swedish' in string:
        return 'extranjero'
    elif 'ecuador' in string or 'swiss' in string or 'british' in string or 'argentin' in string or 'austria' in string:
        return 'extranjero'
    elif 'korea' in string or 'polish' in string or 'poland' in string or 'finland' in string or 'finnish' in string:
        return 'extranjero'
    elif 'singapore' in string or 'malaysia' in string or 'istanbul' in string or 'ireland' in string or 'czech' in string:
        return 'extranjero'
    elif 'portuguese' in string or 'united kingdom' in string or 'ukrainia' in string or 'canadia' in string or 'conselho' in string:
        return 'extranjero'
    elif 'america' in string or 'u.s' in string or 'france' in string or 'peru' in string or 'texas' in string or 'otago' in string:
        return 'extranjero'
    elif 'united states' in string or 'sweden' in string or 'oxford' in string or 'portugal' in string or 'italy' in string:
        return 'extranjero'
    elif 'sao paulo' in string or 'geneva' in string or 'ukri' in string or 'nerc' in string or 'netherland' in string or 'london' in string:
        return 'extranjero'
    elif 'royal society' in string or 'costa rica' in string or 'internation' in string or 'minnesota' in string or 'harvard' in string:
        return 'extranjero'
    elif 'cambridge' in string or 'california' in string or 'belgian' in string or 'milan' in string or 'canada' in string:
        return 'extranjero'
    elif 'recherche' in string or 'venezuela' in string or 'bolivar' in string or 'buenos aires' in string or 'tokyo' in string:
        return 'extranjero'
    elif 'fundação' in string or 'shanghai' in string or 'sydney' in string or 'norwe' in string or 'fundacao' in string:
        return 'extranjero'

    ##No categorizados
    else:
        return 'noinf'


def filtrar_normalizacion_funding_wos( lista ):
    anid = 'no'
    inach= 'no'
    extranjero = 'no'
    corfo = 'no'
    otro = 'no'
    uni = 'no'
    if 'anid' in lista: anid='si'
    if 'inach' in lista: inach='si'
    if 'extranjero' in lista: extranjero='si'
    if 'corfo' in lista: corfo='si'
    if 'otro' in lista: otro='si'
    if 'universidad' in lista: uni='si'
    return [anid, inach, extranjero, corfo, otro, uni]

##La idea es tomar las diferentes journal y agruparlas bajo una casa de publicacion
def normalizar_casa_publicacion( string ):
    string = string.lower().strip()
    if 'elsevier' in string:
        return 'elsevier'
    elif 'wiley' in string:
        return 'wiley'
    elif 'nature' in string:
        return 'nature'
    elif 'mdpi' in string:
        return 'mdpi'
    elif 'springer' in string:
        return 'springer'
    elif 'taylor' in string and 'francis' in string:
        return 't&f'
    elif 'ieee' in string:
        return 'ieee'
    elif 'cambridge' in string and 'press' in string:
        return 'cambridge univ press'
    elif 'oxford' in string and 'press' in string:
        return 'cambridge univ press'
    elif 'frontiers' in string:
        return 'frontiers'
    elif 'iop' in string:
        return 'iop'
    elif 'univ' in string:
        return 'universidad'
    elif 'chile' in string:
        return 'soc. chilena'
    return 'otro'

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
    'u. autonoma': 'metropolitana',
    'u. de santiago de chile': 'metropolitana',
    'u. de chile': 'metropolitana',
    'u. del desarrollo': 'metropolitana',
    'u. andres bello': 'metropolitana',
    'u. catolica de chile': 'metropolitana',
    'u. mayor': 'metropolitana',
    'u. metropolitana': 'metropolitana',
    'u. santo tomas': 'metropolitana',
    'u. adolfo ibañez': 'metropolitana',
    'u. arturo prat': 'metropolitana',
    'u. san sebastian': 'metropolitana',
    'inst. milenio base': 'metropolitana',
    'u. de las americas': 'metropolitana',
    'inst. de ecologia y biodiversidad': 'metropolitana',
    'inst. de nutricion y tecnologia de los alimentos': 'metropolitana',
    'museo natural de historia natural': 'metropolitana',
    'min. de obras publicas': 'metropolitana',
    'meteochile': 'metropolitana',
    'u. bernardo ohiggins': 'metropolitana',
    'universidad de las americas': 'metropolitana',
    'comision chilena de energia nuclear': 'metropolitana',
    #valparaiso
    'u. de valparaiso': 'valparaiso',
    'u. catolica de valparaiso': 'valparaiso',
    'u. de viña del mar': 'valparaiso',
    'u. de playa ancha': 'valparaiso',
    'u. tecnica federico santa maria': 'valparaiso',
    #magallanes
    'u. de magallanes': 'magallanes',
    'inst. antartico chileno': 'magallanes',
    'centro internacional cabo de hornos': 'magallanes',
    'fundacion cequa': 'magallanes',
    #antofagasta
    'u. de antofagasta': 'antofagasta',
    'u. catolica del norte': 'antofagasta',
    #atacama
    'u. de atacama': 'atacama',
    #coquimbo
    'centro de estudios avanzados en zonas aridas': 'coquimbo',
    #bio bio
    'u. del bio bio': 'bio bio',
    'u. de concepcion': 'bio bio',
    'u. catolica de la santisima concepcion': 'bio bio',
    #maule
    'u. de talca': 'maule',
    'u. catolica del maule': 'maule',
    #araucania
    'u. de la frontera': 'araucania',
    'u. catolica de temuco': 'araucania',
    #los lagos
    'u. de los lagos': 'los lagos',
    #los rios
    'u. austral de chile': 'los rios',
    'centro de estudios cientificos de valdivia': 'los rios',
    #aysen
    'centro de investigacion en ecosistemas de la patagonia': 'aysen',
    #ohiggins
    'u. de ohiggins': 'ohiggins'
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