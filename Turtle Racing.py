import turtle
import time
import random

# Constants
WIDTH, HEIGHT = 500, 500  # Screen dimensions
COLORS = ['red', 'green', 'black', 'cyan', 'yellow', 'purple', 'blue', 'pink', 'brown', 'orange']
MIN_RANGE, MAX_RANGE = 1, 20  # Range of movement per step for turtles

def get_number_of_turtles():
    """
    Prompts the user to enter the number of turtles (2-10) for the race.
    Returns:
        int: The number of turtles selected.
    """
    while True:
        turtles = input("Enter the number of Turtles (2-10): ")
        if turtles.isdigit():
            turtles = int(turtles)
            if 2 <= turtles <= 10:
                return turtles
            else:
                print("Number of turtles must be between 2 and 10!")
        else:
            print("Invalid input! Please enter a numeric value.")

def create_turtles(colors):
    """
    Creates and positions the turtles on the screen for the race.

    Args:
        colors (list): List of colors for the turtles.

    Returns:
        list: A list of turtle objects ready for the race.
    """
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)  # Calculate spacing between turtles
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)  # Face the turtles upwards
        racer.penup()
        # Set the starting position for each turtle
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(turtles):
    """
    Runs the turtle race, moving each turtle a random distance forward.
    The first turtle to reach the top of the screen wins.

    Args:
        turtles (list): A list of turtle objects participating in the race.

    Returns:
        str: The color of the winning turtle.
    """
    while True:
        for racer in turtles:
            distance = random.randrange(MIN_RANGE, MAX_RANGE)
            racer.forward(distance)

            # Check if the turtle has crossed the finish line
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return racer.color()[0]  # Return the color of the winning turtle

def init_screen():
    """
    Initializes the turtle screen with the specified width, height, and title.
    """
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game")

def main():
    """
    The main function to run the turtle racing game.
    """
    turtles_count = get_number_of_turtles()  # Get the number of turtles for the race
    init_screen()  # Initialize the turtle screen

    random.shuffle(COLORS)  # Shuffle the colors randomly
    colors = COLORS[:turtles_count]  # Select the colors for the chosen number of turtles

    turtles = create_turtles(colors)  # Create and position the turtles
    winner = race(turtles)  # Start the race and get the winner

    print(f"The winning turtle is: {winner}!")  # Announce the winner

if __name__ == "__main__":
    main()  # Run the game
