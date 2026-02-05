#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 12/4/2025

@author: Margarita Paiti
"""
import random
import string
import sys
from idlelib.replace import replace

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton
from enum import Enum

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60



class game_states:
    LOAD = 0
    MODE_SELECTION = 1
    START = 2
    END = 3

class lives:
    FIVE = 0
    FOUR = 1
    THREE = 2
    TWO = 3
    ONE = 4
gamestate = game_states.LOAD
answer = ""
feedback = ""

active_keys = []
active_other_keys = []


easy_keys = [
    "cat", "dog", "sun", "tree", "ball", "book", "fish", "hat", "pen", "car",
    "star", "bird", "cake", "milk", "shoe", "apple", "door", "leaf", "toy", "egg",
    "cup", "bag", "rain", "moon", "boat", "rock", "king", "queen", "fork", "spoon",
    "sock", "lamp", "note", "ring", "leaf", "bush", "frog", "nest", "leaflet", "coin",
    "mat", "desk", "pencil", "brush", "glass", "bell", "doorbell", "hatchet", "pan", "tray"
]

other_easy_keys = [
    "ant", "bat", "cow", "dig", "elf", "fog", "gum", "hen", "ice", "jam",
    "key", "lid", "man", "net", "owl", "pig", "rat", "sip", "tap",
    "van", "wig", "yak", "zip", "axe", "bus", "cap", "dip", "fan", "gap",
    "jar", "kin", "log", "mug", "nap", "oak", "pet", "quill", "rod", "sunny",
    "tin", "urns", "vial", "wax", "yarn", "zen", "pot", "cub", "mud", "bun"
]

medium_keys = [
    "dae", "otorhinolaryngologist", "nauseous", "spaghetti", "irregardless", "paranormal",
    "phenomenon", "splendid", "jalapenos", "money", "exaggerate", "neighbour", "penguin",
    "labyrinth", "elusive", "preproduction", "programming", "fundamentals", "overcast", "rambunctious",
    "silhouette", "turbulent", "whimsical", "ostrich", "quaint", "cascade", "diligent",
    "frenzy", "peculiar",
    "benevolent", "tangible", "flourish", "ephemeral", "traverse", "serenity", "luminous",
    "camaraderie", "resilient", "intricate", "jovial", "jealous", "optimistic", "mysterious", "capricious", "enigmatic", "vivacious"
]

other_medium_keys = [
    "vigilant", "melancholy", "gossamer", "conundrum",
    "audacious", "brilliant", "cunning",
    "dauntless", "elaborate", "fervent", "gregarious", "hallowed", "illustrious", "jocular",
    "keen", "lucid", "magnanimous", "notable", "obstinate", "pristine", "quixotic",
    "robust", "sagacious", "tenacious", "undaunted", "valiant", "witty", "xenial",
    "youthful", "zephyr", "ardent", "blithe", "charming", "dexterous", "exuberant", "forlorn", "gallant", "humble"
]

hard_keys = [
    "sesquipedalian", "antitransubstantiationalist",
    "radioimmunoelectrophoresis",
     "floccinaucinihilipilification", "pseudopseudohypoparathyroidism", "tetrahydrocannabinol",
    "thyrocalcitonin", "hexakosioihexekontahexaphobia",
    "ultracrepidarian", "prognosticational",  "electrocardiographically",
    "microbarograph", "laryngotracheobronchitis", "onomatopoeically", "thermoelectrically",
    "triskaidekaphobia", "circumlocutional", "psychoneuroendocrinological", "subdermatoglyphic",
    "tintinnabulation","radioimmunoelectrophoresis","onomatopoeically", "thermoelectrically",
    "counterdemonstrations"
]

other_hard_keys = [
    "otorhinolaryngologist","pneumonoultramicroscopicsilicovolcanoconiosis",
    "antidisestablishmentarianism", "hippopotomonstrosesquipedaliophobia",
    "spectrophotofluorometrically", "uncharacteristically", "electroencephalographically",
    "immunoelectrophoretically", "dichlorodifluoromethane",
    "sphygmomanometrically", "overintellectualization",
     "zoogeographical",
    "honorificabilitudinitatibus", "thyroparathyroidectomized", "psychophysicotherapeutics", "incomprehensibilities"
]

score = 0
chose = ""

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    pass

def reset_round():
    global answer, time, feedback, active_keys, active_other_keys, gamestate

    answer = ""
    feedback = ""
    time = 10

    active_keys = active_keys_original.copy()
    active_other_keys = active_other_keys_original.copy()

    choose_new_word()
    gamestate = game_states.START


def choose_new_word():
    global key, other_key, active_keys, active_other_keys, gamestate

    if not active_keys or not active_other_keys:
        reset_round()
        return

    key = random.choice(active_keys)
    active_keys.remove(key)

    other_key = random.choice(active_other_keys)
    active_other_keys.remove(other_key)


def handle_letter_input(letter):
    global answer, feedback, score, time
    for word in [key, other_key]:
        letter = letter.lower()
        if (answer + letter) == word[:len(answer)+1]:
            answer += letter
            feedback = "Correct!"
            return
    feedback = "Wrong letter!"
    score -= 5
    time -= 2

def draw_feedback():
    global feedback
    engine.color = 1, 0, 0
    engine.set_font_size(80)
    engine.draw_text(feedback, engine.width/2, 300, True)

def initialize_variables():
    global load_screen,game_background,man_up,man_r,man_l,char_x_position\
        ,char_y_position,kitchen,woman_up,woman_l,woman_r,char_width,char_height\
        ,char_width,char_height,cat_l,cat_r,char_width,char_height,speed\
        ,crazy_chef_R, crazy_chef_L , chef_x_position,chef_y_position,chef_speed,chef_direction,mode_selection\
        ,easy,medium,hard,hard_pizza_slice,medium_pizza_slice,easy_pizza_slice\
        ,words,char_direction,char_speed,text_placeholder,time,count_frames,lives\
        ,easy_box_x,easy_box_y,medium_box_x,medium_box_y,hard_box_x,hard_box_y,chef_width,chef_height\
        ,total_time,live
    load_screen = engine.load_image('resources/loading_pizzaria.png')
    mode_selection = engine.load_image('resources/mode_selection.jpg')
    game_background = engine.load_image('resources/background_pizzaria.png')
    kitchen = engine.load_image('resources/kitchen.png')
    crazy_chef_R = engine.load_image('resources/crazy_chef_R.png')
    crazy_chef_L = engine.load_image('resources/crazy_chef_L.png')
    easy = engine.load_image('resources/pizza_box.png')
    medium = engine.load_image('resources/pizza_box.png')
    hard = engine.load_image('resources/pizza_box.png')
    hard_pizza_slice = engine.load_image('resources/hard_pizza_slice.png')
    medium_pizza_slice = engine.load_image('resources/medium_pizza_slice.png')
    easy_pizza_slice = engine.load_image('resources/easy_pizza_slice.png')
    live = engine.load_image('resources/lives.png')
    chef_x_position = 400
    chef_y_position = 80
    chef_width = 200
    chef_height = 200
    chef_direction = 1
    chef_speed = 3
    char_speed = 3
    time = 10
    count_frames = 0
    lives = 5
    easy_box_x = 50
    easy_box_y = 10
    medium_box_x = 300
    medium_box_y = 10
    hard_box_x = 550
    hard_box_y = 10
    total_time = 0
initialize_variables()

def draw_lives():
    global lives, live
    for i in range(lives):
        live.draw_fixed_size(200 + i*70, 20, 80, 80, False)  # Draw each heart


def show_key():
    words = [key, other_key]
    y = 500

    engine.color = 1,1,1
    engine.set_font_size(50)

    for word in words:
        engine.draw_text(word, engine.width / 2, y, True)
        y += 50

    engine.color = 1,1,1
    engine.set_font_size(50)
    question = "Enter a word to guess:"
    engine.set_font_size(50)
    engine.draw_text(f"{question}",200,450,True)

def draw_go_back():
    engine.set_font_size(50)
    engine.color = 0,0,0
    is_mouse_inside_home = engine.colliding_point_in_rect(engine.mouse_x,engine.mouse_y,30,100,200,50)
    if is_mouse_inside_home:
        engine.color = 1,0,0
    engine.draw_text("Home Screen",30, 100, False)


def draw_replay():
    engine.set_font_size(80)
    engine.color = 0,0,0
    is_mouse_inside_replay = engine.colliding_point_in_rect(engine.mouse_x,engine.mouse_y,300,500,300,80)
    if is_mouse_inside_replay:
        engine.color = 1,0,0
    engine.draw_text("Replay", engine.width / 2, 500, True)

def draw_score():
    global score,game_states,gamestate
    engine.set_font_size(80)
    engine.draw_text("Score:",20,20,False)
    engine.draw_text(f"{score}",20,80,False)



def draw_modes():
    engine.color = 1,1,1
    engine.draw_text("EASY          MEDIUM            HARD",engine.width/2,390,True)

def draw_crazy_chef():
    global crazy_chef_R,crazy_chef_L,chef_x_position,chef_y_position,chef_width,chef_height
    if chef_direction == 1:
        crazy_chef_R.draw_fixed_size(chef_x_position, chef_y_position,chef_width,chef_height,True)
    if chef_direction == -1 :
        crazy_chef_L.draw_fixed_size(chef_x_position, chef_y_position,chef_width,chef_height,True)


def draw_easy_box():
    global easy,easy_pizza_slice,easy_box_x,easy_box_y
    easy.draw_fixed_size(easy_box_x,easy_box_y,200,200,False)
    is_mouse_inside_box = engine.colliding_point_in_circle(engine.mouse_x, engine.mouse_y, 50, 10, 200)
    if is_mouse_inside_box:
        easy_pizza_slice.draw_fixed_size(100, 250, 100, 100, False)
def draw_medium_box():
    global medium,medium_pizza_slice,medium_box_x,medium_box_y
    medium.draw_fixed_size(medium_box_x,medium_box_y,200,200,False)
    is_mouse_inside_box = engine.colliding_point_in_circle(engine.mouse_x,engine.mouse_y,300,10,200)
    if is_mouse_inside_box:
        medium_pizza_slice.draw_fixed_size(350, 250, 100, 100, False)


def draw_hard_box():
    global hard,hard_pizza_slice,hard_box_x,hard_box_y
    hard.draw_fixed_size(hard_box_x , hard_box_y, 200, 200, False)
    is_mouse_inside_box = engine.colliding_point_in_circle(engine.mouse_x,engine.mouse_y,500,10,200)
    if is_mouse_inside_box:
        hard_pizza_slice.draw_fixed_size(600, 250, 100, 100, False)

def choose_mode():
    engine.color = 1,1,1
    engine.draw_text("Choose your pizza box!",engine.width /2,500,True)


def draw_box():
    engine.color = 0,0,0
    engine.outline_color = 0,0,0
    engine.draw_rectangle(0,450,engine.width,450)
    engine.color = 0,1,1
    engine.draw_text(answer,engine.width/2,100,True)

def draw_mode_selection():
    global mode_selection
    mode_selection.draw_fixed_size(0,0,engine.width,engine.height,False)

def draw_kitchen():
    kitchen.draw_fixed_size(0,0, engine.width, engine.height, False)

def draw_load_screen():
    load_screen.draw_fixed_size(0, 0,engine.width, engine.height,False)
    engine.color = 0,0,0
    engine.set_font_size(50)
    engine.draw_text("Press ENTER to begin the journey!",engine.width /2,50,True)


def draw_background_pizzaria():
    game_background.draw_fixed_size(0,0,engine.width,engine.height,False)

def draw_time():
    global time
    engine.color = 1,1,1
    engine.set_font_size(80)
    engine.draw_text("TIME",550,50,False)
    engine.draw_text(f"{time}",580,100,False)

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global char_x_position,char_y_position,woman_states,char_width,char_height,feedback,woman_r,cat_r,man_r,score
    if gamestate == game_states.LOAD:
        engine.background_color = 0,0,0
        draw_load_screen()
    elif gamestate == game_states.MODE_SELECTION:
        draw_mode_selection()
        choose_mode()
        draw_modes()
        draw_easy_box()
        draw_medium_box()
        draw_hard_box()
    if gamestate == game_states.START:
        draw_background_pizzaria()
        draw_lives()
        draw_box()
        show_key()
        draw_feedback()
        draw_time()
        draw_score()
        draw_crazy_chef()
    elif gamestate == game_states.END:
        engine.color = 0,0,0
        engine.background_color = 1,1,1
        feedback == ""
        engine.set_font_size(80)
        if lives == 0:
            engine.set_font_size(40)
            engine.background_color = 1,0,0
            engine.color = 0,0,0
            engine.draw_text("Game Over!",engine.width / 2,engine.height / 2,True)
        if score == 200 :
            engine.background_color = 1,1,1
            engine.set_font_size(40)
            engine.color = 0,0,0
            engine.draw_text("You Win!", engine.width / 2, engine.height / 2, True)
        engine.draw_text(f"Score : {score}",engine.width / 2,engine.height / 2 + 80,True)
        engine.draw_text(f"Total Time: {total_time} secs",500,100,False)
        draw_replay()
        draw_go_back()
def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    global char_x_position,char_y_position,char_width,char_height,speed,chef_x_position,chef_y_position
    global chef_direction,chef_speed,char_direction,char_speed,time,count_frames,lives,key,answer
    global gamestate,feedback,score,total_time
    if gamestate == game_states.START :
        chef_x_position += chef_direction * chef_speed
        if chef_x_position <= 150:
            chef_direction = 1
        if chef_x_position >= 350:
            chef_direction = -1

        count_frames += 1
        if count_frames >= 60:
            total_time += 1
            time -= 1
            count_frames = 0
        if time < 0:
            lives -= 1
            time = 10
            choose_new_word()
            answer = ""
        if answer == key or answer == other_key:
            feedback = "Good job!"
            answer = ""
            choose_new_word()
            lives == lives
            time = 10
            score += 10
        if lives == 0 :
            gamestate = game_states.END
        if score >= 200 :
            gamestate = game_states.END
def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    global gamestate,easy_box_x,easy_box_y,medium_box_x,medium_box_y,hard_box_x,hard_box_y,easy_keys,other_keys,medium_keys
    global other_medium_keys,hard_keys,other_hard_keys,score,lives,total_time,active_keys,active_other_keys
    global active_keys_original, active_other_keys_original

    if gamestate == game_states.MODE_SELECTION and mouse_button.LEFT:
        if easy_box_x <= mouse_x <= easy_box_x + 200 and easy_box_y <= mouse_y <= easy_box_y + 200:
            active_keys = easy_keys.copy()
            active_other_keys = other_easy_keys.copy()
            active_keys_original = active_keys.copy()
            active_other_keys_original = active_other_keys.copy()
            choose_new_word()
            gamestate = game_states.START

        if medium_box_x <= mouse_x <= medium_box_x + 200 and medium_box_y <= mouse_y <= medium_box_y + 200:
            active_keys = medium_keys.copy()
            active_other_keys = other_medium_keys.copy()
            active_keys_original = active_keys.copy()
            active_other_keys_original = active_other_keys.copy()
            choose_new_word()
            gamestate = game_states.START

        if hard_box_x <= mouse_x <= hard_box_x + 200 and hard_box_y <= mouse_y <= hard_box_y + 200:
            active_keys = hard_keys.copy()
            active_other_keys = other_hard_keys.copy()
            active_keys_original = active_keys.copy()
            active_other_keys_original = active_other_keys.copy()
            choose_new_word()
            gamestate = game_states.START

    if gamestate == game_states.END:
        is_mouse_inside_replay = engine.colliding_point_in_rect(engine.mouse_x, engine.mouse_y, 300, 500, 300, 80)
        if mouse_button.LEFT and is_mouse_inside_replay:
            lives = 5
            score = 0
            total_time = 0
            reset_round()

        is_mouse_inside_home = engine.colliding_point_in_rect(engine.mouse_x, engine.mouse_y, 30, 100, 200, 50)
        if mouse_button.LEFT and is_mouse_inside_home :
            lives = 5
            score = 0
            total_time = 0
            gamestate = game_states.LOAD

def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    global gamestate,answer,char_width,char_height,char_x_position,char_y_position,text_placeholder
    if key == "ESCAPE":
        sys.exit()
    if gamestate == game_states.LOAD and key  == 'ENTER' :
        gamestate = game_states.MODE_SELECTION


    if gamestate == game_states.START:
        allowed_characters = set(string.ascii_letters)
        if key in allowed_characters:
            handle_letter_input(key)


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
