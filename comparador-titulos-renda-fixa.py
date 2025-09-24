print('-='*5, 'COMPARADOR DE TÍTULOS DE RENDA FIXA', '-='*5)

# Lê a quantidade de títulos que o usuário gostaria de comparar
n_invest = int(input('Quantos investimentos você gostaria de comparar? '))

print('-='*35)

# Mapas e listas
mapa = {1: 'dias', 2: 'meses', 3: 'anos'}
respostas = []      # tipos de investimento
tipos_rtb = []      # tipos de rentabilidade
tipos_prazo = []    # unidade do prazo
prazos_em_dias = [] # prazo convertido em dias
valores_invest = [] # valores investidos
v_rtbs = []         # rentabilidade declarada
a = [0.225, 0.2, 0.175, 0.15]  # alíquotas IR
a_invest = []       # alíquotas aplicadas
cdi = 0.149
ipca = 0.15

# Entrada de dados
for c in range(1, n_invest+1):
    # Tipo de investimento
    print('[1] CDB \n[2] LCI/LCA \n[3] CRI/CRA')
    resp = int(input(f'Selecione a classe do {c}º investimento: '))
    print('-='*35)

    # Tipo de rentabilidade
    print('[1] % do CDI \n[2] IPCA+% \n[3] % ')
    tipo_rtb = int(input(f'Selecione o tipo de rentabilidade do {c}º investimento: '))

    # Valor da rentabilidade 
    print('-='*35)
    v_rtb = float(input('Digite o valor da rentabilidade (somente números): '))

    # Tipo de prazo
    print('-='*35)
    print('[1] Dias \n[2] Meses \n[3] Anos')
    tipo_prazo = int(input(f'Selecione a contagem de prazo do {c}º investimento: '))

    # Valor do prazo
    nomes_prazo = [mapa[x] for x in tipos_prazo + [tipo_prazo]]
    print('-='*35)
    valor_prazo = int(input(f'Por quantos {nomes_prazo[c-1]} o {c}º título ficará investido? '))

    # Valor investido
    print('-='*35)
    valor_invest = float(input('Valor investido: R$ '))
    print('-='*35)

    # Converte para dias
    if tipo_prazo == 2:  # meses
        valor_prazo *= 30
    elif tipo_prazo == 3:  # anos
        valor_prazo *= 365

    # Armazena nas listas
    respostas.append(resp)
    tipos_rtb.append(tipo_rtb)
    tipos_prazo.append(tipo_prazo)
    prazos_em_dias.append(valor_prazo)
    valores_invest.append(valor_invest)
    v_rtbs.append(v_rtb)

# Calcula alíquotas de IR e prepara rendimento bruto/líquido
a_invest = []
rbs = []
rls = []

for c in range(n_invest):
    if respostas[c] == 1:  # CDB
        if prazos_em_dias[c] <= 180:
            aliquota = a[0]
        elif 181 <= prazos_em_dias[c] <= 360:
            aliquota = a[1]
        elif 361 <= prazos_em_dias[c] <= 720:
            aliquota = a[2]
        else:
            aliquota = a[3]
        a_invest.append(aliquota)
        print(f'Investimento {c+1}: alíquota de IR = {aliquota*100:.2f}%')
    else:  # LCI/LCA e CRI/CRA
        a_invest.append(0)
        print(f'Investimento {c+1}: isento de IR')

    # Calcula rendimento bruto
    if tipos_rtb[c] == 1:  # % do CDI
        rb = (v_rtbs[c] * cdi) / 100
        print('Vc escolheu % do CDI')
    elif tipos_rtb[c] == 2:  # IPCA+%
        rb = ipca + (v_rtbs[c] / 100)
        print('Vc escolheu IPCA+%')
    elif tipos_rtb[c] == 3:  # % fixo
        rb = v_rtbs[c] / 100
        print('Vc escolheu %')

    rl = rb * (1 - a_invest[c])  # rendimento líquido
    rbs.append(rb)
    rls.append(rl)

    print(f'Rendimento bruto: {rb*100:.2f}%')
    print(f'Rendimento líquido: {rl*100:.2f}%')

# Calcula lucro líquido
lucros = [valores_invest[c] * rls[c] for c in range(n_invest)]

# Ranking dos investimentos por lucro líquido
ranking = sorted(enumerate(lucros), key=lambda x: x[1], reverse=True)

# Exibe tabela com lucro e rentabilidade líquida
print('-='*35)
print(f'{"Posição":^10}{"Investimento":^15}{"Lucro líquido (R$)":^25}{"Rentabilidade líquida (%)":^25}')
print('-'*75)
for pos, (idx, valor) in enumerate(ranking, start=1):
    print(f'{pos:^10}{idx+1:^15}{valor:>25.2f}{rls[idx]*100:>25.2f}')
print('-='*35)
