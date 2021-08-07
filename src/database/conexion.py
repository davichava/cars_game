import pymysql


class DataBase:
    def __init__(self) -> None:
        self.__conecction = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='cars_game'
        )

        self.cursor = self.__conecction.cursor(pymysql.cursors.DictCursor)

    def get_all_juegos(self):
        sql = 'SELECT * FROM cars_game.juegos'
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print(data[0]['primero'])
        except Exception as e:
            raise

    def get_ganados(self, nombre):
        sql = f"SELECT * FROM cars_game.jugadores WHERE nombre = '{nombre}'"
        try:
            self.cursor.execute(sql)
            jugador = self.cursor.fetchone()
            if jugador:
                return jugador['ganados']
            else:
                return 0
        except Exception as e:
            raise

    def calcular_nuevo_indicador_juego(self):
        sql = f"SELECT count(*) as numero_juegos FROM cars_game.juegos "
        try:
            self.cursor.execute(sql)
            juegos = self.cursor.fetchone()
            return juegos['numero_juegos'] + 1
        except Exception as e:
            raise

    def save_juego(self, juego):
        primero = juego.get_podio().get_primero()
        segundo = juego.get_podio().get_segundo()
        tercero = juego.get_podio().get_tercero()
        sql = f"INSERT INTO cars_game.juegos(primero, segundo, tercero) VALUES('{primero}', '{segundo}', '{tercero}');"
        try:
            self.cursor.execute(sql)
            self.__conecction.commit()
        except Exception as e:
            raise

    def save_campeon(self, juego):
        campeon = juego.get_podio().get_primero()
        sql = f"INSERT INTO cars_game.jugadores (nombre) VALUES ('{campeon}')"
        try:
            self.cursor.execute(sql)
            self.__conecction.commit()
        except Exception as e:
            raise
        
    
    def get_campeones(self):
        sql = "SELECT nombre, count(*) AS victorias FROM cars_game.jugadores GROUP BY 1 ORDER BY victorias DESC"
        try:
            self.cursor.execute(sql)
            campeones = self.cursor.fetchall()
            return campeones
        except Exception as e:
            raise
