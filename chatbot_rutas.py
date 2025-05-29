import numpy as np
import numpy as np
import pandas as pd
import os
from collections import defaultdict
# Lista completa de estaciones sin acentos y con nombres consistentes
estaciones = [
    'Acatitla', 'Agricola Oriental', 'Allende', 'Apatlaco', 'Aragon', 'Aculco','Aquiles Serdan','Atlalilco',
    'Auditorio', 'Autobuses del Norte', 'Azcapotzalco', 'Balbuena', 'Balderas', 'Barranca del Muerto',
    'Bellas Artes', 'Bondojito', 'Bosques de Aragon', 'Boulevard Puerto Aereo',
    'Buenavista', 'Calle 11', 'Camarones', 'Canal de San Juan', 'Canal del Norte',
    'Candelaria', 'Centro Medico', 'Cerro de la Estrella', 'Chabacano','Chapultepec',
    'Chilpancingo', 'Ciudad Deportiva', 'Ciudad Azteca', 'Colegio Militar',
    'Consulado', 'Constitucion de 1917', 'Constituyentes', 'Copilco',
    'Coyoacan', 'Coyuya', 'Cuatro Caminos', 'Cuauhtemoc', 'Culhuacan','Cuitlahuac',
    'Deportivo 18 de Marzo', 'Deportivo Oceanía', 'Division del Norte',
    'Doctores', 'Ecatepec', 'Eduardo Molina', 'Eje Central', 'Ermita',
    'Escuadron 201', 'Etiopia/Plaza de la Transparencia', 'Eugenia',
    'Ferreria', 'Fray Servando', 'Garibaldi', 'General Anaya', 'Gomez Farias',
    'Guelatao', 'Guerrero', 'Hangares', 'Hidalgo', 'Hospital 20 de Noviembre',
    'Hospital General', 'Impulsora', 'Indios Verdes', 'Insurgentes',
    'Insurgentes Sur', 'Instituto del Petroleo', 'Isabel la Catolica',
    'Iztacalco', 'Iztapalapa', 'Jamaica', 'Juanacatlan', 'Juarez', 'La Paz',
    'La Raza', 'La Viga', 'La Villa - Basilica', 'Lagunilla', 'Lazaro Cardenas',
    'Lindavista', 'Lomas Estrella', 'Los Reyes', 'Martin Carrera', 'Merced',
    'Mexicaltzingo', 'Miguel Angel de Quevedo','Misterios', 'Mixcoac', 'Mixiuhca',
    'Moctezuma', 'Morelos', 'Muzquiz', 'Nativitas', 'Nezahualcoyotl',
    'Niños Heroes', 'Nopalera', 'Norte 45', 'Normal', 'Observatorio',
    'Oceanía', 'Obrera', 'Olimpica', 'Olivos', 'Pantitlan', 'Panteones',
    'Parque de los Venados', 'Patriotismo', 'Peñon Viejo', 'Periferico Oriente',
    'Pino Suarez', 'Plaza Aragon', 'Polanco', 'Politecnico', 'Popotla',
    'Portales', 'Potrero', 'Puebla', 'Refineria', 'Revolucion',
    'Ricardo Flores Magon', 'Rio de los Remedios', 'Romero Rubio', 'Rosario',
    'Salto del Agua', 'San Andres Tomatlan', 'San Antonio', 'San Antonio Abad',
    'San Cosme', 'San Joaquin', 'San Juan de Letran', 'San Lazaro',
    'San Pedro de los Pinos', 'Santa Anita', 'Santa Marta', 'Sevilla',
    'Tacuba', 'Tacubaya', 'Talisman', 'Tasquena', 'Tepalcates', 'Tepito','Terminal Aerea',
    'Tezonco', 'Tezozomoc', 'Tlatelolco', 'Tlaltenco', 'Tlahuac', 'UAM I',
    'Universidad', 'Valle Gomez', 'Vallejo', 'Velodromo', 'Viaducto',
    'Villa de Aragon', 'Villa de Cortes', 'Viveros/Derechos Humanos',
    'Xola', 'Zapata', 'Zapotitlan', 'Zaragoza', 'Zocalo'
]

