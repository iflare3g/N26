from app import app
import socket,os

if __name__ == "__main__":
    try:
        PORT=8080
        app.run(host=os.getenv("IP","0.0.0.0"),port=PORT,threaded=True,debug=True)
    except socket.error as err:
        if err.args[0] == 98:
            print ("Flask is already running or port {} is busy.".format(PORT))
        else:
            pass