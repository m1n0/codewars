# https://www.codewars.com/kata/comic-book-hero-the-flash-saving-lives
def Saving_Lives(obstacles, miles, time, lives):
    speed = 186282

    remaining_time = time - ((obstacles * 2) + (lives * 3))
    distance = (obstacles * 2 * (speed / 2)) + (lives * 3) + (remaining_time * speed)
    return True if distance >= miles and remaining_time > 0 else False

print(Saving_Lives(29, 1072626, 167, 44))