# Crear matriz de adyacencia R inicializada con ceros
n = len(estaciones)
R = np.zeros((n, n), dtype=int)

# Función para obtener índice de estación (case-sensitive)
def idx(estacion):
    try:
        return estaciones.index(estacion)
    except ValueError:
        print(f"Error: Estación '{estacion}' no encontrada")
        raise

# Conexiones de la Línea 1
linea1 = [
    'Pantitlan', 'Zaragoza', 'Gomez Farias', 'Boulevard Puerto Aereo', 'Balbuena',
    'Moctezuma', 'San Lazaro', 'Candelaria', 'Merced', 'Pino Suarez',
    'Isabel la Catolica', 'Salto del Agua', 'Balderas', 'Cuauhtemoc',
    'Insurgentes', 'Sevilla', 'Chapultepec', 'Juanacatlan', 'Tacubaya', 'Observatorio'
]
for i in range(len(linea1)-1):
    R[idx(linea1[i]), idx(linea1[i+1])] = 1
    R[idx(linea1[i+1]), idx(linea1[i])] = 1

# Conexiones de la Línea 2
linea2 = [
    'Cuatro Caminos', 'Panteones', 'Tacuba', 'Cuitlahuac', 'Popotla',
    'Colegio Militar', 'Normal', 'San Cosme', 'Revolucion', 'Hidalgo',
    'Bellas Artes', 'Allende', 'Zocalo', 'Pino Suarez', 'San Antonio Abad',
    'Chabacano', 'Viaducto', 'Xola', 'Villa de Cortes', 'Nativitas',
    'Portales', 'Ermita', 'General Anaya', 'Tasquena'
]
for i in range(len(linea2)-1):
    R[idx(linea2[i]), idx(linea2[i+1])] = 1
    R[idx(linea2[i+1]), idx(linea2[i])] = 1

# Conexiones de la Línea 3
linea3 = [
    'Indios Verdes', 'Deportivo 18 de Marzo', 'Potrero', 'La Raza', 'Tlatelolco',
    'Guerrero', 'Hidalgo', 'Juarez', 'Balderas', 'Niños Heroes',
    'Hospital General', 'Centro Medico', 'Etiopia/Plaza de la Transparencia',
    'Eugenia', 'Division del Norte', 'Zapata', 'Coyoacan',
    'Viveros/Derechos Humanos', 'Miguel Angel de Quevedo', 'Copilco', 'Universidad'
]
for i in range(len(linea3)-1):
    R[idx(linea3[i]), idx(linea3[i+1])] = 1
    R[idx(linea3[i+1]), idx(linea3[i])] = 1

# Conexiones de la Línea 4
linea4 = [
    'Santa Anita', 'Jamaica', 'Fray Servando', 'Candelaria', 'Morelos',
    'Canal del Norte', 'Consulado', 'Bondojito', 'Talisman', 'Martin Carrera'
]
for i in range(len(linea4)-1):
    R[idx(linea4[i]), idx(linea4[i+1])] = 1
    R[idx(linea4[i+1]), idx(linea4[i])] = 1

# Conexiones de la Línea 5
linea5 = [
    'Politecnico', 'Instituto del Petroleo', 'Autobuses del Norte', 'La Raza',
    'Misterios', 'Valle Gomez', 'Consulado', 'Eduardo Molina', 'Aragon',
    'Oceanía', 'Terminal Aerea', 'Hangares', 'Pantitlan'
]
for i in range(len(linea5)-1):
    R[idx(linea5[i]), idx(linea5[i+1])] = 1
    R[idx(linea5[i+1]), idx(linea5[i])] = 1

