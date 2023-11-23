import pygame

# 初始化pygame
pygame.init()

# 設定視窗的大小及標題
width, height = 1024, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('逃出天文鎖-系外行星與你的距離')

# 設定顏色
WHITE = '#FFFFFF'
GOLD = '#FFD700'

# 設定背景圖片
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (width, height))

# 設定字型
font_path = './NotoSansTC-Black.ttf'
title_font = pygame.font.Font(font_path, 60)
subtitle_font = pygame.font.Font(font_path, 30)
author_font = pygame.font.Font(font_path, 24)

# 設定首頁的主標題、副標題和作者資訊
title = title_font.render('逃出天文鎖-系外行星與你的距離', True, GOLD)
subtitle = subtitle_font.render('為了逃脫《天文鎖》密室，請你解開系外行星與你的距離', True, GOLD)
author_info = author_font.render('由astrobackhacker.tw製作', True, GOLD)

# 設定進入密室按鈕
button_color = '#D32F2F'
button_rect = pygame.Rect(width // 2 - 100, height // 3 + 50, 200, 50)
button_text = subtitle_font.render('進入密室', True, WHITE)

# 遊戲主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # 這裡放入進入遊戲的程式碼
                print('按鈕被點擊')
    
    # 放置背景圖
    screen.blit(background, (0, 0))
    
    # 放置主標題、副標題和作者資訊
    screen.blit(title, (width // 2 - title.get_width() // 2, height // 6 - 15))
    screen.blit(subtitle, (width // 2 - subtitle.get_width() // 2, height // 6 + 60))
    screen.blit(author_info, (width // 2 - author_info.get_width() // 2, height - 35))
    
    # 放置按鈕
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2, button_rect.y + (button_rect.height - button_text.get_height()) // 2))
    
    # 更新畫面
    pygame.display.flip()

# 關閉pygame程式結束遊戲主循環
pygame.quit()
