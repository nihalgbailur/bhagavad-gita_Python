import random

quotes = [("You have the right to work, but never to the fruit of the work.", "Chapter 2, Verse 47"),
          ("One who has control over the mind is tranquil in heat and cold, in pleasure and pain, and in honor and dishonor.", "Chapter 6, Verse 7"),
          ("The self-controlled soul, who moves amongst sense objects, free from either attachment or repulsion, he wins eternal Peace.", "Chapter 2, Verse 64"),
          ("The embodied soul is eternal in existence, indestructible, and infinite, only the material body is factually perishable.", "Chapter 2, Verse 18"),
          ("The wise see that there is action in the midst of inaction and inaction in the midst of action.", "Chapter 4, Verse 18")]

random_quote = random.choice(quotes)
print(random_quote[0])
print("-" + random_quote[1])
