# ask user for type of ball
# check that ball type is in dictionary
# print ball type and its rating


# Not Blank Function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit():
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


keep_going = ""
while keep_going == "":

    # main routine goes here

    # ball list
    soccer = ["soccer ball", "soccer-ball", "football", "foot-ball", "foot ball"]
    rugby = ["rugby ball", "rugby-ball"]
    baseball = ["baseball", "base ball", "base-ball"]
    basketball = ["basketball", "basket ball", "basket-ball"]
    volleyball = ["volleyball", "volley ball", "volley-ball"]
    bowling = ["bowling ball", "bowling-ball"]
    hockey = ["hockey puck", "hockey-ball"]
    ice_hockey = ["ice hockey ball", "ice-hockey-ball", "ice hockey-ball", "ice-hockey ball"]
    golf = ["golf ball", "golf-ball"]
    lacrosse = ["lacrosse ball", "lacrosse-ball"]
    netball = ["netball", "net ball", "net-ball"]
    softball = ["softball", "soft ball", "soft-ball"]
    tennis = ["tennis ball", "tennis-ball"]
    table_tennis = ["table tennis ball", "table-tennis-ball", "table tennis-ball", "table-tennis ball"]
    ping_pong = ["ping pong", "ping-pong"]

    ball_to_check = not_blank("What is your preferred ball type? ",
                              "Your answer may not be blank oor contain numbers",
                              "no")

    # reviews
    if ball_to_check.lower() in soccer:
        print("5/5, if you enjoy playing soccer you are a hugggggge alpha")
    elif ball_to_check.lower() in rugby:
        print("4/5, if you enjoy rugby your cool but the ball you play with has a tumor")
    elif ball_to_check.lower() in baseball:
        print("2/5, if you enjoy this sport chances are you enjoyed t-ball as a child")
    elif ball_to_check.lower() in basketball:
        print("4/5, if you enjoy this sport chances are you're very tall and will be drafted into the NBA")
    elif ball_to_check.lower() in volleyball:
        print("3/5, if you enjoy volleyball you know sport is about having fun")
    elif ball_to_check.lower() in bowling:
        print("3/5, if you bowl, chances are you only play because you're out of shape ;)")
    elif ball_to_check.lower() in hockey:
        print("2/5, you're bad at soccer so you turned to soccer with sticks and a deformed ball")
    elif ball_to_check.lower() in ice_hockey:
        print("3/5, you most probably grew up in Canada, "
              "chances are you're great at ice-hockey because it's the only sport you know")
    elif ball_to_check.lower() in golf:
        print("0/5, you're the worst at every sport, so you play a game and call it a sport")
    elif ball_to_check.lower() in lacrosse:
        print("1/5, this is aa very strange sport and i'm not sure your life has purpose")
    elif ball_to_check.lower() in netball:
        print("1/5, chances are you only play netball because you did not make the basketball team")
    elif ball_to_check.lower() in softball:
        print("2/5, if you enjoy this sport chances are you enjoyed t-ball as a child")
    elif ball_to_check.lower() in tennis:
        print("3/5, you're probably in quite a good physical condition" 
              "but not every gives you the respect you deserve for playing this sport")
    elif ball_to_check.lower() in table_tennis:
        print("1/5, this is a very strange sport but your insanely skilled and don't get enough respect")
    elif ball_to_check.lower() in ping_pong:
        print("1/5, this is a very strange sport but your insanely skilled and don't get enough respect")
