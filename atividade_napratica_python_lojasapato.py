#Programa de auxílio ao cálculo do preço de custo e preço final

#v_couro é o valor do couro para fabricação unitária
v_couro = float(input('Digite o valor do COURO: '))
#v_solado é o valor do solado para fabricação unitária
v_solado = float(input('Digite  valor do SOLADO: '))
#v_cordoes é o valor de cordões e ilhoses para fabricação unitária
v_cordoes = float(input('Digite o valor de CORDÕES E ILHOSES: '))
#v_insumos é o valor dos insumos diversos para fabricação unitária
v_insumos = float(input('Digite o valor de INSUMOS: '))
#v_MaoObra é o valor de mão de obra para fabricação unitária
v_MaoObra = float(input('Digite o valor de MÃO DE OBRA: '))
#v_marketing é o valor de marketing e propagando dividido pela produção
v_marketing = float(input('Digite o valor de marketing: '))
#v_vendas é o valor od custo de vendas dividido pela produção
v_vendas = float(input('Digite o valor dos custos de venda: '))

#CALCULO DO PREÇO DE CUSTO
preco_custo = (v_couro*0.30)+(v_solado*0.20)+(v_cordoes*0.05)+(v_insumos*0.05)+(v_MaoObra*0.20)+(v_marketing*0.10)
print('O preço de custo unitário deste modelo de sapato é: ',preco_custo)

#CALCULANDO O PREÇO FINAL:
#CALCULO DO PREÇO ADICIONANDO LUCRO DO FABRICANTE
preco_lucro = preco_custo*1.30
#CALCULO DO PREÇO ADICIONANDO PERDAS DE CAPITAL
preco_perdas = preco_lucro*1.15
#CALCULO DO PRECO ADICIONANDO IMPOSTOS FEDERAIS
preco_IPI_COFINS = preco_perdas*1.15
#CALCULO DO PRECO ADICIONANDO MARGEM DE VENDAS
preco_venda = preco_IPI_COFINS*1.25
#CALCULO DO PREÇO ADICIONANDO IMPOSTOS ESTADUAIS E MUNICIPAIS
preco_ICM_INSS = preco_venda*1.30

#PREÇO FINAL, ACRESCIDO DE TODOS OS IMPOSTOS E MARGENS DE LUCRO
preco_final = preco_ICM_INSS
print ('O preço final ao consumidor deste modelo de sapato é: ',preco_final)
