import pygame
import sys

morse_tab = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',

    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',

    '..--..': '?',
    '-.-.--': '!',
    '.-.-.-': '.',
    '--..--': ',',
    '-.-.-.': ';',
    '---...': ':',
    '.-.-.': '+',
    '-....-': '-',
    '-..-.': '/',
    '-...-': '='
}

def morse_to_ascii( morse ):
    words = morse.split( ' ' )
    ascii_text = ''
    for word in words:
        if word in morse_tab:
            ascii_text += morse_tab[ word ]
    return ascii_text

if __name__ == "__main__":
    pygame.init()

    WIDTH, HEIGHT = 800, 800
    WHITE = ( 255, 255, 255 )
    BLACK = ( 0, 0, 0 )
    FONT_SIZE = 32

    button_rect = pygame.Rect( 200, 200, 400, 200 )
    button_font = pygame.font.Font( None, FONT_SIZE )
    button_text = 'Press'

    output_rect = pygame.Rect( 200, 400, 400, 50 )
    output_font = pygame.font.Font( None, FONT_SIZE )
    output_text = ''

    ascii_rect = pygame.Rect( 200, 600, 400, 50 )
    ascii_font = pygame.font.Font( None, FONT_SIZE )
    ascii_text = ''

    SHORT_PRESS_TIME = 10
    LONG_PRESS_TIME = 200
    INACTIVITY_TIME = 3000

    button_pressed_time = 0
    is_button_pressed = False
    last_activity_time = pygame.time.get_ticks()
    morse_input = ''

    window = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
    pygame.display.set_caption( "Morse code reader" )

    running = True
    while running:
        window.fill( WHITE )
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint( event.pos ):
                    is_button_pressed = True
                    button_pressed_time = current_time
                    last_activity_time = current_time
            elif event.type == pygame.MOUSEBUTTONUP:
                if is_button_pressed:
                    if button_rect.collidepoint( event.pos ):
                        if current_time - button_pressed_time > LONG_PRESS_TIME:
                            morse_input += '-'
                        else:
                            morse_input += '.'
                    is_button_pressed = False
                    last_activity_time = current_time

        if current_time - last_activity_time > INACTIVITY_TIME:
            if output_text:
                ascii_text += morse_to_ascii( output_text )
                output_text = ''
            else:
                ascii_text += ' '
            last_activity_time = current_time

        if morse_input == ' ':
            ascii_text += morse_to_ascii( output_text )
            output_text = ''
        elif morse_input:
            output_text += morse_input
            morse_input = ''

        pygame.draw.rect( window, BLACK, button_rect, 2 )
        button_surface = button_font.render( button_text, True, BLACK )
        button_text_rect = button_surface.get_rect( center = button_rect.center )
        window.blit( button_surface, button_text_rect )

        pygame.draw.rect( window, BLACK, output_rect, 2 )
        output_surface = output_font.render( output_text, True, BLACK )
        output_text_rect = output_surface.get_rect( center = output_rect.center )
        window.blit( output_surface, output_text_rect )

        pygame.draw.rect( window, BLACK, ascii_rect, 2 )
        ascii_surface = ascii_font.render( ascii_text, True, BLACK )
        ascii_text_rect = ascii_surface.get_rect( center = ascii_rect.center )
        window.blit( ascii_surface, ascii_text_rect )

        pygame.display.flip()

    pygame.quit()
    sys.exit()