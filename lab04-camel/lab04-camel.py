class Room:
    def __init__(self, description="", north=None, east=None, south=None, west=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []

    # Define rooms
    room = Room("no ves una puta mierda, hay un pasadizo hacia el norte.", north=1)
    room_list.append(room)

    room = Room("esta echenique en la habitacion. Hay puerta con escalon (no puede subir hacia el este o el sur.", south=0, east=2)
    room_list.append(room)

    room = Room("Estas en un meeting del psoen. puerte en el oeste", west=1)
    room_list.append(room)

    current_room = 0
    done = False

    while not done:
        print("\n" + room_list[current_room].description)

        user_input = input("Que cojones haces? ").strip().lower()

        if user_input in ["n", "norte"]:
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input in ["e", "este"]:
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input in ["s", "sur"]:
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input in ["o", "oeste"]:
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input in ["q", "quit"]:
            print("gracias por jugar")
            done = True

        else:
            print("I don't understand that command.")


if __name__ == "__main__":
    main()
