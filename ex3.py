import pygame
import random
import time



# Function to calculate hand value
def hand_value(hand):
    value = 0
    aces = 0
    for rank, _ in hand:
        if rank > 10:
            value += 10
        elif rank == 1:
            value += 11
            aces += 1
        else:
            value += rank
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Function to draw text
def draw_text(text, pos, font, screen, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)


def pex3():

    # Initial money and bet
    money = 1000
    bet = 100
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blackjack (H=Hit S=Stand)")

    # Colors
    GREEN = (0, 128, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Load card images
    CARD_WIDTH, CARD_HEIGHT = 100, 150
    card_back = pygame.image.load('Cards/table.png')
    card_back = pygame.transform.scale(card_back, (CARD_WIDTH, CARD_HEIGHT))

    # Load deck of cards (simplified for example)
    deck = []
    for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
        for rank in range(1, 14):
            card_image = pygame.image.load(f'Cards/{rank}_of_{suit}.png')
            card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
            deck.append((rank, card_image))

    # Shuffle deck
    random.shuffle(deck)

    # Font
    font = pygame.font.Font(None, 36)
    deck = deck if len(deck) > 10 else [card for _ in range(4) for card in deck]
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    game_over = False
    winner_text = ""
    # Game loop
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_h:  # Hit
                    player_hand.append(deck.pop())
                    if hand_value(player_hand) > 21:
                        game_over = True
                elif event.key == pygame.K_s:  # Stand
                    while hand_value(dealer_hand) < 17:
                        dealer_hand.append(deck.pop())
                    game_over = True

        if game_over:
            player_value = hand_value(player_hand)
            dealer_value = hand_value(dealer_hand)
            if player_value > 21:
                winner_text = 'Player Busts! Dealer Wins!'
                money -= bet
            elif dealer_value > 21 or player_value > dealer_value:
                winner_text = 'Player Wins!'
                money += bet
            elif player_value < dealer_value:
                winner_text = 'Dealer Wins!'
                money -= bet
            else:
                winner_text = 'Push!'

        # Clear screen
        screen.fill(GREEN)

        # Draw hands
        for i, (rank, card_image) in enumerate(player_hand):
            screen.blit(card_image, (50 + i * 110, HEIGHT - CARD_HEIGHT - 20))
        for i, (rank, card_image) in enumerate(dealer_hand):
            if i == 0 and not game_over:
                screen.blit(card_back, (50 + i * 110, 20))
            else:
                screen.blit(card_image, (50 + i * 110, 20))

        # Draw hand values
        draw_text(f'Player: {hand_value(player_hand)}', (50, HEIGHT - CARD_HEIGHT - 70), font, screen)
        draw_text(f'Dealer: {hand_value(dealer_hand) if game_over else "?"}', (50, 200), font, screen)

        # Draw money and bet
        draw_text(f'Doblers: {money}€', (WIDTH - 200, HEIGHT - 50), font, screen)
        draw_text(f'Aposta: {bet}€', (WIDTH - 200, HEIGHT - 100), font, screen)

        if game_over:
            draw_text(winner_text, (350, HEIGHT // 2), font, screen)
            pygame.display.flip()
            time.sleep(2)  # Mostra el resultat durant 2 segons
            pex3()  # Comença una partida nova

        pygame.display.flip()

    pygame.quit()