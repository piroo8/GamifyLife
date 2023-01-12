def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars

    global is_user_tired

    global the_offered_star

    global time_of_star_offering

    global number_of_stars_offered

    global time_of_first_star_offered

    global last_hard_activity_time

    cur_hedons = 0
    cur_health = 0

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    is_user_tired = False

    the_offered_star = None
    time_of_star_offering = 0
    number_of_stars_offered = 0
    time_of_first_star_offered = 0

    last_hard_activity_time = 0

def star_can_be_taken(activity):
    if activity == the_offered_star and bored_with_stars == False and time_of_star_offering == cur_time:
        return True
    else:
        return False

def perform_activity(activity, duration):
    global last_activity, last_activity_duration
    global cur_hedons, cur_health, cur_time
    global last_hard_activity_time
    global is_user_tired

    if activity == "running":
        running_star = star_can_be_taken("running")

        if running_star == True:
            if duration <= 10:
                cur_hedons += 3 * duration
            else:
                cur_hedons += 3 * 10

        if is_user_tired == False:
            if duration >= 10:
                cur_hedons += 2 * 10
                cur_hedons += -2 * (duration - 10)
            else:
                cur_hedons += 2 * duration
        elif is_user_tired == True:
            cur_hedons += -2 * duration

        if last_activity != "running":
            if duration <= 180:
                cur_health += 3 * duration
            else:
                cur_health += 3 * 180
                cur_health += 1 * (duration - 180)
        else:
            '''The last activtiy was running then'''
            current_running_duration = duration + last_activity_duration
            if (current_running_duration) <= 180:
                cur_health += 3 * duration
            else:
                cur_health += 3 * (current_running_duration - last_activity_duration - (current_running_duration - 180))
                cur_health += 1 * (current_running_duration - 180)

        last_activity = "running"
        last_activity_duration = duration

    elif activity == "textbooks":
        textbook_star = star_can_be_taken("textbooks")

        if textbook_star == True:
            if duration <= 10:
                cur_hedons += 3 * duration
            else:
                cur_hedons += 3 * 10

        if is_user_tired == False:
            if duration >= 20:
                cur_hedons += 1 * 20
                cur_hedons += -1 * (duration - 20)
            elif is_user_tired == True:
                cur_hedons += 1 * duration
        else:
            cur_hedons += -2 * duration

        cur_health += 2 * duration

        last_activity = "textbooks"
        last_activity_duration = duration

    elif activity == "resting":
        last_activity = "resting"
        last_activity_duration = duration

    cur_time += duration

    if activity == "running" or activity == "textbooks":
        last_hard_activity_time = cur_time

    if cur_time - last_hard_activity_time >= 120:
        is_user_tired = False
    else:
        is_user_tired = True

def get_cur_hedons():
    global cur_hedons

    return cur_hedons

def get_cur_health():
    global cur_health

    return cur_health

def offer_star(activity):
    global the_offered_star
    global time_of_star_offering
    global number_of_stars_offered
    global time_of_first_star_offered
    global bored_with_stars

    number_of_stars_offered += 1

    if number_of_stars_offered == 1:
        time_of_first_star_offered = cur_time

    if (cur_time - time_of_first_star_offered) >= 120:
        number_of_stars_offered = 0

    if number_of_stars_offered >= 3:
        bored_with_stars = True

    if activity == "running" or activity == "textbooks" or activity == "resting" and bored_with_stars == False:
        the_offered_star = activity
        time_of_star_offering = cur_time

def most_fun_activity_minute():
    global is_user_tired
    duration = 1
    possible_resting_hedons = 0

    #Possible Running Hedons#
    possible_running_hedons = 0
    running_star = star_can_be_taken("running")

    if running_star == True:
        if duration <= 10:
            possible_running_hedons += 3 * duration
        else:
            possible_running_hedons += 3 * 10

    if is_user_tired == False:
        if duration >= 10:
            possible_running_hedons += 2 * 10
            possible_running_hedons += -2 * (duration - 10)
        else:
            possible_running_hedons += 2 * duration
    elif is_user_tired == True:
        possible_running_hedons += -2 * duration

    #Possible Textbook Hedons#
    possible_textbook_hedons = 0
    textbook_star = star_can_be_taken("textbooks")

    if textbook_star == True:
        if duration <= 10:
            possible_textbook_hedons += 3 * duration
        else:
            possible_textbook_hedons += 3 * 10

    if is_user_tired == False:
        if duration >= 20:
            possible_textbook_hedons += 1 * 20
            possible_textbook_hedons += -1 * (duration - 20)
        elif is_user_tired == True:
            possible_textbook_hedons += 1 * duration
    else:
        possible_textbook_hedons += -2 * duration

    max_possible_hedons = max(possible_running_hedons,possible_textbook_hedons,possible_resting_hedons)

    if max_possible_hedons == possible_running_hedons:
        return "running"
    elif max_possible_hedons == possible_textbook_hedons:
        return "texbooks"
    else:
        return "resting"

if __name__ == '__main__':
    initialize()