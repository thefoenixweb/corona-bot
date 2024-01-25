# whatsapp bot to get live status update on corona virus

from pymongo import MongoClient
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from corona1 import get_data


# database connectivity
cluster = MongoClient("mongodb+srv://john:Father@cluster0.b1lrdrw.mongodb.net/?retryWrites=true&w=majority")
db = cluster["covid"]
users = db["users"]

appbot = Flask(__name__)


@appbot.route("/", methods=["get", "post"])
def reply():
    num = request.form.get("From")
    num = num.replace("whatsapp:", "")
    msg_text = request.form.get("Body")
    x = users.find_one({"NUMBER": num})
    try:
        status = x["status"]
    except:
        pass

    if (bool(x) == False):
        users.insert_one({"NUMBER": num, "status": "first"})
        msg = MessagingResponse()
        resp = msg.message(
            "Hello, this is a covid statistics update bot. Enter any country to receive covid infection rate statistics")
        return (str(msg))
    else:
        if (status == "first"):
            data = get_data(msg_text, num)
            msg = MessagingResponse()
            resp = msg.message(data)
            users.delete_one({"NUMBER": num})
            return (str(msg))



if (__name__ == "__main__"):
    appbot.run(port=5000)
