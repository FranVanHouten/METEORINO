import timeimport serialimport stringimport pynmea2import MySQLdbimport datetime as fechastarttime = time.time()ser = serial.Serial("/dev/ttyAMA0", 9600,timeout=0)    while 1:    if ser.inWaiting() > 0:        try:            data = ser.readline()            if data[0:6] == "$GPGGA":                try:                    mifecha = fecha.datetime.now()                    conexion = MySQLdb.connect(host="localhost", user="pi", passwd="0000", db="meteorino") or die("Connection error")                    cursor = conexion.cursor()                    msg = pynmea2.parse(data)                    lat = msg.latitude                    print(lat)                    lon = msg.longitude                    print(lon)                    alt = msg.altitude                    print(alt)                finally:                    pass                try:                    with conexion.cursor() as cursor:                        query_gps = "INSERT INTO gps(fecha,longitud,latitud,altitud) VALUES(%s,%s,%s,%s)"                        cursor.execute(query_gps, (mifecha, lon, lat, alt))                        conexion.commit()                finally:                    conexion.close()                    time.sleep(1.0 - ((time.time() - starttime) % 1.0))        except serial.serialutil.SerialException: #excepción por otro error que aparece	    print ("No data")            time.sleep(1.0 - ((time.time() - starttime) % 1.0))