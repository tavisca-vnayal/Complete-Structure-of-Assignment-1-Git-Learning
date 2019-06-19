
def initialize(company,programme):
    print(company,programme)
    
    global companyName 
    global programmeName

    companyName = company
    programmeName = programme


def greeter():
    print("Welcome to " + programmeName + " @ " + companyName)

initialize("Tavisca","Prejoining Training")
greeter()


