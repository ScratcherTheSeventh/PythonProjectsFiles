import random

deck = []
for colour in ['Red', 'Blue', 'Green', 'Yellow']:
    deck.append(f'{colour} 0')
    for number in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'SKIP', 'REVERSE', '+2']:
        for _ in range(2):
            deck.append(f'{colour} {number}')

for power in ['Wild +4', 'Wild']:
    for _ in range(4):
        deck.append(power)

random.shuffle(deck)


aideck = [deck.pop(0) for _ in range(7)]
usrdeck = [deck.pop(0) for _ in range(7)]

top = deck.pop(0).split()

print(f"Select a card to play using its index. Example: if you want to play {usrdeck[0]}, type 1.")

def pick_cards(n):
    return [deck.pop(0) for _ in range(min(n, len(deck)))]

skip_turn = False  

while usrdeck and aideck:
    print("\nYour Hand:", usrdeck)
    print("Top Card:", ' '.join(top))

    if not skip_turn:
        while True:
            playable_cards = [
                card for card in usrdeck if 'Wild' in card or
                (len(card.split()) > 1 and (card.split()[0] == top[0] or (len(top) > 1 and card.split()[1] == top[1])))
            ]

            if playable_cards:
                try:
                    play = int(input("Card Index >>> ")) - 1
                    if play < 0 or play >= len(usrdeck):
                        print("Invalid choice. Pick a valid index.")
                        continue
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                card = usrdeck[play]
                if card not in playable_cards:
                    print("You can't play that card. Choose a valid card.")
                    continue
                
                usrdeck.pop(play)
                playraw = card.split() # 0th: Colour, 1th: number

                if 'Wild' in card:
                    if '+4' in card:
                        aideck.extend(pick_cards(4)) # red => Red
                    while True:
                        colour = input("Choose a color (Red, Yellow, Green, Blue) >>> ").title()
                        if colour in ['Red', 'Yellow', 'Green', 'Blue']:
                            top = [colour]
                            print(f"Color changed to {colour}.")
                            break
                        else:
                            print("Invalid color choice.")
                else:
                    if '+2' in card:
                        aideck.extend(pick_cards(2))
                    top = playraw

                if 'SKIP' in card or 'REVERSE' in card:
                    print("AI's turn is skipped!")
                    skip_turn = True  
                break
            else:
                print("No valid cards. Drawing a card...")
                new_card = pick_cards(1)
                if new_card:
                    usrdeck.append(new_card[0])
                    print(f"You drew: {new_card[0]}")
                else:
                    print("No more cards to draw. Turn skipped.")
                break

    skip_turn = False
# AI TURN
    print("\nAI's turn:")
    if not skip_turn:
        ai_played = False
        for i, card in enumerate(aideck):
            playraw = card.split()
            if 'Wild' in card or playraw[0] == top[0] or (len(playraw) > 1 and len(top) > 1 and playraw[1] == top[1]):
                ai_played = True
                print(f"AI played: {card}")  
                aideck.pop(i)
                top = playraw

                if 'Wild' in card:
                    new_colour = random.choice(['Red', 'Blue', 'Green', 'Yellow'])
                    print(f"AI chose the color {new_colour}.")
                    top = [new_colour]

                if '+4' in card:
                    print("AI played a +4! You must draw 4 cards.")
                    usrdeck.extend(pick_cards(4))  
                elif '+2' in card:
                    print("AI played a +2! You must draw 2 cards.")
                    usrdeck.extend(pick_cards(2))  
                elif 'SKIP' in card or 'REVERSE' in card:
                    print("AI played a SKIP! Your turn is skipped.")
                    skip_turn = True  
                break
        
        if not ai_played:
            print("AI has no playable cards. Drawing one card...")
            drawn_card = pick_cards(1)
            if drawn_card:
                aideck.append(drawn_card[0])
                print(f"AI drew: {drawn_card[0]}")
                playraw = drawn_card[0].split()
                if 'Wild' in drawn_card[0] or playraw[0] == top[0] or (len(playraw) > 1 and len(top) > 1 and playraw[1] == top[1]):
                    print(f"AI immediately plays the drawn card: {drawn_card[0]}")
                    aideck.pop()
                    top = playraw

                    if 'Wild' in drawn_card[0]:
                        new_colour = random.choice(['Red', 'Blue', 'Green', 'Yellow'])
                        print(f"AI chose the color {new_colour}.")
                        top = [new_colour]

                    if '+4' in drawn_card[0]:
                        print("AI played a +4! You must draw 4 cards.")
                        usrdeck.extend(pick_cards(4))  
                    elif '+2' in drawn_card[0]:
                        print("AI played a +2! You must draw 2 cards.")
                        usrdeck.extend(pick_cards(2))  
                    elif 'SKIP' in drawn_card[0] or 'REVERSE' in drawn_card[0]:
                        print("AI played a SKIP! Your turn is skipped.")
                        skip_turn = True  
            else:
                print("AI couldn't draw a card. Turn skipped.")

    if not usrdeck:
        print("You won!")
        break
    if not aideck:
        print("AI won!")
        break
