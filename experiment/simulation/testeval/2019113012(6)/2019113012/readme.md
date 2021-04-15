# Run-:
* To start game type 'python3 main.py in terminal

# Controls-:
* Press 'a' to move paddle left
* Press 'd' to move paddle right
* Press space to release the ball initially
* Press 'q' to exit the game

# Components of the game:
 * Paddle: Main paddle is used to control the ball
    Default velocity of paddle is 2 units
    paddle.py contains all classes related to padle
 * ball : This is the main ball used in the game (Multiple balls are also present in case of powerups)
 * Bricks : Total of 3 different type of bricks are present:
    i) Strong brick:Strength of this brick is 3
    ii) Unbreakable brick: This brick is unbreakable
    iii) Glass Brick: Strength of this brick is 1 and this is a special type of brick that present in the group of six bricks
 * Powerup : All powerups are present ,theser are:
    i) Increase paddle length : paddle length always remain odd and increases by 2 units
    ii) Decrease paddle length: Paddle length always remains odd and decreases by 2 units.Minimum length reachable is 3 units and it can't reduce further.
    iii) Through ball: This feature allows the ball to destroy all the brick in one go.
    iv) Paddle grab: Allows to hold the ball for some time
    v) Multiple balls: Every ball gets split up into 2 balls.
    vi) Increase ball speed:this powerup increases the speed of the ball by one unit.

# Features:-
    * Inheritance:-
    Brick and Powerup classes are inheriting from main class
    * Polymorphism:-
    All powerup classes are following polymorphism with inheritance
    * Abstraction:-
    Almost all functions are abstracted
    * Encapsulation:-
    Classes and objects are present.

# Rules
* Score increases whenever brick is destroyed completely
* Time always run when an attempt is made.
* Four lives are present
