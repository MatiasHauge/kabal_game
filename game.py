import pygame
import sys, os

pygame.init()
pygame.font.init()

WIN_WIDTH, WIN_HEIGHT = 1180, 880
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("The Kabal Game")

# Frames per second
FPS = 60

# COLORS
WHITE_COL = (255, 255, 255)
GREEN_ONE_COL = (0, 157, 0)

# Fonts
STAND_FONT = pygame.font.SysFont('Arial-bold', 20)

# The four cards holders and its variables
right_padding = 20
left_padding = 50
y_padding = 100
card_width, card_height = 100, 180

hearts_card_holder = pygame.Rect(left_padding, y_padding, card_width, card_height)
clubs_card_holder = pygame.Rect(hearts_card_holder.right + right_padding, y_padding, card_width, card_height)
diamonds_card_holder = pygame.Rect(clubs_card_holder.right + right_padding, y_padding, card_width, card_height)
spades_card_holder = pygame.Rect(diamonds_card_holder.right + right_padding, y_padding, card_width, card_height)

# Heart image
ace_heart_image = pygame.image.load(os.path.join('assets', 'ace_hearth.png'))
ace_heart = pygame.transform.scale(ace_heart_image, (card_width, card_height))

# Clubs image
ace_clubs_image = pygame.image.load(os.path.join('assets', 'ace_clubs.png'))
ace_clubs = pygame.transform.scale(ace_clubs_image, (card_width, card_height))

# Diamond image
ace_diamond_image = pygame.image.load(os.path.join('assets', 'ace_hearth.png'))
ace_diamond = pygame.transform.scale(ace_diamond_image, (card_width, card_height))

# Spades image
ace_spades_image = pygame.image.load(os.path.join('assets', 'ace_spades.png'))
ace_spades = pygame.transform.scale(ace_spades_image, (card_width, card_height))

session_score = 0

def draw_main_win():

    WIN.fill(GREEN_ONE_COL)

    # The cards
    ace_heart_card = pygame.Rect(hearts_card_holder.x, hearts_card_holder.y, card_width, card_height)
    ace_clubs_card = pygame.Rect(clubs_card_holder.x, clubs_card_holder.y, card_width, card_height)
    ace_diamond_card = pygame.Rect(diamonds_card_holder.x, diamonds_card_holder.y, card_width, card_height)
    ace_spades_card = pygame.Rect(spades_card_holder.x, spades_card_holder.y, card_width, card_height)

    draw_ace_card(ace_heart_card, ace_clubs_card, ace_diamond_card, ace_spades_card)

    # Score text
    score_text = STAND_FONT.render(f"Score: {session_score}", 1, WHITE_COL)
    WIN.blit(score_text, (WIN_WIDTH / 2, 20))

    pygame.display.update()

def draw_ace_card(ace_heart_card, ace_clubs_card, ace_diamond_card, ace_spades_card):

    # Drawing the cards onto the windows surface
    # Hearts
    pygame.draw.rect(WIN, WHITE_COL, hearts_card_holder)
    WIN.blit(ace_heart, (ace_heart_card.x, ace_heart_card.y))

    # Clubs
    pygame.draw.rect(WIN, WHITE_COL, clubs_card_holder)
    WIN.blit(ace_clubs, (ace_clubs_card.x, ace_clubs_card.y))

    # Diamonds
    pygame.draw.rect(WIN, WHITE_COL, diamonds_card_holder)
    WIN.blit(ace_diamond, (ace_diamond_card.x, ace_diamond_card.y))

    # Spades
    pygame.draw.rect(WIN, WHITE_COL, spades_card_holder)
    WIN.blit(ace_spades, (ace_spades_card.x, ace_spades_card.y))

def ace_cards_movement():
    pass

def draw_regular_cards():
    # Antall cards in each catagory
    num_of_cards = 13

    all_hearts_cards = []
    all_clubs_cards = []
    all_diamonds_cards = []
    all_spades_cards = []

    for hearts in range(0, num_of_cards):
        all_hearts_cards.append(hearts)
        # Figure how to implement each card of hearts the proper way

    for clubs in range(0, num_of_cards):
        all_clubs_cards.append(all_clubs_cards)

    for diamonds in range(0, num_of_cards):
        all_diamonds_cards.append(diamonds)

    for spades in range(0, num_of_cards):
        all_spades_cards.append(spades)

def main_loop():

    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Figure out a way to make cards be dragged with mouse
                    pass

        #mouse_moved = pygame.mouse.get_pressed()

        clock.tick(FPS)
        draw_main_win()
        ace_cards_movement()

if __name__ == '__main__':

    main_loop()