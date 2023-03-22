import random

#Lista dos caracteres do Coreano
caracteres = ['가', '각', '간', '감', '갑', '값', '강', '같', '개', '거', '건', '걷', '검', '겁', '것', '게', '겨', '격', '견', '경', '계', '고', '곤', '곧', '곱', '곳', '공', '과', '관', '교', '구', '국', '굴', '권', '귀', '그', '극', '금', '급', '기', '길', '꺼', '꼬', '꽃', '꽤', '꾸', '끄', '끔', '끝', '나', '난', '날', '낡', '남', '낮', '내', '냄', '냉', '너', '넘', '네', '넷', '녁', '년', '노', '녹', '놀', '농', '놓', '누', '눈', '눕', '느', '늘', '늙', '능', '늦', '니', '님', '다', '닫', '달', '닭', '담', '답', '당', '대', '더', '덕', '던', '덟', '덥', '도', '독', '돈', '돕', '동', '돼', '되', '두', '둘', '뒤', '드', '듣', '들', '등', '딱', '딸', '땅', '때', '떠', '똑', '뚱', '라', '락', '람', '래', '럭', '럽', '레', '력', '렵', '로', '롭', '료', '루', '류', '르', '른', '름', '리', '립', '마', '막', '만', '많', '말', '맛', '맞', '매', '맵', '머', '먹', '멀', '명', '몇', '모', '목', '몸', '못', '무', '문', '물', '미', '밀', '밑', '바', '박', '반', '받', '발', '밤', '방', '배', '백', '버', '번', '벗', '벽', '볍', '병', '보', '복', '본', '봄', '부', '북', '분', '불', '비', '빠', '빨', '빵', '쁘', '사', '삭', '살', '삼', '상', '새', '색', '생', '서', '선', '섯', '성', '세', '셋', '소', '속', '손', '송', '수', '숙', '숨', '쉬', '쉰', '쉽', '스', '슬', '습', '슷', '시', '식', '신', '실', '싫', '심', '십', '싶', '싸', '썹', '쓰', '씨', '아', '악', '안', '앉', '알', '앞', '야', '약', '얇', '양', '어', '억', '언', '얼', '업', '에', '여', '역', '연', '열', '엽', '영', '옆', '오', '온', '올', '옷', '완', '외', '요', '우', '운', '울', '웃', '원', '월', '위', '유', '육', '은', '을', '음', '의', '이', '익', '인', '일', '읽', '잃', '입', '있', '잊', '자', '작', '잔', '잘', '잠', '잡', '장', '재', '저', '적', '전', '젊', '점', '정', '제', '젯', '존', '종', '좋', '죄', '주', '죽', '준', '중', '쥐', '즉', '즘', '증', '지', '직', '진', '질', '집', '짓', '짜', '째', '쪽', '찍', '차', '착', '창', '찾', '채', '책', '처', '천', '철', '첫', '청', '체', '초', '촌', '추', '축', '출', '춤', '춥', '층', '치', '친', '칠', '침', '카', '캐', '커', '컴', '케', '켜', '콩', '크', '타', '탁', '택', '터', '털', '텔', '토', '통', '투', '트', '튼', '틀', '파', '판', '팔', '펜', '편', '평', '포', '풀', '퓨', '프', '피', '하', '학', '한', '할', '함', '항', '해', '행', '험', '현', '형', '호', '혼', '홉', '화', '활', '황', '회', '획', '후', '흔', '흘', '흥', '흰', '히']

#Escolha do tema do caça-palavras
tema  = input("Os temas disponiveis são comidas, compras, escola, tempo, transporte. Escolha um e digite o nome dele:")
with open(f'palavras\{tema}.txt','r', encoding="utf-8") as f:
    lista = [line[:-1] for line in f]

#Escolha do tamanho do caça-palavras
tam = int(input("Digite o tamanho do caça palavra( entre 9 e 25):"))
palavras = random.sample(lista,tam+1)

#criação do tabuleiro
tabuleiro = [["_ " for _ in range(tam)] for _ in range(tam)]

#Função de impressão do tabuleiro
def printgrid():
    for i in range(tam):
        print( ' '.join(tabuleiro[i]))

#Escolher a diração e posição
def fit(tam, tam_pal):
    while True:
        direc = random.choice(orient)
        if direc == 'horiz':
            x = 1
            y = 0
        if direc == 'vert':
            x = 0
            y = 1
        if direc == 'diagcima':
            x = 1
            y = 1
        if direc == 'diagbaixo':
            x = 1
            y = -1

        x_in = random.randint(0,tam-1)  
        y_in = random.randint(0,tam-1)  
 
        x_end =  x_in + tam_pal*x
        y_end =  y_in + tam_pal*y
        
        if x_end>=0 and x_end < tam-1: 
            if y_end>=0 and y_end < tam-1:
                break
        
    return x, y, x_in, y_in, x_end, y_end

#Checar se cabe a palavra na posição
def cabe(tam_pal, tabuleiro, x_in, y_in, palavra, x, y):
    failed = False

    for i in range(tam_pal):
        letra = palavra[i]

        novox = x_in + i*x
        novoy = y_in + i*y

        velho = tabuleiro[novox][novoy]

        if velho != '_ ':
            if velho == letra:
                continue
            else:
                failed = True
                break
    return failed

orient = ['horiz', 'vert', 'diagcima', 'diagbaixo']

#Colocar as palavras no tabuleiro
for palavra in palavras:
    tam_pal = len(palavra)
    ind = True

    while ind == True:
        x, y, x_in, y_in, x_end, y_end = fit(tam, tam_pal)
        failed = cabe(tam_pal, tabuleiro, x_in, y_in, palavra, x, y)
        if failed == False:
            for i in range(tam_pal):
                letra = palavra[i]

                novox = x_in + i*x
                novoy = y_in + i*y

                tabuleiro[novox][novoy] = letra
            break

#Imprimir tabuleiro de resposta
printgrid()

#Preencher espaços restantes
for x in range(tam):
    for y in range(tam):
        if (tabuleiro[x][y]=="_ "):
            tabuleiro[x][y] = random.choice(caracteres)

#Imprimir tabuleiro completo
printgrid()

#Imprimir lista de palavras
for a in range(tam):
    print(palavras[a])