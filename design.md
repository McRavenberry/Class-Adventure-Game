# Love and Legends
By Mr. McGarrah's 7th Period Programming Class
2022

## Synopsis
Your family is cursed.  Every member of your family has to find true love or become a living legend before the age of 21, or be forced to live forever as a hideous monster.

As you move through the world, you will encounter random enemies.  There will be potential love interests you will have to fulfill requests for in order to gain favor.  There will be dungeons full of bad guys the player will need to defeat too.  Every action and choice brings the player closer to fulfilling the curse.  Only true love or becoming a living legend will lift the curse.

Will you be able to find true love or become a living legend?  Or is it already too late and your fate is sealed?  Or, maybe, you are the one who can finally break the family curse for good by become the first person to find true love AND become a living legend before the curse takes hold.

## How to Win
You win the game when you find true love.  

OR

after you gain enough fame points to become a living legend.

BUT

Can you achieve both before your 21st birthday and break the family curse for good?

## How to Lose
The player loses the game when he/she runs out of time and the curse takes hold.

## Core Game Loop
The player navigates the world looking for an adventure and love.  Along the way, the player will have random encounters with small enemies.  The player will choose to battle or attempt to escape.

The player will have encounters with love interests, each with different wants/needs.  Obtain enough favor with one of these people in order to find true love.  Each failed love encounter will leave you broken hearted.  It will take you time to get over the broken heart before you can move on.

With each enemy defeated, your reputation spreads.  Too much damage during battle will cause you to lose precious time to heal.

You will either lift the curse by finding true love or becoming a living legend, or you will be cursed to become a hideous monster.  Whatever the result, your name will be added to the cumulative family history that tracks each playthrough, including the name and result of each attempt.  The game is not officially defeated until you find true love and become a living legend before the age of 21.

## Perks
You have no perks on a new playthrough or if you failed to lift the curse.

If you find true love, on your next playthrough you will start with 20 favor points with a random love interest on the map.

If you become a living legend, the weapon you had becomes a family heirloom that you pass on to your next playthrough.

## Key Systems
- Time System
- Battle System
- Love System
- Shop System
- Health System
- Inventory System

## Time System
- There are 200 days left before you turn 21 and the curse takes hold.  
- Each battle, love interaction, or travel between encounters reduces the time by 1 day.
- A defeat in battle sends you to the hospital for 5-10 days.
- A dungeon will take 3-5 days to complete.
- A defeat against the boss dragon ends the game.
- A failed love encounter takes 5-10 days to recover from a broken heart. 

## Battle System Description
Gain 1 fame for every enemy defeated.  Gain 10 for every dungeon defeated.  Get instant 100 fame for defeating the dragon.

### Random Encounters
There are battles with random enemies as you travel around the map.  Battle is turn based.  You can either choose to attack, defend, or escape.  There is no chance to heal during battle.  If you lose during battle, you faint and travel to the hospital to recover.

### Dungeons
These battles are quests from the king.  You will be given a series of back to back to back battles, varying from 3-5 battles in a row.  You are able to carry up to three potions into battle, but you can only heal between battles.  Failure to complete a dungeon quest will result in a loss of 10 fame.

### Boss Battle
This battle is virtually impossible to win, but it might be your only chance to lift the curse before time runs out.  Slay the dragon and be instantly granted legendary status.  Fail, and you seal your fate to become a hideous monster.  Unlike other battles, you may use a potion during a boss battle.

## Love System Description
Various love interests are scattered around the map.  Each one has their own way to gain favor.  Which love interest you chose is up to you.

- One likes gifts
- One likes spending time together
- One likes the heads of monsters
- etc

Collect 100 favor points for one of them to fall in love with you.

## Shop System Description
The shop sells two weapons, two gifts, and one health potion at any given time.
- Weapons
    - Weapons have random names, damage, and price
- Gifts
    - Gift items are random, but will gain you favor with different love interests depending on what they are
- Health potions

The shop only hold five items at a time.  After a purchase is made, the item slot will be placed with a new item on the next visit.  Every 14 days, all of the items in the shop will be swapped out.

If you purchase anything from the shop, it takes a day off of your time.

## Health System Description
You have 100 health.  It cannot go higher than 100.  If it goes to zero, you faint and have to go to the hospital for 5-10 days to recover.

A health potion will heal you up to 50 health points.

If you rest at a hotel, it will heal you 25-50 points per day.

## Inventory System Description
You can have up to the following quantities in your inventory, but no more than five total items:
- two weapons
- two gifts
- three health potions