# Conexiones de la Línea 6
linea6 = [
    'Rosario', 'Tezozomoc', 'Azcapotzalco', 'Ferreria', 'Norte 45',
    'Vallejo', 'Instituto del Petroleo', 'Lindavista', 'Deportivo 18 de Marzo',
    'La Villa - Basilica', 'Martin Carrera'
]
for i in range(len(linea6)-1):
    R[idx(linea6[i]), idx(linea6[i+1])] = 1
    R[idx(linea6[i+1]), idx(linea6[i])] = 1

# Conexiones de la Línea 7
linea7 = [
    'Rosario', 'Aquiles Serdan', 'Camarones', 'Refineria', 'Tacuba',
    'San Joaquin', 'Polanco', 'Auditorio', 'Constituyentes', 'Tacubaya',
    'San Pedro de los Pinos', 'San Antonio', 'Mixcoac', 'Barranca del Muerto'
]
for i in range(len(linea7)-1):
    R[idx(linea7[i]), idx(linea7[i+1])] = 1
    R[idx(linea7[i+1]), idx(linea7[i])] = 1

# Conexiones de la Línea 8
linea8 = [
    'Garibaldi', 'Bellas Artes', 'San Juan de Letran', 'Salto del Agua',
    'Doctores', 'Obrera', 'Chabacano', 'La Viga', 'Santa Anita', 'Coyuya',
    'Iztacalco', 'Apatlaco', 'Aculco', 'Escuadron 201', 'Atlalilco',
    'Iztapalapa', 'Cerro de la Estrella', 'UAM I', 'Constitucion de 1917'
]
for i in range(len(linea8)-1):
    R[idx(linea8[i]), idx(linea8[i+1])] = 1
    R[idx(linea8[i+1]), idx(linea8[i])] = 1

# Conexiones de la Línea 9
linea9 = [
    'Pantitlan', 'Puebla', 'Ciudad Deportiva', 'Velodromo', 'Mixiuhca',
    'Jamaica', 'Chabacano', 'Lazaro Cardenas', 'Centro Medico',
    'Chilpancingo', 'Patriotismo', 'Tacubaya'
]
for i in range(len(linea9)-1):
    R[idx(linea9[i]), idx(linea9[i+1])] = 1
    R[idx(linea9[i+1]), idx(linea9[i])] = 1

# Conexiones de la Línea A
lineaA = [
    'Pantitlan', 'Agricola Oriental', 'Canal de San Juan', 'Tepalcates',
    'Guelatao', 'Peñon Viejo', 'Acatitla', 'Santa Marta', 'Los Reyes', 'La Paz'
]
for i in range(len(lineaA)-1):
    R[idx(lineaA[i]), idx(lineaA[i+1])] = 1
    R[idx(lineaA[i+1]), idx(lineaA[i])] = 1

# Conexiones de la Línea B
lineaB = [
    'Ciudad Azteca', 'Plaza Aragon', 'Olimpica', 'Ecatepec', 'Muzquiz',
    'Rio de los Remedios', 'Impulsora', 'Nezahualcoyotl', 'Villa de Aragon',
    'Bosques de Aragon', 'Deportivo Oceanía', 'Oceanía', 'Romero Rubio',
    'Ricardo Flores Magon', 'San Lazaro', 'Morelos', 'Tepito', 'Lagunilla',
    'Garibaldi', 'Guerrero', 'Buenavista'
]
for i in range(len(lineaB)-1):
    R[idx(lineaB[i]), idx(lineaB[i+1])] = 1
    R[idx(lineaB[i+1]), idx(lineaB[i])] = 1

# Conexiones de la Línea 12
linea12 = [
    'Tlahuac', 'Tlaltenco', 'Zapotitlan', 'Nopalera', 'Olivos', 'Tezonco',
    'Periferico Oriente', 'Calle 11', 'Lomas Estrella', 'San Andres Tomatlan',
    'Culhuacan', 'Atlalilco', 'Mexicaltzingo', 'Ermita', 'Eje Central',
    'Parque de los Venados', 'Zapata', 'Hospital 20 de Noviembre',
    'Insurgentes Sur', 'Mixcoac'
]
for i in range(len(linea12)-1):
    R[idx(linea12[i]), idx(linea12[i+1])] = 1
    R[idx(linea12[i+1]), idx(linea12[i])] = 1

