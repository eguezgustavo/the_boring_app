from the_boring_app.use_cases.first_thing_it_does import execute as execute_first_thing  # easter egg: o
from the_boring_app.use_cases.second_thing_it_does import execute as execute_second_thing
from the_boring_app.use_cases.third_thing_it_does import execute as execute_third_thing

from the_boring_app.services.car_service import drive_to_snack_store  # easter egg: s
from the_boring_app.services.snacks_service import pick_snack

def first_thing_the_app_does_easter_egg_U():
    execute_first_thing(drive_to_snack_store, pick_snack)


def second_thing_the_app_does_easter_egg_W():
    execute_second_thing()


def third_thing_the_app_does_easter_egg_Q():
    execute_third_thing()
