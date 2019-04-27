import pygame
from scene import *

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


class TitleScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.count = 0
	
	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				print('Mouse position: ' + str(mouse_pos))
				print('play: ' + str(self.btn_play))
				if(point_isinside(mouse_pos[0], mouse_pos[1], self.btn_play)):
					print('You clicked Play button!')
					self.SwitchToScene(GameScene())
				if(point_isinside(mouse_pos[0], mouse_pos[1], self.btn_rules)):
					print('You clicked Rules button!')
				# Move to the next scene when the user pressed Enter

	def Load(self):
		pass
	
	def Update(self):
		pass
	
	def Render(self, screen):
		screen.fill((40, 40, 40))
		self.btn_play = create_button(screen, 'Play', 250, 100, 225, 55)
		self.btn_rules = create_button(screen, 'Rules', 250, 200, 225, 55)


class GameScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
	
	def ProcessInput(self, events, pressed_keys):
		pass
		
	def Update(self):
		pass
	
	def Render(self, screen):
		# The game scene is just a blank blue screen 
		screen.fill((0, 0, 255))


def create_button(screen, text, x, y, width, height, font = None):
	# A little hard coded but yeah
	if font == None:
		font = pygame.font.Font(None, 34)
	button_text = font.render(text, True, (170, 170, 170))
	pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(x, y, width, height))
	screen.blit(button_text, ((x + 100) - button_text.get_width() // 2,  (y + 25) - button_text.get_height() // 2))
	# returns bottom-left of rectangle and top right
	return (x, y+height, x + width, y)

def point_isinside(x, y, rect) :
	x1 = rect[0]
	y1 = rect[1]
	x2 = rect[2]
	y2 = rect[3]
	# bottom left: (x1, y1)
	# top right: (x2, y2)
	# Point: (x, y)
	if (x > x1 and x < x2 and y < y1 and y > y2): 
		return True
	else: 
		return False


run_game(680, 680, 60, TitleScene())