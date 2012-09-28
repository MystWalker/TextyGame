class TextGame():
    def __init__(self):
        self.FOCUS = None
        
        #dummy room
        self.dahRoom = Room("Room", "A shity room.")
        self.FOCUS = self.dahRoom

        #dummy Character
        self.char1 = Character("Tool", "He's an asshole, you can tell.")

        self.dahRoom.addChar(self.char1)
        
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
    def getInput(self):
        thing = input("TYPE SOMESHIEIHTDGSHOJS>>")
        return thing

    def display(self, FOCUS):
        FOCUS.menu()
        
    def mainLoop(self):

        while True:
            print(self.FOCUS.lookAt())
            self.display(self.FOCUS)
            move = self.getInput()
            self.FOCUS.interact(move)
            

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
        self.topics = {Topic("Greeting","Hi.",[]), Topic("Goodbye","bye", []), Topic("Unknown","What?", [])}

    def __str__(self):
        string = "Talk to " + self.name
        return string

    def interact(self):
        self.talk()

    def talk(self): ## I copy pasted this method, it's fucked. Redo it.
        print(self.name + ' says, "' + 'Greetz' + '"\n')

        while True:
            found = False
            
            subject = input(self.name + ">>")

            print(subject.lower() + "\n")
            
            if( subject.lower() == "leave"):
                print('"'+ 'Goodbye'.response + '"')
                break
            
            if( subject.lower() == "look"):
                print("You are speaking with " + self.description + "\n")
                found = True

            for key in self.topics:
                if subject.lower() == key.lower():
                    print('"' + "Topic" + '"')
                    found = True
                    break
                if found == False: print("Come again?\n")
        '''
        Greeting
        goodbye
        unknown
        '''
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

class Topic():

    def __init__(self, name, response, topics):
        self.name = name
        self.response = response
        self.topics = topics



if __name__ == '__main__':

    game = TextGame()
    game.mainLoop()