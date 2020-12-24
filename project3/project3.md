# Project 3: Ants Vs. SomeBees

![splash](images/splash.png)

> The bees are coming!
> Create a better soldier with inherit-ants.

## Download Project Materials

To get started, download project materials `project3.zip` from our QQ group if you don't have one. Below is a list of all the files you will see in the `project3.zip`. However, you only have to make changes to `ants/ants.py` in this project.

```
project3
  |-ants
  |  |-ants.py     # The game logic of Ants Vs. SomeBees
  |  |-ants_gui.py # The original GUI for Ants Vs. SomeBees
  |  |-graphics.py # Utilities for displaying simple two-dimensional animations
  |  |-utils.py    # Some functions to facilitate the game interface
  |  |-ucb.py      # Utility functions from CS 61A
  |  |-assets      # A directory of images and files used by gui.py
  |  |-img         # A directory of images used by ants_gui.py
  |  |-ok          # The autograder
  |  |-proj3.ok    # The ok configuration file
  |  `-tests       # A directory of tests used by ok
  `-project3.pdf   # Instructions for this project you must read
```

## Introduction

> **Important submission notes**: This project has four phases. You have seven days for Phase 1&2 and seven more days for Phase 2&3. It doesn't mean that you are restricted to complete Phase 3&4 in just seven days. That is, you have 14 days in total for this project but the Phase 1&2 should be finished in the first 7 days. We recommend starting and finishing Phase 1&2 as soon as possible to give yourself adequate time to complete Phases 3&4, which can be more time consuming. Check the exact deadline on our OJ website.
>
> After completing any problems required in each phase, you need to submit your answer to `Contest 'ants: phase 1&2'` and `Contest 'ants: phase 3&4'` correspondingly on our [OJ website](http://114.212.84.18) to get your answer scored. We recommend that you submit **after you finish each problem** so that you can find bugs as soon as possible.

In this project, you will create a [tower defense](https://baike.baidu.com/item/%E5%A1%94%E9%98%B2%E6%B8%B8%E6%88%8F/3296020) game called Ants Vs. SomeBees. As the ant queen, you populate your colony with the bravest ants you can muster. Your ants must protect their queen from the evil bees that invade your territory. Irritate the bees enough by throwing leaves at them, and they will be vanquished. Fail to pester the airborne intruders adequately, and your queen will succumb to the bees' wrath. This game is inspired by PopCap Games' [Plants Vs. Zombies](https://www.ea.com/studios/popcap/plants-vs-zombies).

This project combines functional and object-oriented programming paradigms, focusing on the material from [Chapter 2.5](http://composingprograms.com/pages/25-object-oriented-programming.html) of Composing Programs. The project also involves understanding, extending, and testing a large program.

## Suggestions

For the functions that we ask you to complete, there may be some initial code that we provide. If you would rather not use that code, feel free to delete it and start from scratch. You may also add new function definitions as you see fit.

However, please do **not** modify any other functions. Doing so may result in your code failing our framework. Also, please do **not** change any function signatures (names, argument order, or number of arguments).

## The Game
A game of Ants Vs. SomeBees consists of a series of turns. In each turn, new bees may enter the ant colony. Then, new ants are placed to defend their colony. Finally, all insects (ants, then bees) take individual actions. Bees either try to move toward the end of the tunnel or sting ants in their way. Ants perform a different action depending on their type, such as collecting more food, or throwing leaves at the bees. The game ends either when a bee reaches the end of a tunnel (you lose), or the entire bee fleet has been vanquished (you win).

![gui_explanation](images/gui_explanation.png)

### Core concepts
**The Colony.** This is where the game takes place. The colony consists of several *places* that are chained together to form a tunnel where bees can travel through. The colony has some quantity of food that can be expended to deploy ant troops.

**Places.** A place links to another place to form a tunnel. The player can place a single ant into each place. However, there can be many bees in a single place.

**The Hive.** This is the place where bees originate. Bees exit the beehive to enter the ant colony.

**Ants.** Ants are the usable troops in the game that the player places into the colony. Each type of ant takes a different action and requires a different amount of food to place. The two most basic ant types are the `HarvesterAnt`, which adds one food to the colony during each turn, and the `ThrowerAnt`, which throws a leaf at a bee each turn. You will be implementing many more.

**Bees.** Bees are the antagonistic troops in the game that the player must defend the colony from. Each turn, a bee either advances to the next place in the tunnel if no ant is in its way, or it stings the ant in its way. Bees win when at least one bee reaches the end of a tunnel.

### Core classes

The concepts described above each have a corresponding class that encapsulates the logic for that concept. Here is a summary of the main classes involved in this game:

- `GameState`: Represents the colony and some state information about the game, including how much food is available, how much time has elapsed, where the `QueenAnt` resides, and all the `Places` in the game.
- `Place`: Represents a single place that holds insects. At most one `Ant` can be in a single place, but there can be many `Bee`s in a single place. `Place` objects have an `exit` to the left and an `entrance` to the right which are also places. Bees travel through a tunnel by moving to a `Place`'s `exit`.
- `Hive`: Represents the place where `Bee`s start out (on the right of the tunnel).
- `AntHomeBase`: Represents the place `Ant`s are defending (on the left of the tunnel). If `Bee`s get here, they win :(
- `Insect`: A superclass for `Ant` and `Bee`. All insects have an `armor` attribute, representing their remaining health, and a `place` attribute, representing the `Place` where they are currently located. Each turn, every active `Insect` in the game performs its `action`.
- `Ant`: Represents ants. Each `Ant` subclass has special attributes or a special `action` that distinguish it from other `Ant` types. For example, a `HarvesterAnt` gets food for the colony and a `ThrowerAnt` attacks `Bee`s. Each ant type also has a `food_cost` attribute that indicates how much it costs to deploy one unit of that type of ant.
- `Bee`: Represents bees. Each turn, a bee either moves to the `exit` of its current Place if no ant blocks its path, or stings an ant that blocks its path.

### Game Layout

Below is a visualization of an GameState. As you work through the unlocking tests and problems, we recommend drawing out similar diagrams to help your understanding.

![colony-drawing](images/colony-drawing.png)

### Playing the game

The game can be run in two modes: as a text-based game or using a graphical user interface (GUI). The game logic is the same in either case, but the GUI enforces a turn time limit that makes playing the game more exciting. The text-based interface is provided for debugging and development.

The files are separated according to these two modes. `ants.py` knows nothing of graphics or turn time limits.

To start a text-based game, run

```
python ants_text.py
```

To start a graphical game, run

```
python ants_gui.py
```

When you start the graphical version, a new browser window should appear. In the starter implementation, you have unlimited food and your ants can only throw leaves at bees in their current `Place`. Try playing the game anyway! You'll need to place a lot of `ThrowerAnts` (the second type) in order to keep the bees from reaching your queen.

The game has several options that you will use throughout the project, which you can view with `python ants_text.py --help`
(or `python ants_gui.py --help` in GUI mode).

```
usage: ants_text.py [-h] [-d DIFFICULTY] [-w] [--food FOOD]

Play Ants vs. SomeBees

optional arguments:
  -h, --help     show this help message and exit
  -d DIFFICULTY  sets difficulty of game (test/easy/medium/hard/extra-hard)
  -w, --water    loads a full layout with water
  --food FOOD    number of food to start with when testing
```

## Phase 1: Basic gameplay

> **Important submission notes**: After completing any problems required in this phase, you need to submit your answer to `Contest 'ants: phase 1&2'` on our [OJ website](http://114.212.84.18) to get your answer scored. Don't forget to check the deadline on the OJ website.

### Problem 0 (0 pts)

Before writing any code, let us introduce a new tool `ok` that is used in this project.

`ok` is an auto-grader that is designed to check your understanding of problems and test your code. It is distributed along with our project, so you can find it in the `ants` directory.

To use `ok`, you should open the terminal, `cd` to the `ants` directory, and then use the command like `python ok --local <options>...` to start `ok`. What does the `--local` option mean here? Well, `ok` has two modes: remote mode and local mode. The remote mode works like our OJ website where `ok` tests and grades your code remotely. The local mode works like doctest where `ok` tests your code locally. Since we have already had an OJ website, we just use the local mode in this project. Don't forget to add `--local` option when using `ok`. What would happen if you forgot it? Well, nothing, because we have changed the ok configuration file to suppress something bad.

> If you forget how to use terminal or what the common format of commands is, please refer to `lab00`.

Now the current procedure to do assignments with `ok` is as follows:
1. Read the instructions for some `<problem>`.
2. Use `python ok --local -q <problem> -u` to unlock the test cases for the `<problem>` by answering the questions from `ok`. This step is used to check your understanding of the `<problem>` before you write any code. The test cases are locked at the beginning, so you couldn't test your code if you bypass this step.
3. Write some code as required by the `<problem>`.
4. Use `python ok --local -q <problem>` to test your code for the `<problem>`. If you didn't pass the tests, `ok` will show you some error messages such as which test case you failed. Fix your code in your text editor until the test passes.
5. Submit your code to our OJ website to get your code scored.

You may need some explanations for the commands we just mentioned:
- Well, the `--local` option has been explained before.
- The `-q` option is used to test a particular question. For example, `-q 01` means testing problem 1 only, so you will not see any annoying unrelated errors from the test cases for the problems you have not completed. If `-q` is not used, it means testing all the problems in this project, which is somewhat like `python -m doctest xxx.py` used in the previous assignments. Therefore, you can use `python ok --local` to test your code all at once after you complete the project.
- The test cases are locked at the beginning, so `-u` is used to unlock them by answering the questions from `ok`  before you can use `-q` to test your code. `ok` will guide you how to answer its questions.

Don't worry! We will let you known which command you should use when you need it.

> By the way, the test cases used by `ok` is placed in the `ants/tests` directory.

Now, let's try out `ok` for the problem 0. First, read the entire `ants.py` file. Then, test your understanding and unlock test cases for the problem 0 by answering the questions from `ok`:

```
python ok --local -q 00 -u
```

If you cannot answer these questions, read the file again, consult the core concepts/classes sections above, or ask a question in the QQ group.

> The problem 0 doesn't require writing any code, so you needn't do step 2-4 as described above. That is to say, you needn't write, test, and submit your code any further in this problem. In fact, problem 0 doesn't have any test cases as well. Therefore, `-u` is just used to have you answer some questions and will not unlock any test cases here.

### Problem 1 (100 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 01 -u
```

First, add food costs and implement harvesters. Currently, there is no cost for deploying any type of `Ant`, and so there is no challenge to the game. You'll notice that `Ant` has a base `food_cost` of zero. Override this value in each of the subclasses listed below with the correct costs.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_harvester.gif" height="80px" width="80px" /> | `HarvesterAnt` | 2 | 1|
| <img src="images/ant_thrower.gif" height="80px" width="80px"/> | `ThrowerAnt` | 3 | 1 |


Now that deploying `Ant`s cost food, we need to be able to gather more food! To fix this issue, implement the `HarvesterAnt` class. A `HarvesterAnt` is a type of `Ant` that adds one food to the `gamestate.food` total as its `action`.

After writing code, test your implementation:

```
python ok --local -q 01
```

Try playing the game by running `python ants_gui.py`. Once you have placed a `HarvesterAnt`, you should accumulate food each turn. You can also place `ThrowerAnts`, but you'll see that they can only attack bees that are in their `Place`, so it'll be a little difficult to win.

### Problem 2 (300 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 02 -u
```

Complete the `Place` constructor by adding code that tracks entrances. Right now, a `Place` keeps track only of its `exit`. We would like a `Place` to keep track of its entrance as well. A `Place` needs to track only one `entrance`. Tracking entrances will be useful when an `Ant` needs to see what `Bee`s are in front of it in the tunnel.

However, simply passing an entrance to a `Place` constructor will be problematic; we would need to have both the exit and the entrance before creating a `Place`! (It's a chicken or the egg problem.) To get around this problem, we will keep track of entrances in the following way instead. The `Place` constructor should specify that:

- A newly created `Place` always starts with its `entrance` as `None`.
- If the `Place` has an `exit`, then the `exit`'s `entrance` is set to that `Place`.

> *Hint*: Remember that when the `__init__` method is called, the first parameter, `self`, is bound to the newly created object.

> *Hint*: Try drawing out two `Place`s next to each other if things get confusing. In the GUI, a place's `entrance` is to its right while the `exit` is to its left.

After writing code, test your implementation:

```
python ok --local -q 02
```

### Problem 3 (200 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 03 -u
```

In order for a `ThrowerAnt` to attack, it must know which bee it should hit. The provided implementation of the `nearest_bee` method in the `ThrowerAnt` class only allows them to hit bees in the same `Place`. Your job is to fix it so that a `ThrowerAnt` will `throw_at` the nearest bee in front of it that is not still in the `Hive`.

The `nearest_bee` method returns a random `Bee` from the nearest place that contains bees. Places are inspected in order by following their `entrance` attributes.

- Start from the current `Place` of the `ThrowerAnt`.
- For each place, return a random bee if there is any, or consider the next place that is stored as the current place's `entrance`.
- If there is no bee to attack, return `None`.

> *Hint*: The `random_or_none` function provided in `ants.py` returns a random element of a sequence or None if the sequence is empty.

> *Hint*: Having trouble visualizing the test cases? Try drawing them out on paper! The example diagram provided in [Game Layout](#game-layout) shows the first test case for this problem.

After writing code, test your implementation:

```
python ok --local -q 03
```

After implementing `nearest_bee`, a `ThrowerAnt` should be able to `throw_at` a `Bee` in front of it that is not still in the `Hive`. Make sure that your ants do the right thing! To start a game with ten food (for easy testing):

```
python ants_gui.py --food 10
```

## Phase 2: Ants!

Now that you've implemented basic gameplay with two types of `Ant`s, let's add some flavor to the ways ants can attack bees. In this phase, you'll be implementing several different `Ant`s with different offensive capabilities.

After you implement each `Ant` subclass in this section, you'll need to set its `implemented` attribute to `True` so that that type of ant will show up in the GUI. Feel free to try out the game with each new ant to test the functionality!

With your Phase 2 ants, try `python ants_gui.py -d easy` to play against a full swarm of bees in a multi-tunnel layout and try `-d normal`, `-d hard`, or `-d extra-hard` if you want a real challenge! If the bees are too numerous to vanquish, you might need to create some new ants.

### Problem 4 (200 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 04 -u
```

The `ThrowerAnt` is a great offensive unit, but it'd be nice to have a cheaper unit that can throw. Implement two subclasses of `ThrowerAnt` that are less costly but have constraints on the distance they can throw:

- The `LongThrower` can only `throw_at` a `Bee` that is found after following at least 5 `entrance` transitions. It cannot hit `Bee`s that are in the same `Place` as it or the first 4 `Place`s in front of it. If there are two `Bee`s, one too close to the `LongThrower` and the other within its range, the `LongThrower` should throw past the closer `Bee`, instead targeting the farther one, which is within its range.
- The `ShortThrower` can only `throw_at` a `Bee` that is found after following at most 3 `entrance` transitions. It cannot throw at any ants further than 3 `Place`s in front of it.

Neither of these specialized throwers can `throw_at` a `Bee` that is exactly 4 `Place`s away.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_longthrower.gif" height="80px" width="80px" /> | `ShortThrower` | 2 | 1 |
| <img src="images/ant_shortthrower.gif" height="80px" width="80px"/> | `LongThrower` | 2 | 1 |

A good way to approach the implementation to `ShortThrower` and `LongThrower` is to have it inherit the `nearest_bee` method from the base `ThrowerAnt` class. The logic of choosing which bee a thrower ant will attack is essentially the same, except the `ShortThrower` and `LongThrower` ants have maximum and minimum ranges, respectively.

To implement these behaviors, you will need to modify the `nearest_bee` method to reference `min_range` and `max_range` attributes, and only return a bee that is in range.

Make sure to give these `min_range` and `max_range` sensible defaults in `ThrowerAnt` that do not change its behavior. Then, implement the subclasses `LongThrower` and `ShortThrower` with appropriately constrained ranges and correct food costs.

> *Hint*: `float('inf')` returns an infinite positive value represented as a float that can be compared with other numbers.

Don't forget to set the `implemented` class attribute of `LongThrower` and `ShortThrower` to `True`.

> Note! Please make sure your attributes are called `max_range` and `min_range` rather than `maximum_range` and `minimum_range` or something. The tests directly reference this variable name.

After writing code, test your implementation (rerun the tests for 03 to make sure they still work):

```
python ok --local -q 03
python ok --local -q 04
```

### Problem 5 (300 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 05 -u
```

Implement the `FireAnt`, which does damage when it receives damage. Specifically, if it is damaged by `armor` armor units, it does a damage of `armor` to all bees in its place (this is called *reflected damage*).

If it dies, it does an additional amount of damage, which is specified by its `damage` attribute (by default 3).

To implement this, we have to override the `FireAnt`'s `reduce_armor` method. Normally, `Insect.reduce_armor `will decrement the insect's `armor` by the given `amount` and remove the insect from its place if `armor` reaches zero or lower. However, `FireAnt` also does damage to all the bees in its place when it receives damage, with a special bonus when its armor drops to 0, before being removed from its `place`.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_fire.gif" height="80px" width="80px" /> | `FireAnt` | 5 | 3 |

> *Hint*: To damage a `Bee`, call the `reduce_armor` method inherited from `Insect`.
>
> *Hint*: Damaging a bee may cause it to be removed from its place. If you iterate over a list, but change the contents of that list at the same time, you [may not visit all the elements](https://docs.python.org/3/tutorial/controlflow.html#for-statements). This can be prevented by making a copy of the list. You can either use a list slice, or use the built-in `list` function.
>
> ```
> >>> lst = [1,2,3,4]
> >>> lst[:]
> [1, 2, 3, 4]
> >>> list(lst)
> [1, 2, 3, 4]
> >>> lst[:] is not lst and list(lst) is not lst
> True
> ```

Once you've finished implementing the `FireAnt`, give it a class attribute `implemented` with the value `True`.

> Note, even though you are overriding the `Insect.reduce_armor` function, you can still use it in your implementation by calling it directly (rather than via `self`). Note that this is not recursion (why?)

After writing code, test your implementation:

```
python ok --local -q 05
```

You can also test your program by playing a game or two! A `FireAnt` should destroy all co-located `Bee`s when it is stung. To start a game with ten food (for easy testing):

```
python ants_gui.py --food 10
```

### Problem 6 (200 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 06 -u
```

Implement the `HungryAnt`, which will select a random `Bee` from its `place` and eat it whole. After eating a `Bee`, it must spend 3 turns digesting before eating again. If there is no bee available to eat, it will do nothing.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_hungry.gif" height="80px" width="80px" /> | `HungryAnt` | 4 | 1 |

Give `HungryAnt` a `time_to_digest` class attribute that holds the number of turns that it takes a `HungryAnt` to digest (default to 3). Also, give each `HungryAnt` an instance attribute `digesting` that counts the number of turns it has left to digest (default is 0, since it hasn't eaten anything at the beginning).

Implement the `action` method of the `HungryAnt` to check if it is digesting; if so, decrement its `digesting` counter. Otherwise, eat a random `Bee` in its `place` by reducing the `Bee`'s armor to 0 and restart the `digesting` timer.

After writing code, test your implementation:

```
python ok --local -q 06
```

### Problem 7 (200 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 07 -u
```

Implement the `NinjaAnt`, which damages all `Bee`s that pass by, but can never be stung.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_ninja.gif" height="80px" width="80px" /> | `Ninja` | 5 | 1 |

A `NinjaAnt` does not block the path of a `Bee` that flies by. To implement this behavior, first modify the `Ant` class to include a new class attribute `blocks_path` that is `True` by default. Set the value of `blocks_path` to `False` in the `NinjaAnt` class.

Second, modify the `Bee`'s method `blocked` to return `False` if either there is no `Ant` in the `Bee`'s `place` or if there is an `Ant`, but its `blocks_path` attribute is `False`. Now `Bee`s will just fly past `NinjaAnts`.

Finally, we want to make the `NinjaAnt` damage all `Bee`s that fly past. Implement the `action` method in `NinjaAnt` to reduce the armor of all `Bee`s in the same `place` as the `NinjaAnt` by its `damage` attribute. Similar to the `FireAnt`, you must iterate over a list of bees that may change.

> *Hint*: Having trouble visualizing the test cases? Try drawing them out on paper! See the example in [Game Layout](#game-layout) for help.

After writing code, test your implementation:

```
python ok --local -q 07
```

For a challenge, try to win a game using only `HarvesterAnt` and `NinjaAnt`.

Congratulations! You have finished Phases 1 and 2 of this project!

## Phase 3: More Ants!

> **Important submission notes**: After completing any problems required in the following two phases, you need to submit your answer to `Contest 'ants: phase 3&4'` on our [OJ website](http://114.212.84.18) to get your answer scored. Don't forget to check the deadline on the OJ website.

We now have some great offensive troops to help vanquish the bees, but let's make sure we're also keeping our defensive efforts up. In this phase you will implement ants that have special defensive capabilities such as increased armor and the ability to protect other ants.

### Problem 8 (100 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 08 -u
```

We are going to add some protection to our glorious home base by implementing the `WallAnt`, which is an ant that does nothing each turn. A `WallAnt` is useful because it has a large `armor` value.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_wall.gif" height="80px" width="80px" /> | `WallAnt` | 4 | 4 |

Unlike with previous ants, we have not provided you with a class header. Implement the `WallAnt` class from scratch. Give it a class attribute `name` with the value `'Wall'` (so that the graphics work) and a class attribute `implemented` with the value `True` (so that you can use it in a game).

After writing code, test your implementation:

```
python ok --local -q 08
```

### Problem 9 (400 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 09 -u
```

Right now, our ants are quite frail. We'd like to provide a way to help them last longer against the onslaught of the bees. Enter the `BodyguardAnt`.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_bodyguard.gif" height="80px" width="80px" /> | `BodyguardAnt` | 4 | 2 |

A `BodyguardAnt` differs from a normal ant because it is a `ContainerAnt`; it can contain another ant and protect it, all in one `Place`. When a `Bee` stings the ant in a `Place` where one ant contains another, only the container is damaged. The ant inside the container can still perform its original action. If the container perishes, the contained ant still remains in the place (and can then be damaged).

Each `ContainerAnt` has an instance attribute `contained_ant` that stores the ant it contains. It initially starts off as `None`, to indicate that no ant is being protected. Implement the `contain_ant` method so that it sets the bodyguard's `contained_ant` instance attribute to the passed in `ant` argument. Also implement the `ContainerAnt`'s `action` method to perform its `contained_ant`'s action if it is currently containing an ant.

In addition, you will need to make the following modifications throughout your program so that a container and its contained ant can both occupy a place at the same time (a maximum of two ants per place), but only if exactly one is a container:

1. Implement the method `ContainerAnt.can_contain` which takes an other ant as an argument and returns `True` if:
  - This ant does not already contain another ant.
  - The other ant is not a container.
  Currently `Ant.can_contain` returns `False` by default; it needs to be overridden in `ContainerAnt`.
2. Modify `Ant.add_to` to allow a container and a non-container ant to occupy the same place according to the following rules:
  - If the ant currently occupying a place can contain the current ant, then it does.
  - If the current ant can contain the ant in the space, then it does.
  - If neither Ant can contain the other, raise the same AssertionError as before (the one already present in the starter code).
3. Add a `BodyguardAnt.__init__` that changes the default amount of armor.

> Hint: You may find the `isinstance` function useful for checking if an object is an instance of a given class. For example:
> ```
> >>> a = Foo()
> >>> isinstance(a, Foo)
> True
> ```

> Note: the constructor of `ContainerAnt.__init__` is implemented as such
> ```python
> def __init__(self, *args, **kwargs):
>    Ant.__init__(self, *args, **kwargs)
>    self.contained_ant = None
> ```
> As we saw in Hog, we have that `args` is bound to all positional arguments (that is all arguments not passed not with keywords, and `kwargs` is bound to all the keyword arguments. This ensures that both sets of arguments are passed to the Ant constructor).
>
> Effectively, this means the constructor is exactly the same as `Ant.__init__` but sets `self.contained_ant = None`

After writing code, test your implementation:

```
python ok --local -q 09
```

### Problem 10 (100 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 10 -u
```

The `BodyguardAnt` provides great defense, but they say the best defense is a good offense. The `TankAnt` is a container that protects an ant in its place and also deals 1 damage to all bees in its place each turn.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_tank.gif" height="80px" width="80px" /> | `TankAnt` | 6 | 2 |

You should not need to modify any code outside of the `TankAnt` class. If you find yourself needing to make changes elsewhere, look for a way to write your code for the previous question such that it applies not just to `BodyguardAnt` and `TankAnt` objects, but to container ants in general.

After writing code, test your implementation:

```
python ok --local -q 10
```

## Phase 4: Water and Might

In the final phase, you're going to add one last kick to the game by introducing a new type of place and new ants that are able to occupy this place. One of these ants is the most important ant of them all: the queen of the colony.

### Problem 11 (100 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 11 -u
```

Let's add water to the colony! Currently there are only two types of places, the `Hive` and a basic `Place`. To make things more interesting, we're going to create a new type of `Place` called `Water`.

Only an ant that is watersafe can be deployed to a `Water` place. In order to determine whether an `Insect` is watersafe, add a new attribute to the `Insect` class named `is_watersafe` that is `False` by default. Since bees can fly, make their `is_watersafe` attribute `True`, overriding the default.

Now, implement the `add_insect` method for `Water`. First, add the insect to the place regardless of whether it is watersafe. Then, if the insect is not watersafe, reduce the insect's armor to 0. *Do not repeat code from elsewhere in the program.* Instead, use methods that have already been defined.

After writing code, test your implementation:

```
python ok --local -q 11
```

Once you've finished this problem, play a game that includes water. To access the `wet_layout` which includes water, add the `--water` option (or `-w` for short) when you start the game.

```
python ants_gui.py --water
```

### Problem 12 (100 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 12 -u
```

Currently there are no ants that can be placed on `Water`. Implement the `ScubaThrower`, which is a subclass of `ThrowerAnt` that is more costly and watersafe, but otherwise identical to its base class. A `ScubaThrower` should not lose its armor when placed in `Water`.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_scuba.gif" height="80px" width="80px" /> | `ScubaThrower` | 6 | 1 |

We have not provided you with a class header. Implement the `ScubaThrower` class from scratch. Give it a class attribute `name` with the value `'Scuba'` (so that the graphics work) and remember to set the class attribute `implemented` with the value `True` (so that you can use it in a game).

After writing code, test your implementation:

```
python ok --local -q 12
```

### Problem 13 (400 pts)

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q 13 -u
```

Finally, implement the `QueenAnt`. The queen is a waterproof `ScubaThrower` that inspires her fellow ants through her bravery. In addition to the standard `ScubaThrower` action, the `QueenAnt` doubles the damage of all the ants behind her each time she performs an action. Once an ant's damage has been doubled, it is *not* doubled again for subsequent turns.

> Note that the reflected damage of a fire ant should not be doubled, only the extra damage it deals when its armor is reduced to 0

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_queen.gif" height="80px" width="80px" /> | `QueenAnt` | 7 | 1 |

However, with great power comes great responsibility. The `QueenAnt` is governed by three special rules:
1. If the queen ever has its armor reduced to 0, the bees win. The bees also still win if any bee reaches the end of a tunnel. You can call `bees_win()` to signal to the simulator that the game is over.
2. There can be only one true queen. Any queen instantiated beyond the first one is an impostor, and should have its armor reduced to 0 upon taking its first action, without doubling any ant's damage or throwing anything. If an impostor dies, the game should still continue as normal.
3. The true (first) queen cannot be removed. Attempts to remove the queen should have no effect (but should not cause an error). You will need to override `Ant.remove_from` in `QueenAnt` to enforce this condition.

Some hints:
- All instances of the same class share the same class attributes. How can you use this information to tell whether a `QueenAnt` instance is the true `QueenAnt`?
- You can find each `Place` in a tunnel behind the `QueenAnt` by starting at the ant's `place.exit` and then repeatedly following its `exit`. The `exit` of a `Place` at the end of a tunnel is `None`.
- To avoid doubling an ant's damage twice, mark the ants that have been buffed in some way, in a way that persists across calls to `QueenAnt.action`.
- When buffing the ants' damage, keep in mind that there can be more than one ant in one place!

After writing code, test your implementation:

```
python ok --local -q 13
```

### Optional Problem (0 pts)

> **Note**: This problem is a bit difficult, so we make it optional. However, we recommend you to try to solve it if you have time because it is fun. You don't have to submit your code for this problem to our OJ website.

Before writing any code, read the instructions and test your understanding of the problem:

```
python ok --local -q OPTIONAL -u
```

Implement two final thrower ants that do zero damage, but instead produce a temporary "effect" on the `action` method of a `Bee` instance that they `throw_at`. This effect is an alternative action that lasts for a certain number of `.action(gamestate)` calls, after which the `Bee`'s action reverts to its previous behavior.

We will be implementing two new ants that subclass `ThrowerAnt`.

- `SlowThrower` throws sticky syrup at a bee, applying a slow effect for 3 turns.
- `ScaryThrower` intimidates a nearby bee, causing it to back away instead of advancing. (If the bee is already right next to the Hive and cannot go back further, it should not move.) The scare effect lasts for 2 turns. *Once a bee has been scared once, it can't be scared again*.

| | Class | Food Cost | Armor |
| - | - | - | - |
| <img src="images/ant_slow.gif" height="80px" width="80px" /> | `SlowThrower` | 4 | 1 |
| <img src="images/ant_scary.gif" height="80px" width="80px" /> | `ScaryThrower` | 6 | 1 |

In order to complete the implementations of these two ants, you will need to set their class attributes appropriately and implement the following three functions:

1. `make_slow` is an effect that takes an `action` method and a `bee`, and returns a new action method that performs the original action on every turn that `gamestate.time` is even and does nothing on other turns.
2. `make_scare` is an effect that takes an `action` method and a `bee`, and returns a new `action` method that makes the bee go backwards.
3. `apply_effect` takes an `effect` (either `make_slow` or `make_scare`), a `Bee`, and a `duration`. The way it works is as so: imagine that a `Bee` has a bunch of effects, each of which modifies `action` in sequence. When an effect's duration is up, it removes itself from the list. `apply_effect` adds the given effect to the end of the list, so that it is applied latest.

> *Hint*: to make a bee go backwards, consider adding an instance variable indicating its current direction. Where should you change the bee's direction? Once the direction is known, how can you modify the `action` method of `Bee` to move appropriately?
>
> *Hint*: You will need to rebind a method in one of the functions. Note that when assigning to an instance, the self parameter isn't bound.
> ```python
> class X: pass
> def f(x): return x ** 3
> x = X()
> x.f = f
> print(x.f(2)) # prints 8
> ```
>
> As an example of what "previous behavior" means, take the example of a bee that has been slowed twice (say by two separate SlowThrowers). It will have the following behavior
>
> - on time 1, it will do nothing. The outer slow has 2 turns to go, the inner one still has 3 turns
> - on time 2, it moves forward. The outer slow has 1 turn to go, the inner one has 2 turns
> - on time 3, it will do nothing. The outer slow has no turns left, the inner one has 2 turns
> - on time 4, it moves forward. The inner slow has 1 turn left
> - on time 5, it does nothing. The inner slow has no turns left

You can run some provided tests, but they are not exhaustive:

```
python ok --local -q OPTIONAL
```

Make sure to test your code! Your code should be able to apply multiple effects on a target; each new effect applies to the current (possibly affected) action method of the bee.

## Conclusion
**You are now done with the project!** If you haven't yet, you should try playing the game!

```
python ants_gui.py [-h] [-d DIFFICULTY] [-w] [--food FOOD]
```

**Acknowledgments to cs61A:** Tom Magrino and Eric Tzeng developed this project with John DeNero. Jessica Wan contributed the original artwork. Joy Jeng and Mark Miyashita invented the queen ant. Many others have contributed to the project as well!

The new concept artwork was drawn by Alana Tran, Andrew Huang, Emilee Chen, Jessie Salas, Jingyi Li, Katherine Xu, Meena Vempaty, Michelle Chang, and Ryan Davis.