# Conexiones entre líneas (transbordos)
transbordos = [
    ('Pantitlan', 'Pantitlan'), ('Pino Suarez', 'Pino Suarez'),
    ('Tacubaya', 'Tacubaya'), ('Hidalgo', 'Hidalgo'),
    ('Balderas', 'Balderas'), ('Salto del Agua', 'Salto del Agua'),
    ('Chabacano', 'Chabacano'), ('La Raza', 'La Raza'),
    ('Consulado', 'Consulado'), ('Candelaria', 'Candelaria'),
    ('Morelos', 'Morelos'), ('Oceanía', 'Oceanía'),
    ('San Lazaro', 'San Lazaro'), ('Guerrero', 'Guerrero'),
    ('Bellas Artes', 'Bellas Artes'), ('Zocalo', 'Zocalo'),
    ('Martin Carrera', 'Martin Carrera'), ('Tacuba', 'Tacuba'),
    ('Deportivo 18 de Marzo', 'Deportivo 18 de Marzo'),
    ('Centro Medico', 'Centro Medico'), ('Zapata', 'Zapata'),
    ('Mixcoac', 'Mixcoac'), ('Instituto del Petroleo', 'Instituto del Petroleo'),
    ('Rosario', 'Rosario'), ('Garibaldi', 'Garibaldi'),
    ('Jamaica', 'Jamaica'), ('Santa Anita', 'Santa Anita'),
    ('Atlalilco', 'Atlalilco'), ('Ermita', 'Ermita')
]

for est1, est2 in transbordos:
    R[idx(est1), idx(est2)] = 1
    R[idx(est2), idx(est1)] = 1

# La matriz R ahora contiene todas las conexiones del Metro de la CDMX
print(R)

