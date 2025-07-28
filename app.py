from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_UID = os.getenv("DB_UID")
DB_PWD = os.getenv("DB_PWD")

conn_str = (
    f"DRIVER={{{DB_DRIVER}}};"
    f"SERVER={DB_SERVER};"
    f"DATABASE={DB_DATABASE};"
    f"UID={DB_UID};"
    f"PWD={DB_PWD};"
)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/occupancy', methods=['GET'])
def get_occupancy():
    query = """
        SELECT 
            OP.BayIndex AS id,
            DATEADD(HOUR, 10, EventTimeUtc) AS lastSeen,
            OP.State AS status,
            OP.Active,
            B.Latitude AS lat,
            B.Longitude AS lng,
            B.Suburb,
            B.Name AS name,
            C.Name AS customerName
        FROM [dbo].[Occupancy] OP
        JOIN [dbo].[Bay_info_all] B
          ON OP.BayIndex = B.ExtSpaceId AND OP.TenantId = B.TenantId
        JOIN [dbo].[Customers] C on OP.TenantId = C.Id
        WHERE OP.TenantId = 28
          AND CAST(DATEADD(HOUR, 10, EventTimeUtc) AS DATE) = CAST(DATEADD(HOUR, 10, GETDATE()) AS DATE)
    """

    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

            for row in rows:
                # Assign same default heat intensity (0.6) for now
                # You can later vary based on time since lastSeen or event frequency
                row["heat_intensity"] = 0.6

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
