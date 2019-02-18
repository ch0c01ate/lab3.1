import json

def show_json_object(object):
    print("Keys here:")
    for key in object:
        print(key)


def introduce():
    print("Use cd to get back")
    print("Use key to get value of the key")
    print("Press Enter to stop", end='\n\n\n')


def main():
    introduce()

    ended = False

    with open("response.json", "r") as f:
        response = json.load(f)

    object = response

    history = [response]

    while not ended:
        if type(object) == dict:
            show_json_object(object)
        elif type(object) == list:
            print("Values are:")
            for i in object:
                print(i)

            print("No more keys here, enter cd")

        else:
            print("Here is no values")
            print("No more keys here, enter cd")

        command = input("Enter key or cd to get back\n")

        if(command == ''):
            ended = True

        elif(command == 'cd' and object != response):
            history.pop()
            object = history[-1]

        elif(command in object):
            object = object[command]
            history.append(object)

        else:
            print("Wrong key")


if __name__ == '__main__':
    main()