distancias = {
    # Línea 1
    ('Pantitlan', 'Zaragoza'): 1320, ('Zaragoza', 'Gomez Farias'): 762,
    ('Gomez Farias', 'Boulevard Puerto Aereo'): 611, ('Boulevard Puerto Aereo', 'Balbuena'): 595,
    ('Balbuena', 'Moctezuma'): 703, ('Moctezuma', 'San Lazaro'): 478,
    ('San Lazaro', 'Candelaria'): 866, ('Candelaria', 'Merced'): 698,
    ('Merced', 'Pino Suarez'): 745, ('Pino Suarez', 'Isabel la Catolica'): 382,
    ('Isabel la Catolica', 'Salto del Agua'): 445, ('Salto del Agua', 'Balderas'): 458,
    ('Balderas', 'Cuauhtemoc'): 409, ('Cuauhtemoc', 'Insurgentes'): 793,
    ('Insurgentes', 'Sevilla'): 645, ('Sevilla', 'Chapultepec'): 501,
    ('Chapultepec', 'Juanacatlan'): 973, ('Juanacatlan', 'Tacubaya'): 1158,
    ('Tacubaya', 'Observatorio'): 1262,

    # Línea 2
    ('Cuatro Caminos', 'Panteones'): 1639, ('Panteones', 'Tacuba'): 1416,
    ('Tacuba', 'Cuitlahuac'): 637, ('Cuitlahuac', 'Popotla'): 620,
    ('Popotla', 'Colegio Militar'): 462, ('Colegio Militar', 'Normal'): 516,
    ('Normal', 'San Cosme'): 657, ('San Cosme', 'Revolucion'): 537,
    ('Revolucion', 'Hidalgo'): 587, ('Hidalgo', 'Bellas Artes'): 447,
    ('Bellas Artes', 'Allende'): 387, ('Allende', 'Zocalo'): 602,
    ('Zocalo', 'Pino Suarez'): 745, ('Pino Suarez', 'San Antonio Abad'): 817,
    ('San Antonio Abad', 'Chabacano'): 642, ('Chabacano', 'Viaducto'): 774,
    ('Viaducto', 'Xola'): 490, ('Xola', 'Villa de Cortes'): 698,
    ('Villa de Cortes', 'Nativitas'): 750, ('Nativitas', 'Portales'): 924,
    ('Portales', 'Ermita'): 748, ('Ermita', 'General Anaya'): 838,
    ('General Anaya', 'Tasquena'): 1330,

    # Línea 3
    ('Indios Verdes', 'Deportivo 18 de Marzo'): 1166, ('Deportivo 18 de Marzo', 'Potrero'): 966,
    ('Potrero', 'La Raza'): 1106, ('La Raza', 'Tlatelolco'): 1445,
    ('Tlatelolco', 'Guerrero'): 1042, ('Guerrero', 'Hidalgo'): 702,
    ('Hidalgo', 'Juarez'): 251, ('Juarez', 'Balderas'): 659,
    ('Balderas', 'Niños Heroes'): 665, ('Niños Heroes', 'Hospital General'): 559,
    ('Hospital General', 'Centro Medico'): 653, ('Centro Medico', 'Etiopia/Plaza de la Transparencia'): 1119,
    ('Etiopia/Plaza de la Transparencia', 'Eugenia'): 950, ('Eugenia', 'Division del Norte'): 715,
    ('Division del Norte', 'Zapata'): 794, ('Zapata', 'Coyoacan'): 1153,
    ('Coyoacan', 'Viveros/Derechos Humanos'): 908, ('Viveros/Derechos Humanos', 'Miguel Angel de Quevedo'): 824,
    ('Miguel Angel de Quevedo', 'Copilco'): 1295, ('Copilco', 'Universidad'): 1306,

    # Línea 4
    ('Santa Anita', 'Jamaica'): 758, ('Jamaica', 'Fray Servando'): 1033,
    ('Fray Servando', 'Candelaria'): 633, ('Candelaria', 'Morelos'): 1062,
    ('Morelos', 'Canal del Norte'): 910, ('Canal del Norte', 'Consulado'): 884,
    ('Consulado', 'Bondojito'): 645, ('Bondojito', 'Talisman'): 959,
    ('Talisman', 'Martin Carrera'): 1129,

    # Línea 5
    ('Politecnico', 'Instituto del Petroleo'): 1188, ('Instituto del Petroleo', 'Autobuses del Norte'): 1067,
    ('Autobuses del Norte', 'La Raza'): 975, ('La Raza', 'Misterios'): 892,
    ('Misterios', 'Valle Gomez'): 969, ('Valle Gomez', 'Consulado'): 679,
    ('Consulado', 'Eduardo Molina'): 815, ('Eduardo Molina', 'Aragon'): 860,
    ('Aragon', 'Oceanía'): 1219, ('Oceanía', 'Terminal Aerea'): 1174,
    ('Terminal Aerea', 'Hangares'): 1153, ('Hangares', 'Pantitlan'): 1644,

    # Línea 6
    ('Rosario', 'Tezozomoc'): 1257, ('Tezozomoc', 'Azcapotzalco'): 973,
    ('Azcapotzalco', 'Ferreria'): 1173, ('Ferreria', 'Norte 45'): 1072,
    ('Norte 45', 'Vallejo'): 660, ('Vallejo', 'Instituto del Petroleo'): 755,
    ('Instituto del Petroleo', 'Lindavista'): 1258, ('Lindavista', 'Deportivo 18 de Marzo'): 1075,
    ('Deportivo 18 de Marzo', 'La Villa - Basilica'): 570, ('La Villa - Basilica', 'Martin Carrera'): 1141,

    # Línea 7
    ('Rosario', 'Aquiles Serdan'): 1615, ('Aquiles Serdan', 'Camarones'): 1402,
    ('Camarones', 'Refineria'): 952, ('Refineria', 'Tacuba'): 1295,
    ('Tacuba', 'San Joaquin'): 1433, ('San Joaquin', 'Polanco'): 1163,
    ('Polanco', 'Auditorio'): 812, ('Auditorio', 'Constituyentes'): 1430,
    ('Constituyentes', 'Tacubaya'): 1005, ('Tacubaya', 'San Pedro de los Pinos'): 1084,
    ('San Pedro de los Pinos', 'San Antonio'): 606, ('San Antonio', 'Mixcoac'): 788,
    ('Mixcoac', 'Barranca del Muerto'): 1476,

    # Línea 8
    ('Garibaldi', 'Bellas Artes'): 634, ('Bellas Artes', 'San Juan de Letran'): 456,
    ('San Juan de Letran', 'Salto del Agua'): 292, ('Salto del Agua', 'Doctores'): 564,
    ('Doctores', 'Obrera'): 761, ('Obrera', 'Chabacano'): 1143,
    ('Chabacano', 'La Viga'): 843, ('La Viga', 'Santa Anita'): 633,
    ('Santa Anita', 'Coyuya'): 968, ('Coyuya', 'Iztacalco'): 993,
    ('Iztacalco', 'Apatlaco'): 910, ('Apatlaco', 'Aculco'): 534,
    ('Aculco', 'Escuadron 201'): 789, ('Escuadron 201', 'Atlalilco'): 1738,
    ('Atlalilco', 'Iztapalapa'): 732, ('Iztapalapa', 'Cerro de la Estrella'): 717,
    ('Cerro de la Estrella', 'UAM I'): 1135, ('UAM I', 'Constitucion de 1917'): 1137,

    # Línea 9
    ('Pantitlan', 'Puebla'): 1380, ('Puebla', 'Ciudad Deportiva'): 800,
    ('Ciudad Deportiva', 'Velodromo'): 1110, ('Velodromo', 'Mixiuhca'): 821,
    ('Mixiuhca', 'Jamaica'): 942, ('Jamaica', 'Chabacano'): 1031,
    ('Chabacano', 'Lazaro Cardenas'): 1000, ('Lazaro Cardenas', 'Centro Medico'): 1059,
    ('Centro Medico', 'Chilpancingo'): 1152, ('Chilpancingo', 'Patriotismo'): 955,
    ('Patriotismo', 'Tacubaya'): 1133,

    # Línea A
    ('Pantitlan', 'Agricola Oriental'): 1409, ('Agricola Oriental', 'Canal de San Juan'): 1093,
    ('Canal de San Juan', 'Tepalcates'): 1456, ('Tepalcates', 'Guelatao'): 1161,
    ('Guelatao', 'Peñon Viejo'): 2206, ('Peñon Viejo', 'Acatitla'): 1379,
    ('Acatitla', 'Santa Marta'): 1100, ('Santa Marta', 'Los Reyes'): 1783,
    ('Los Reyes', 'La Paz'): 1956,

    # Línea B
    ('Ciudad Azteca', 'Plaza Aragon'): 574, ('Plaza Aragon', 'Olimpica'): 709,
    ('Olimpica', 'Ecatepec'): 596, ('Ecatepec', 'Muzquiz'): 1485,
    ('Muzquiz', 'Rio de los Remedios'): 1155, ('Rio de los Remedios', 'Impulsora'): 436,
    ('Impulsora', 'Nezahualcoyotl'): 1393, ('Nezahualcoyotl', 'Villa de Aragon'): 1335,
    ('Villa de Aragon', 'Bosques de Aragon'): 784, ('Bosques de Aragon', 'Deportivo Oceanía'): 1165,
    ('Deportivo Oceanía', 'Oceanía'): 863, ('Oceanía', 'Romero Rubio'): 809,
    ('Romero Rubio', 'Ricardo Flores Magon'): 908, ('Ricardo Flores Magon', 'San Lazaro'): 907,
    ('San Lazaro', 'Morelos'): 1296, ('Morelos', 'Tepito'): 498,
    ('Tepito', 'Lagunilla'): 611, ('Lagunilla', 'Garibaldi'): 474,
    ('Garibaldi', 'Guerrero'): 757, ('Guerrero', 'Buenavista'): 521,

    # Línea 12
    ('Tlahuac', 'Tlaltenco'): 1298, ('Tlaltenco', 'Zapotitlan'): 1115,
    ('Zapotitlan', 'Nopalera'): 1276, ('Nopalera', 'Olivos'): 1360,
    ('Olivos', 'Tezonco'): 490, ('Tezonco', 'Periferico Oriente'): 1545,
    ('Periferico Oriente', 'Calle 11'): 1111, ('Calle 11', 'Lomas Estrella'): 906,
    ('Lomas Estrella', 'San Andres Tomatlan'): 1060, ('San Andres Tomatlan', 'Culhuacan'): 990,
    ('Culhuacan', 'Atlalilco'): 1671, ('Atlalilco', 'Mexicaltzingo'): 1922,
    ('Mexicaltzingo', 'Ermita'): 1805, ('Ermita', 'Eje Central'): 895,
    ('Eje Central', 'Parque de los Venados'): 1280, ('Parque de los Venados', 'Zapata'): 563,
    ('Zapata', 'Hospital 20 de Noviembre'): 450, ('Hospital 20 de Noviembre', 'Insurgentes Sur'): 725,
    ('Insurgentes Sur', 'Mixcoac'): 651
}

