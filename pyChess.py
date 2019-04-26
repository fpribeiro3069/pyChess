import pygame

def main():
	pygame.init()
	screen = pygame.display.set_mode((680, 680))
	done = False

	pieces = load_pieces()

	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		draw_board(screen)

		screen.blit(pieces['black_rook'], (0, 0))

		pygame.display.flip()
		clock.tick(60)


def draw_board(screen):
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	x = 0;
	y = 0;
	for line in range(8):
		for column in range(8):
			pygame.draw.rect(screen, WHITE if ((line + column + 1) % 2 == 0) else BLACK, pygame.Rect(x, y, 85, 85))
			x += 85
		x = 0
		y += 85


def load_pieces():
	pieces = {}
	path = 'images/'
	file_type = '.png'
	string = 'white_'
	for i in range(2):
		pieces[string + 'king'] = pygame.image.load(path + string + 'king' + file_type)
		pieces[string + 'queen'] = pygame.image.load(path + string + 'queen' + file_type)
		pieces[string + 'bishop'] = pygame.image.load(path + string + 'bishop' + file_type)
		pieces[string + 'knight'] = pygame.image.load(path + string + 'knight' + file_type)
		pieces[string + 'rook'] = pygame.image.load(path + string + 'rook' + file_type)
		pieces[string + 'pawn'] = pygame.image.load(path + string + 'pawn' + file_type)
		string = 'black_'
	return pieces


if __name__ == '__main__':
	main()