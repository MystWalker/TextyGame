class TextGame():
    def __init__(self):
        self.FOCUS = None
        
        #dummy room
        self.dahRoom = Room("Room", "A shity room.")
        self.FOCUS = self.dahRoom

        #dummy Character
        self.char1 = Character("Tool", "He's an asshole, you can tell.")
        topic1 = Topic("Shoes", "", [])
        topic2 = Topic("Chat", "Hey, what do you think of my [shoes]?", [topic1])
        topic3 = Topic("Shoes", "Oh, THESE old things? I got them Holister", [])
        self.char1.addTopic(topic2)
        self.char1.addTopic(topic3)
        
        self.dahRoom.addChar(self.char1)
        

        #Player
        self.player = Player()

        #Free topics
        self.hate = Topic("Hate", "A terible emotion.", [])
        self.love = Topic("Love", "A mythical emotion.", [])
        
    #Hold player focus
    #get input
    #direct input to focus
    #Current_room

    #Set-up
        #charley is a character
            #Greeting = hello
            #Chat = Seen any [girls]?
            #Girls = I saw one earlyer with the [key]
            #key = Probably opens the exit.
            #Unknown = Sorry, what was that?

        #Player
            #lexicon:
                #chat

    #Main loop
        #Wait for input
        #Parse input to focus
        #Print output from focus
        #loop

    def look(self, player):
        #Look request
        return

    def talk(self, player):
        print(self.FOCUS.name + ' says, "' + self.FOCUS.topics['Greeting'].response + '."\n')

        while True:
            found = False

            print("Type 'leave' to leave conversation, 'list' to list known topics.")            
            subject = input(self.FOCUS.name + ">>")

            print(subject.lower() + "\n\n")

            if( subject.lower() == "leave"):
                print('"'+ self.FOCUS.topics['Goodbye'].response + '."\n')
                break

            if( subject.lower() == "list"):
                player.listTopics()
                found = True
            
            if( subject.lower() == "look"):
                print("You are speaking with " + self.FOCUS.description + "\n")
                found = True

            for key in self.FOCUS.topics:
                if subject.lower() == key.lower():
                    print('"' + self.FOCUS.topics[key].response + '."\n')
                    for topic in self.FOCUS.topics[key].topics:
                        player.learn(topic)
                    found = True
                    break
            if found == False: print('"' + self.FOCUS.topics["Unknown"].response + '"\n')
        

    def use(self, player):
        #Use request
        return
    
    def getInput(self):
        thing = input("--->>")
        return thing

    def display(self, FOCUS):
        FOCUS.menu()
        
    def mainLoop(self):
        print("Texty-Game\nA simpel text game, by Evan Clement\n")
        print("You are in ", end = "")
        while True:
            print(self.FOCUS.lookAt() + "\n")

            print("You are speaking to Tool.")
            
            self.FOCUS = self.char1
            self.talk(self.player)
            
            print("End of game.")
            break
            
            

#class Exit():
    #object that holds link to room
    

class Prop():

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def lookAt(self):
        return self.description

class Room(Prop):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.props = []
        self.characters = []
        self.options = []         
        
    def menu(self):
        num = 1
        for thing in self.options:
            print(str(num) + ". " + str(thing))
            num += 1

    def interact(self, choice):
        print(self.options[int(choice)-1].interact())
        
    def addChar(self, character):
        self.characters.append(character)
        self.options.append(character)

    def addProp(self, prop):
        self.props.append(prop)
    #Characters
    #Items
    #Exits

class Character(Prop):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.topics = {}
        self.topics['Greeting'] = Topic("Greeting","Hi",[])
        self.topics['Goodbye'] = Topic("Goodbye","Bye", [])
        self.topics['Unknown'] = Topic("Unknown","I don't know what you're talking about", [])
        self.topics['Chat'] = Topic("Chat","This is my standard response", [])

    def __str__(self):
        string = "Talk to " + self.name
        return string

    def addTopic(self, topic):
        self.topics[topic.name] = topic

    def interact(self):
        self.talk()

    
    

    #States
    '''
        Interact
        Respond
        '''
    #Dictionarys
    '''
        Topics
        inventory
        '''

class Player():

    def __init__(self):
        self.lexicon = {}
        self.inventory = {}

    #--------- Item methods

    def get(self, item):
        self.inventory[item.name] = item

    def lose(self, item):
        item = item.capitalize() #Forces correct format
        if item in self.invetory:
            del self.inventory[item]

    def listItems(self):
        for key in self.inventory:
            print(self.inventory[key].name)
            
    #Checks if item is in inventory returns true/false
    def inInv(self, item):
        item = item.capitalize()
        for key in self.inventory:
            if item == self.inventory[key].name: return True
        return False

    #--------- Topic methods

    def learn(self, topic):
        self.lexicon[topic.name] = topic

    def forget(self, topic):
        topic = topic.capitalize() #Forces correct format
        if topic in self.lexicon:
            del self.lexicon[topic]

    def listTopics(self):
        print("You've heard of:")
        for key in self.lexicon:
            print(self.lexicon[key].name)

    def inLex(self, topic):
        topic = topic.capitalize()
        for key in self.lexicon:
            if topic == self.lexicon[key].name: return True
        return False

    

class Topic():

    def __init__(self, name, response, topics):
        self.name = name.capitalize() #Forces correct format
        self.response = response
        self.topics = topics

    def __str__(self):
        string = self.name + " " + self.response
        return string



if __name__ == '__main__':

    game = TextGame()
    game.mainLoop()