# Hacer conexiones bidireccionales automáticamente
distancias.update({(est2, est1): dist for (est1, est2), dist in distancias.items()})

# ======================
# 2. CONSTRUIR MATRIZ DE ADYACENCIA CON DISTANCIAS
# ======================

n = len(estaciones)
matriz_distancias = np.full((n, n), np.inf)  # Inicializar con infinito

# Llenar la matriz con distancias reales
for (est1, est2), distancia in distancias.items():
    i, j = estaciones.index(est1), estaciones.index(est2)
    matriz_distancias[i, j] = distancia
    matriz_distancias[j, i] = distancia  # Conexión bidireccional

# Estaciones no conectadas permanecen con np.inf

# ======================
# 3. MATRIZ DE TRANSICIÓN BASADA EN DISTANCIAS
# ======================

def crear_matriz_transicion(matriz_distancias):
    # Invertir distancias (mayor peso = menor distancia)
    inverso_distancias = np.divide(1, matriz_distancias, where=matriz_distancias!=0)
    np.fill_diagonal(inverso_distancias, 0)  # No permitir autoconexiones

    # Normalizar por filas para obtener probabilidades
    suma_filas = inverso_distancias.sum(axis=1, keepdims=True)
    matriz_transicion = np.divide(inverso_distancias, suma_filas, where=suma_filas!=0)

    return np.nan_to_num(matriz_transicion)

