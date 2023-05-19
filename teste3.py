import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Definindo as dimensões da janela do jogo
LARGURA_JANELA = 800
ALTURA_JANELA = 600

# Inicializando a janela do jogo
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Quiz Multidisciplinar")


fonte = pygame.font.Font("Visual/font.ttf",16)

perguntas = [
    {
        "pergunta": "Qual é o maior animal terrestre?",
        "opcoes": ["Elefante", "Girafa", "Rinoceronte", "Hipopótamo"],
        "resposta_correta": 0
    },
    {
        "pergunta": "Qual é o maior animal marinho?",
        "opcoes": ["Tubarão-baleia", "Baleia-azul", "Polvo-gigante", "Golfinho"],
        "resposta_correta": 1
    },
    {
        "pergunta": "Quantas pernas um inseto possui?",
        "opcoes": ["2", "4", "6", "8"],
        "resposta_correta": 2
    },
    {
        "pergunta": "Qual é o maior felino do mundo?",
        "opcoes": ["Leão", "Tigre", "Onça-pintada", "Leopardo"],
        "resposta_correta": 1
    }
]

# Variáveis do jogo
pergunta_atual = 0
pontuacao = 0
exibir_pontuacao_final = False


def desenhar_texto(texto, x, y, cor):
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x, y)
    janela.blit(texto_surface, texto_rect)


def desenhar_botoes(opcoes):
    largura_botao = 300
    altura_botao = 50
    x = (LARGURA_JANELA - largura_botao) // 2
    y_base = ALTURA_JANELA // 2 - 40
    espacamento_vertical = 80

    for i, opcao in enumerate(opcoes):
        retangulo_botao = pygame.Rect(x, y_base + (i * espacamento_vertical), largura_botao, altura_botao)
        pygame.draw.rect(janela, BRANCO, retangulo_botao)
        desenhar_texto(opcao, x + largura_botao // 2, y_base + (i * espacamento_vertical) + altura_botao // 2, PRETO)
        if retangulo_botao.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(janela, VERDE, retangulo_botao, 3)
        else:
            pygame.draw.rect(janela, PRETO, retangulo_botao, 3)

# Loop principal do jogo
rodando = True
tentar_novamente = False

while rodando:
    janela.fill(PRETO)

    # Verifica os eventos do Pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if exibir_pontuacao_final:
                if retangulo_botao_tentar_novamente.collidepoint(pygame.mouse.get_pos()):
                    tentar_novamente = True
            else:
                # Verifica se algum botão foi pressionado
                opcoes = perguntas[pergunta_atual]["opcoes"]
                for i, opcao in enumerate(opcoes):
                    retangulo_botao = pygame.Rect(
                        (LARGURA_JANELA - 300) // 2,
                        ALTURA_JANELA // 2 - 40 + (i * 80),
                        300,
                        50
                    )
                    if retangulo_botao.collidepoint(pygame.mouse.get_pos()):
                        if i == perguntas[pergunta_atual]["resposta_correta"]:
                            pontuacao += 1

                        pergunta_atual += 1

                        if pergunta_atual >= len(perguntas):
                            exibir_pontuacao_final = True

    if exibir_pontuacao_final:
        janela.fill(PRETO)
        desenhar_texto("Pontuação Final: {}".format(pontuacao), LARGURA_JANELA // 2, ALTURA_JANELA // 2 - 40, BRANCO)

        retangulo_botao_tentar_novamente = pygame.Rect(
            (LARGURA_JANELA - 300) // 2,
            ALTURA_JANELA // 2 + 100,
            300,
            50
        )
        pygame.draw.rect(janela, BRANCO, retangulo_botao_tentar_novamente)
        desenhar_texto("Tentar Novamente", LARGURA_JANELA // 2, ALTURA_JANELA // 2 + 125, PRETO)
        if retangulo_botao_tentar_novamente.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(janela, VERDE, retangulo_botao_tentar_novamente, 3)
        else:
            pygame.draw.rect(janela, PRETO, retangulo_botao_tentar_novamente, 3)

        if tentar_novamente:
            # Reinicia as variáveis do jogo
            pergunta_atual = 0
            pontuacao = 0
            exibir_pontuacao_final = False
            tentar_novamente = False

    else:
        desenhar_texto(perguntas[pergunta_atual]["pergunta"], LARGURA_JANELA // 2, 100, BRANCO)

        # Desenha os botões de resposta
        desenhar_botoes(perguntas[pergunta_atual]["opcoes"])

        # Desenha a pontuação
        desenhar_texto("Pontuação: {}".format(pontuacao), LARGURA_JANELA - 100, 20, BRANCO)

    # Desenha o botão de sair
    retangulo_botao_sair = pygame.Rect(20, 20, 100, 50)
    pygame.draw.rect(janela, BRANCO, retangulo_botao_sair)
    desenhar_texto("Sair", 70, 45, PRETO)
    if retangulo_botao_sair.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(janela, VERMELHO, retangulo_botao_sair, 3)
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
    else:
        pygame.draw.rect(janela, PRETO, retangulo_botao_sair, 3)

    # Atualiza a tela
    pygame.display.flip()


pygame.quit()
sys.exit()
