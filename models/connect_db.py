import psycopg2, os, logging
from dotenv import load_dotenv

load_dotenv()

def conectar_db():
    # Buscar as variaveis do .env
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    DBNAME = os.getenv("DBNAME")

    # Conectar ao banco de dados
    try:
        conexao_db = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME,
            sslmode="require"
        )
        logging.info("Conexão efeutada com sucesso")

        return conexao_db
    except Exception as e:
        logging.error(e)
        return "Houve um problema na conexão com o banco de dados"

def dict_fetchall(cursor):
    colunas = [desc[0] for desc in cursor.description]
    return [dict(zip(colunas, linha)) for linha in cursor.fetchall()]