matriz_transicion = crear_matriz_transicion(matriz_distancias)

# ======================
# 4. SIMULACIÓN DE TRAYECTORIAS CON PROBABILIDADES POR DISTANCIA
# ======================

def ruta_markov_distancia(origen, destino, matriz_transicion, estaciones, n_simulaciones=1000000):
    idx_origen = estaciones.index(origen)
    idx_destino = estaciones.index(destino)
    rutas = []

    for _ in range(n_simulaciones):
        estado_actual = idx_origen
        ruta = [estaciones[estado_actual]]
        visitados = set(ruta)

        while estado_actual != idx_destino:
            try:
                # Elegir próxima estación basada en probabilidades
                proximo_estado = np.random.choice(
                    len(estaciones),
                    p=matriz_transicion[estado_actual]
                )

                # Evitar ciclos
                if estaciones[proximo_estado] in visitados:
                    break

                ruta.append(estaciones[proximo_estado])
                visitados.add(estaciones[proximo_estado])
                estado_actual = proximo_estado
            except:
                break

        if estado_actual == idx_destino:
            # Calcular distancia total de la ruta
            distancia_total = sum(
                matriz_distancias[estaciones.index(ruta[i]), estaciones.index(ruta[i+1])]
                for i in range(len(ruta)-1)
            )
            rutas.append((ruta, distancia_total))

    # Devolver la ruta con menor distancia encontrada
    if not rutas:
        return None
    return min(rutas, key=lambda x: x[1])[0]

