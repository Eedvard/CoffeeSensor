import configparser, requests, time

class Bot():

    def __init__(self):

        config = configparser.ConfigParser()
        config.read("settings.ini")
        self.api_token = config.get("secret", "token")

        myInfo = self.getBot()
        self.id = myInfo["result"]["id"]
        self.firstName = myInfo["result"]["first_name"]
        self.userName = myInfo["result"]["username"]

    def getBot(self):

        r = requests.get("https://api.telegram.org/bot"+self.api_token+"/getMe")
        result = r.json()
        return result

    def getUpdates(self, lastSeen):

        params = {'timeout': 100, 'offset': lastSeen}
        r = requests.get("https://api.telegram.org/bot" + self.api_token + "/getUpdates", data=params)
        result = r.json()
        return result

    def sendMessage(self, chatId, message):

        r = requests.post("https://api.telegram.org/bot" + self.api_token + "/sendMessage?chat_id="+str(chatId)+"&text="+message)
        result = r.json()
        return result

    def running(self):

        lastSeen = None
        while True:

            command = self.getUpdates(lastSeen)
            print(len(command))
            print(command)

            lastMessage = command["result"][-1]["message"]
            lastChatId = lastMessage["chat"]["id"]
            lastMessageText = lastMessage["text"]

            if(lastMessageText=="/help"):
                self.sendMessage(lastChatId, "help")
            elif(lastMessageText=="/kahvi"):
                self.sendMessage(lastChatId, "kahvi")

            lastSeen = command["result"][-1]["update_id"] + 1


if __name__ == '__main__':

    bot = Bot()
    bot.running()

