from flask import Flask
import psycopg2
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/health")
def health():
    logger.info("Health check requested")
    return "OK"

@app.route("/")
def home():
  logger.info("Connecting to PostgreSQL")
  try:
    conn = psycopg2.connect(
     host="databases",
     port=5432,
     dbname=os.getenv("POSTGRES_DB"),
     user=os.getenv("POSTGRES_USER"),
     password=os.getenv("POSTGRES_PASSWORD")
    )
  except Exception as e:
    logger.error(f"Database connection failed: {e}")
    return "Database connection failed", 500

  cursor = conn.cursor()
  logger.info("Querying users from PostgreSQL")
  cursor.execute("SELECT id, name FROM users;")
  users = cursor.fetchall()

  cursor.close()
  conn.close()

  return "<br>" .join(f"{user[0]} - {user[1]}" for user in users)

logger.info("Flask application starting")
app.run(host="0.0.0.0", port=5000)