import numpy as np
import pandas as pd
from collections import defaultdict
import networkx as nx
import streamlit as st
import streamlit as st
from PIL import Image
import base64

# Cargar imagen
logo_path = "metrologo.png"
logo = Image.open(logo_path)

# Codificar imagen en base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def header_html():
    logo_base64 = get_base64_of_bin_file(logo_path)
    html = f"""
    <div style="background-color:#ff5e00;padding:10px 20px;border-radius:8px;display:flex;align-items:center;">
        <img src="data:image/png;base64,{logo_base64}" style="height:60px;margin-right:20px;">
        <h1 style="color:white;font-size:28px;margin:0;">SISTEMA DE TRANSPORTE COLECTIVO METRO</h1>
    </div>
    """
    return html

st.markdown(header_html(), unsafe_allow_html=True)



# (Aquí va todo el código anterior que define las estaciones, matriz R, distancias, etc.)

def crear_interfaz():
    st.title("🚇 Planificador de Rutas - Metro CDMX")
    st.subheader("Selecciona estaciones de origen y destino")

    origen = st.selectbox("Estación de origen:", estaciones)
    destino = st.selectbox("Estación de destino:", estaciones)

    if origen and destino and origen != destino:
        if st.button("Calcular Ruta"):
            st.write(f"Calculando rutas desde **{origen}** hasta **{destino}**...")

            # Calcular ruta con Markov
            ruta_markov = ruta_markov_distancia(origen, destino, matriz_transicion, estaciones, n_simulaciones=10000)

            # Calcular ruta óptima con Dijkstra
            ruta_dijk, dist_dijk = ruta_dijkstra(origen, destino, matriz_distancias, estaciones)

            st.markdown("## Resultados")

            if ruta_markov:
                dist_markov = sum(
                    matriz_distancias[estaciones.index(ruta_markov[i]), estaciones.index(ruta_markov[i+1])]
                    for i in range(len(ruta_markov)-1)
                )
                st.markdown("### 📍 Ruta Markov (Probabilística)")
                st.write(" → ".join(ruta_markov))
                st.write(f"Distancia total: {dist_markov:.0f} metros")
                st.write(f"Número de estaciones: {len(ruta_markov)}")
            else:
                st.error("❌ No se encontró una ruta con el método probabilístico.")

            if ruta_dijk:
                st.markdown("### ⚡ Ruta Óptima (Dijkstra)")
                st.write(" → ".join(ruta_dijk))
                st.write(f"Distancia total: {dist_dijk:.0f} metros")
                st.write(f"Número de estaciones: {len(ruta_dijk)}")

                if ruta_markov:
                    diferencia = dist_markov - dist_dijk
                    if diferencia > 0:
                        st.info(f"ℹ️ La ruta óptima es {diferencia:.0f} metros más corta que la ruta probabilística.")
                    elif diferencia < 0:
                        st.warning("ℹ️ ¡Inusual! La ruta probabilística fue más corta que la óptima.")
                    else:
                        st.success("ℹ️ Ambas rutas tienen la misma distancia.")
            else:
                st.error("❌ No se encontró una ruta óptima con Dijkstra.")

    elif origen == destino:
        st.warning("Selecciona estaciones diferentes para calcular una ruta.")

# Ejecutar la interfaz
def ruta_dijkstra(origen, destino, matriz_distancias, estaciones):
    import heapq
    n = len(estaciones)
    origen_idx = estaciones.index(origen)
    destino_idx = estaciones.index(destino)

    dist = [np.inf] * n
    prev = [None] * n
    dist[origen_idx] = 0
    heap = [(0, origen_idx)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v in range(n):
            if matriz_distancias[u][v] != np.inf:
                alt = dist[u] + matriz_distancias[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(heap, (alt, v))

    # reconstruir la ruta
    if dist[destino_idx] == np.inf:
        return None, np.inf
    path = []
    u = destino_idx
    while u is not None:
        path.insert(0, estaciones[u])
        u = prev[u]
    return path, dist[destino_idx]

crear_interfaz()