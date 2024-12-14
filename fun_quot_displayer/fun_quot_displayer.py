#!/usr/bin/python3

import random
from colorama import Fore as f, Style as s

quotes = [
	"Keep going! You’re halfway to almost giving up!",
	"Don't worry if plan A fails, there are 25 more letters in the alphabet!",
	"If at first you don’t succeed, skydiving is not for you.",
	"Dream big! Unless your dreams are silly, then just dream moderately.",
	"The elevator to success is out of order. You'll have to use the stairs, one step at a time.",
	"You miss 100% of the naps you don’t take.",
	"If you think nobody cares if you’re alive, try missing a couple of car payments.",
	"Be yourself; everyone else is already taken, and probably not as funny.",
	"I find television very educational. Every time someone turns it on, I go read a book.",
	"People say nothing is impossible, but I do nothing every day.",
	"Keep calm and carry a wand.",
    "I'm on a seafood diet. I see food, and I eat it.",
    "I am not lazy, I am on energy saving mode.",
    "Money can't buy happiness, but it can buy ice cream and that's kind of the same thing.",
    "I'm not arguing, I'm just explaining why I'm right.",
    "My wallet is like an onion, opening it makes me cry.",
    "I told my wife she should embrace her mistakes... she hugged me.",
    "If you think nobody cares if you're alive, try missing a couple of car payments.",
    "Behind every great man is a woman rolling her eyes.",
    "I always wanted to be somebody, but now I realize I should have been more specific.",
    "Age is something that doesn’t matter, unless you are a cheese.",
    "I’m not insane. My mother had me tested.",
	"The Big Bang Theory.",
    "To steal ideas from one person is plagiarism; to steal from many is research.",
    "I used to think I was indecisive, but now I'm not too sure.",
    "Cleaning up is just putting stuff in less obvious places.",
    "The early bird might get the worm, but the second mouse gets the cheese.",
	"I am glad I will not be young in a future without wilderness.",
	"Nature is cheaper than therapy.",
	"I go to nature to be soothed and healed, and to have my senses put in order.",
	"If you think you are too small to make a difference, try sleeping with a mosquito.",
	"Mother Nature is not sweet.",
	"An optimist is a person who sees a green light everywhere, while a pessimist sees only the stoplight... the truly wise person is colorblind.",
	"A weed is a plant that has mastered every survival skill except for learning how to grow in rows.",
	"Mother Nature's not too kind to stupidity.",
	"Nature abhors a vacuum, and so do I.",
	"Trees that are slow to grow bear the best fruit.",
	"In some mysterious way woods have never seemed to me to be static things. In physical terms, I move through them; yet in metaphysical ones, they seem to move through me.",
	"I like the outdoors. I like to hike, I like to fish, I like to shoot things. But camping? As far as I'm concerned, 'roughing it' means staying at a hotel without room service.",
	"Mosquitoes remind us that we are not as high up on the food chain as we think.",
	"There's always a moment in the woods when you feel like you're being watched by an onion ring.",
	"The best way to observe a fish is to become a fish.",
	"I like work; it fascinates me. I can sit and look at it for hours.", 
	"The best way to appreciate your job is to imagine yourself without one.",
	"I always arrive late at the office, but I make up for it by leaving early.",
	"Hard work never killed anybody, but why take a chance?",
	"Work is the greatest thing in the world. So we should always save some of it for tomorrow.",
	"People who never do any more than they get paid for, never get paid for any more than they do.",
	"I am a friend of the workingman, and I would rather be his friend than be one.",
	"Doing nothing is very hard to do… you never know when you're finished.", 
	"The only thing that ever sat its way to success was a hen.",
	"No man goes before his time—unless the boss leaves early.",
	"Work until your bank account looks like a phone number.",
	"I’m not running away from hard work, I’m too lazy to run.",
	"My keyboard must be broken, I keep hitting the escape key, but I’m still at work.",
	"I love deadlines. I love the whooshing noise they make as they go by.", 
	"Monday is a great for becoming too busy to die.", 
]

faces = [
	"( ͡° ͜ʖ ͡°)",
	"( ͡ᵔ ͜ʖ ͡ᵔ )",
	"( ° ͜ʖ °)",
	"( ͝° ͜ʖ͡°)",
]

fg_colors = [
	f.LIGHTMAGENTA_EX, 
	f.LIGHTGREEN_EX,
	f.LIGHTYELLOW_EX,
]

print(s.BRIGHT + random.choice(fg_colors) + f"\n  {random.choice(faces)}  {random.choice(quotes)}\n")
