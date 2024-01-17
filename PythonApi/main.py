import pypyodbc as odbc
from flask import Flask, jsonify, make_response

app = Flask(__name__)

driverName = "SQL SERVER"
serverName = "LAPTOP-UM5BI89M" #SELECT @@SERVERNAME
databaseName = "StackOverflow2013"

connectionString = f"""
    DRIVER={{{driverName}}};
    SERVER={serverName};
    DATABASE={databaseName};
    Trust_Connection=yes;
"""

print(f"Connecting to database using: \n{connectionString}")
conn = odbc.connect(connectionString)
print(conn)


#Kun for morro med mindre dere bytter over til parametization
def runSql(pQuery):
    cursor = conn.cursor()
    cursor.execute(pQuery)
    rows = cursor.fetchall()
    resp = make_response(jsonify(rows))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/")
def home():
    return '''
        <svg width="12" height="12">
            <rect width="12" height="12" style="fill: green;stroke-width: 3;opacity: 1;display: inline;" y="0" x="0" ry="2" rx="2"></rect>
        </svg>
        Gand api is running 
    '''

#http://localhost:5000/getUserByID/26837
@app.route("/getUserByID/<userID>")
def getUserByID(userID):
    sqlQuery = f"SELECT TOP 1 * FROM Users WHERE ID = '{userID}'"
    return runSql(sqlQuery)

@app.route("/getPostByID/<postID>")
def getPostByID(postID):
    sqlQuery = f"SELECT TOP 1 * FROM Posts WHERE ID = '{postID}'"
    return runSql(sqlQuery)


@app.route("/getCommentsByPostID/<postID>")
def getCommentsByPostID(postID):
    sqlQuery = f"SELECT * FROM Comments WHERE PostID = '{postID}' ORDER BY Score DESC"
    return runSql(sqlQuery)


# Utvidelse hent kun det aksepterte svaret på en post 



if __name__ == "__main__":
    app.run()
