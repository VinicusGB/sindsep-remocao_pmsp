import re

separador_silabico_virgula_antes = re.compile(r'[a-zA-Z0-9]?\s*[-,]\s*\n[a-zA-Z0-9]?')
separador_silabico_virgula_depois = re.compile(r'[a-zA-Z0-9]?\s*\n,\s*[a-zA-Z0-9]?')
preposicoes_daeos_antes = re.compile(r' [aAdDnNsS]?[aàeoAÀEO][sSmM]?\s*\n.')
preposicoes_daeos_depois = re.compile(r'[a-zA-Z0-9]?\s*\n[aAdDnNsS]?[aàeoAÀEO][sSmM]? ')
conjuncoes_antes = re.compile(r'[,\s](com|COM|como|COMO|mas|MAS|mesmo|MESMO|para|PARA|por|POR|qual|QUAL|quando|QUANDO|que|QUE|ou|OU|e/ou|E/OU)\s*\n.')
conjuncoes_depois = re.compile(r'[a-zA-Z0-9]?\s*\n(com|COM|como|COMO|mas|MAS|mesmo|MESMO|para|PARA|por|POR|qual|QUAL|quando|QUANDO|que|QUE|ou|OU) ')
pronomes_antes = re.compile(r'[,\s](nossa|NOSSA|nosso|NOSSO|pelo|PELO|pela|PELA|seu|SEU|sua|SUA|teu|TEU|tua|TUA|um|UM|uns|UNS|uma|UMA)[sS]?\s*\n.')
pronomes_depois = re.compile(r'[a-zA-Z0-9]?\s*\n(nossa|NOSSA|nosso|NOSSO|pelo|PELO|pela|PELA|seu|SEU|sua|SUA|teu|TEU|tua|TUA|um|UM|uns|UNS|uma|UMA)[sS]? ')

def limpa_dados(conteudo):
    """
        Limpa os dados do conteúdo de quebra de linha, separador silábico, preposições, pronomes e conjunções 
    """
    def limpa_quebra_de_linha(conteudo):
        #print(f"ANTES: {conteudo.string[conteudo.start()-10:conteudo.end()+10]}")
        if conteudo.string[conteudo.start()+1] == '-': return (conteudo.string[conteudo.start():conteudo.start()+2].strip()+conteudo.string[conteudo.end()-1:conteudo.end()]).strip().replace('-','')
        elif conteudo.string[conteudo.start()+1] == ',': return conteudo.string[conteudo.start():conteudo.start()+3].strip()+' '+conteudo.string[conteudo.end()-1:conteudo.end()]
        else: return conteudo.string[conteudo.start():conteudo.end()].replace('\n',' ').replace('\t',' ').replace('   ',' ').replace('  ',' ')

    conteudo_alterado = conteudo

    conteudo_alterado = separador_silabico_virgula_antes.sub(limpa_quebra_de_linha,conteudo_alterado)
    conteudo_alterado = separador_silabico_virgula_depois.sub(limpa_quebra_de_linha,conteudo_alterado)

    conteudo_alterado = preposicoes_daeos_antes.sub(limpa_quebra_de_linha,conteudo_alterado)
    conteudo_alterado = preposicoes_daeos_depois.sub(limpa_quebra_de_linha,conteudo_alterado)

    conteudo_alterado = conjuncoes_antes.sub(limpa_quebra_de_linha,conteudo_alterado)
    conteudo_alterado = conjuncoes_depois.sub(limpa_quebra_de_linha,conteudo_alterado)

    conteudo_alterado = pronomes_antes.sub(limpa_quebra_de_linha,conteudo_alterado)
    conteudo_alterado = pronomes_depois.sub(limpa_quebra_de_linha,conteudo_alterado)

    conteudo_alterado = separador_silabico_virgula_antes.sub(limpa_quebra_de_linha,conteudo_alterado)
    conteudo_alterado = separador_silabico_virgula_depois.sub(limpa_quebra_de_linha,conteudo_alterado)

    return conteudo_alterado

def limpa_dados_preposicao_conjuncao(conteudo):
    '''
    Método que utiliza regex para limpar as preposições e conjunções que estão quebrando linha no início ou no final
    '''
    espaco = re.compile(r' +')
    conteudo = espaco.sub(' ',conteudo)
    espaco_inicio = re.compile(r'^ +')
    conteudo = espaco_inicio.sub('',conteudo)
    espaco_final = re.compile(r' +$')
    conteudo = espaco_final.sub('',conteudo)
    # Regex que identifica as linhas que terminam em letra minúscula e que a próxima linha começa com letra minúscula para substituir a quebra de linha por espaço
    quebra_linha = re.compile(r'[a-z]\n[a-z]')
    return conteudo

def limpa_tabulacao_preposicoes(conteudo):
    '''
    Método que limpa a tabulação e as preposições
    '''
    conteudo = conteudo.replace('-\n','')
    conteudo = conteudo.replace(',\n',', ')
    conteudo = conteudo.replace('\npara ',' para ')
    conteudo = conteudo.replace('\nna ',' na ')
    conteudo = conteudo.replace('\nno ',' no ')
    conteudo = conteudo.replace('\nda ',' da ')
    conteudo = conteudo.replace(' da\n',' da ')
    conteudo = conteudo.replace('\nde ',' de ')
    conteudo = conteudo.replace(' de\n',' de ')
    conteudo = conteudo.replace('\ndo ',' do ')
    conteudo = conteudo.replace(' do\n',' do ')
    conteudo = conteudo.replace('\ndos ',' dos ')
    conteudo = conteudo.replace(' dos\n',' dos ')
    conteudo = conteudo.replace('\ndas ',' das ')
    conteudo = conteudo.replace(' das\n',' das ')
    conteudo = conteudo.replace('\nem ',' em ')
    conteudo = conteudo.replace(' em\n',' em ')
    conteudo = conteudo.replace('\ncom ',' com ')
    conteudo = conteudo.replace(' com\n',' com ')
    conteudo = conteudo.replace('\npor ',' por ')
    conteudo = conteudo.replace(' por\n',' por ')
    conteudo = conteudo.replace('\nsem ',' sem ')
    conteudo = conteudo.replace(' sem\n',' sem ')
    conteudo = conteudo.replace('\nentre ',' entre ')
    conteudo = conteudo.replace(' entre\n',' entre ')
    conteudo = conteudo.replace('\nentre ',' entre ')
    conteudo = conteudo.replace(' entre\n',' entre ')
    conteudo = conteudo.replace('\nentre ',' entre ')
    conteudo = conteudo.replace(' entre\n',' entre ')
    return conteudo

def limpa_tabulacao(conteudo_alterado):
    print('\n### LIMPA TABULAÇÃO ###')
    print(f'Qtd de linhas antes: {len(conteudo_alterado)}')
    qtd_len_inicial = len(conteudo_alterado)
    qtd_len_final = 0
    while qtd_len_final < qtd_len_inicial:
        qtd_len_inicial = len(conteudo_alterado)
        conteudo_alterado = conteudo_alterado.replace('\t',' ')
        conteudo_alterado = conteudo_alterado.replace('""','')
        conteudo_alterado = conteudo_alterado.replace('\n\n\n','\n')
        conteudo_alterado = conteudo_alterado.replace('\n\n','\n')
        conteudo_alterado = conteudo_alterado.replace(' \n','\n')
        conteudo_alterado = conteudo_alterado.replace('\n ','\n')
        conteudo_alterado = conteudo_alterado.replace('    ',' ')
        conteudo_alterado = conteudo_alterado.replace('   ',' ')
        conteudo_alterado = conteudo_alterado.replace('  ',' ')
        conteudo_alterado = conteudo_alterado.replace('-\n','')
        conteudo_alterado = conteudo_alterado.replace('\n- ',' - ')
        conteudo_alterado = conteudo_alterado.replace('\n– ',' – ')
        conteudo_alterado = conteudo_alterado.replace(',\n',', ')
        conteudo_alterado = conteudo_alterado.replace(', \n',', ')
        conteudo_alterado = conteudo_alterado.replace('\n, ',', ')
        conteudo_alterado = conteudo_alterado.replace('/\n','/')
        conteudo_alterado = conteudo_alterado.upper()
        qtd_len_final = len(conteudo_alterado)
    print(f'Qtd de linhas depois: {len(conteudo_alterado)}')
    return conteudo_alterado

def normaliza_cabecalho(conteudo_alterado):
    print('\n### NORMALIZA CABEÇALHO ###')
    print(f'Qtd de linhas antes: {len(conteudo_alterado)}')
    qtd_len_inicial = len(conteudo_alterado)
    qtd_len_final = 0
    while qtd_len_final < qtd_len_inicial:
        qtd_len_inicial = len(conteudo_alterado)
        conteudo_alterado = conteudo_alterado.replace('E.H.','EH')
        conteudo_alterado = conteudo_alterado.replace('E.H ','EH ')
        conteudo_alterado = conteudo_alterado.replace('REG. FUNC.','RF')
        conteudo_alterado = conteudo_alterado.replace('REG.FUNC.','RF')
        conteudo_alterado = conteudo_alterado.replace('REG. FUNC/','RF/VINCULO')
        conteudo_alterado = conteudo_alterado.replace('REG. FUNC/VINC ','RF/VINC ')
        conteudo_alterado = conteudo_alterado.replace('REG VINC ','RF VINCULO ')
        conteudo_alterado = conteudo_alterado.replace('RF./','RF/')
        conteudo_alterado = conteudo_alterado.replace('R.F.','RF')
        conteudo_alterado = conteudo_alterado.replace('RF. ','RF ')
        conteudo_alterado = conteudo_alterado.replace(' VINC.',' VINCULO')
        conteudo_alterado = conteudo_alterado.replace('RF/VINC ','RF/VINCULO ')
        conteudo_alterado = conteudo_alterado.replace('DURAÇÃO','DURACAO')
        conteudo_alterado = conteudo_alterado.replace('A PARTIR DE','A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('A PARTIR','A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace(' ART.','ARTIGO')
        conteudo_alterado = conteudo_alterado.replace('PERÍODO','PERIODO')
        conteudo_alterado = conteudo_alterado.replace(' VÍNC.',' VINCULO')
        conteudo_alterado = conteudo_alterado.replace(' QTE DE DIAS ',' DIAS ')
        conteudo_alterado = conteudo_alterado.replace(' NO DE DIAS ',' DIAS ')
        conteudo_alterado = conteudo_alterado.replace('RF/V ','RF/VINCULO ')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO FUNCIONAL NOME A_PARTIR_DE','RF NOME A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO FUNCIONAL NOME ','RF NOME ')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO NOME CARGO EXER- Q U A N - A_PARTIR_DE\nFUNCIONAL CÍCIO TIDADE','RF NOME CARGO EXERCICIO DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO NOME CARGO EXER- QUAN- A_PARTIR_DE\nFUNCIONAL CÍCIO TIDADE','RF NOME CARGO EXERCICIO DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO NOME CARGO EXER- QUANTI- A_PARTIR_DE\nFUNCIONAL CÍCIO DADE','RF NOME CARGO EXERCICIO DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('EH R.F/V NOME QTE DE A_PARTIR_DE\nDIAS','EH RF NOME DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF NOME DIAS A PARTIR DE ARTIGO','RF NOME DIAS A_PARTIR_DE ARTIGO')
        conteudo_alterado = conteudo_alterado.replace('RF NOME A PARTIR DE','RF NOME A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF NOME DUR A_PARTIR_DE','RF NOME DURACAO A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF SERVIDOR CONTROLE NO','RF NOME CONTROLE_NO')
        conteudo_alterado = conteudo_alterado.replace('RF SERVIDOR DIAS A_PARTIR_DE','RF NOME DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF NOME CONTROLE NO','RF NOME CONTROLE_NO')
        conteudo_alterado = conteudo_alterado.replace('RF/V NOME DIAS/EXERCÍCIO A PARTIR DE','RF/VINCULO NOME DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF/VINCULO NOME DIAS A_PARTIR_DE','RF/VINCULO NOME DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF/VINCULO NOME NO DE DIAS A_PARTIR_DE PARENTESCO','RF/VINCULO NOME DIAS A_PARTIR_DE PARENTESCO')
        conteudo_alterado = conteudo_alterado.replace('RF/VINC NOME NÍVEL CAT. SÍMBOLO A PARTIR DE','RF/VINCULO NOME NIVEL_CAT SIMBOLO A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF NOME CARGO','RF NOME CARGO')
        conteudo_alterado = conteudo_alterado.replace('RF V NOME EH A PARTIR DE MOTIVO','RF VINCULO NOME EH A_PARTIR_DE MOTIVO')
        conteudo_alterado = conteudo_alterado.replace('R.F/V. NOME QTE DIAS A_PARTIR_DE','RF/VINCULO NOME DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF VINCULO NOME CARGO A PARTIR DE','RF VINCULO NOME CARGO A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('NOME RF DATA HORARIO','NOME RF DATA_HORARIO')
        conteudo_alterado = conteudo_alterado.replace('NOME RF DATAHORARIO','NOME RF DATA_HORARIO')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO VINC. NOME NIIVEL CAT.','RF VINCULO NOME NIIVEL CAT')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO VINC. NOME NIIVEL CAT. SIM','RF VINCULO NOME NIVEL CAT SIM')
        conteudo_alterado = conteudo_alterado.replace('RF VINC NOME NIIVEL CAT','RF VINCULO NOME NIVEL CAT')
        conteudo_alterado = conteudo_alterado.replace('REG. FUNC. NOME CARGO REGIME EXP. AC. NO','RF NOME CARGO REGIME EXP_AC_NO')
        conteudo_alterado = conteudo_alterado.replace('EH RF NOME DURAÇÃO A PARTIR ART','EH RF NOME DURACAO A_PARTIR_DE ARTIGO')
        conteudo_alterado = conteudo_alterado.replace('EH RF/V NOME DURA- A_PARTIR_DE\nÇÃO','EH RF/VINCULO NOME DURACAO A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('EH RF/VC. NOME DUR. A_PARTIR_DEARTIGO','EH RF/VINCULO NOME DURACAO A_PARTIR_DE ARTIGO')
        conteudo_alterado = conteudo_alterado.replace('REG.FUNC. NOME DE PARA','RF NOME DE PARA')
        conteudo_alterado = conteudo_alterado.replace('RF NOME NOTA INDIVIDUAL NOTA INSTITUCIONAL NOTA FINAL','RF NOME NOTA_INDIVIDUAL NOTA_INSTITUCIONAL NOTA_FINAL')
        conteudo_alterado = conteudo_alterado.replace('RF NOME DURAÇÃO À PARTIR DE','RF NOME DURACAO A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF NOME PERCENTUAL BASE DE CÁLCULO DATA','RF NOME PERCENTUAL BASE_DE_CALCULO DATA')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO NOME CARGO EXERCÍCIO QUAN- A PARTIR DE FUNCIONAL TIDADE','RF NOME CARGO EXERCICIO QUANTIDADE A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF VINCULO NOME: PERÍODO DE :','RF VINCULO NOME PERIODO_DE')
        conteudo_alterado = conteudo_alterado.replace('RF/V NOME CARGO N°DIAS','RF/VINCULO NOME CARGO DIAS')
        conteudo_alterado = conteudo_alterado.replace('NOME RF A PARTIR DE','NOME RF A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF/V NOME A PARTIR DE','RF/VINCULO NOME A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF: NOME: PROCESSO: E.H.:','RF NOME PROCESSO EH')
        conteudo_alterado = conteudo_alterado.replace('EH RF/V NOME DIAS A_PARTIR_DE\nDIAS','EH RF/VINCULO NOME DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF NOME E.H. A PARTIR','RF NOME E.H. A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF/V NOME DIAS A PARTIR DE','RF/VINCULO NOME DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF VINCULO NOME: PERIODO DE :','RF VINCULO NOME PERIODO')
        conteudo_alterado = conteudo_alterado.replace('RF NOME CONTROLE_NO ','RF NOME CONTROLE_NO\n')
        conteudo_alterado = conteudo_alterado.replace('RF VINCULO NOME CARGO A_PARTIR_DE ','RF VINCULO NOME CARGO A_PARTIR_DE\n')
        conteudo_alterado = conteudo_alterado.replace('RF/VÍNCULO NOME EXERCICIO NO DE DIAS A_PARTIR_DE','RF/VINCULO NOME EXERCICIO DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF/V NOME DIAS EXERCÍCIO INICIO','RF/VINCULO NOME DIAS EXERCICIO INICIO')
        conteudo_alterado = conteudo_alterado.replace('RF NOME CARGO REGIME EXP_AC_NO ','RF NOME CARGO REGIME EXP_AC_NO\n')
        conteudo_alterado = conteudo_alterado.replace('RF NOME CARGO EXERCICIO QUANTIDADE A_PARTIR_DE','RF NOME CARGO EXERCICIO QUANTIDADE A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF NOME DE PARA ','RF NOME DE PARA\n')
        conteudo_alterado = conteudo_alterado.replace('RF NOME NOTA_INDIVIDUAL NOTA_INSTITUCIONAL NOTA_FINAL ','RF NOME NOTA_INDIVIDUAL NOTA_INSTITUCIONAL NOTA_FINAL\n')
        conteudo_alterado = conteudo_alterado.replace('RF NOME DURACAO A_PARTIR_DE ','RF NOME DURACAO A_PARTIR_DE\n')
        conteudo_alterado = conteudo_alterado.replace('RF NOME PERCENTUAL BASE_DE_CALCULO DATA ','RF NOME PERCENTUAL BASE_DE_CALCULO DATA\n')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO NOME CARGO EXERCÍCIO QUAN- A PARTIR DE FUNCIONAL TIDADE','RF NOME CARGO EXERCICIO DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('NOME RF A_PARTIR_DE ','NOME RF A_PARTIR_DE\n')
        conteudo_alterado = conteudo_alterado.replace('RF/V NOME A_PARTIR_DE ','RF/V NOME A_PARTIR_DE\n')
        conteudo_alterado = conteudo_alterado.replace('RF NOME A_PARTIR_DE ','RF NOME A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO NOME CARGO EXERCÍCIO QUANTIDADE A_PARTIR_DE FUNCIONAL','RF NOME CARGO EXERCICIO DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO NOME CARGO EXERCÍ- QUANTI- A_PARTIR_DE\nFUNCIONAL CIO DADE','RF NOME CARGO EXERCICIO DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('REGISTRO FUNCIONAL NOME CARGO E X E R C Í - QUANTI- A_PARTIR_DE\nCIO DADE','RF NOME CARGO EXERCICIO DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('R E G I S T R O NOME CARGO EXER- QUANTI- A_PARTIR_DE\nFUNCIONAL CÍCIO DADE','RF NOME CARGO EXERCICIO DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('R. F. NOME DIA INICIO EXERC.','RF/VINCULO NOME DIA INICIO EXERCICIO')
        #conteudo_alterado = conteudo_alterado.replace('RF/VINCULO NOME DIAS A_PARTIR_DE','RF/VINCULO NOME DIAS A_PARTIR_DE\n')
        conteudo_alterado = conteudo_alterado.replace('R.F/V. NOME QTE. DIAS A_PARTIR_DE','RF/VINCULO NOME DIAS A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace('RF/VINCULO NOME DIAS A_PARTIR_DE\nPARENTESCO','RF/VINCULO NOME DIAS A_PARTIR_DE PARENTESCO')
        conteudo_alterado = conteudo_alterado.replace('RF/VINCULO NOME NÍVEL CAT. SÍMBOLO A_PARTIR_DE\nVINC','RF/VINCULO NOME NIVEL CATEGORIA SIMBOLO A_PARTIR_DE')
        conteudo_alterado = conteudo_alterado.replace(' R.F/V ',' RF/VINCULO ')
        qtd_len_final = len(conteudo_alterado)
    print(f'Qtd de linhas depois: {len(conteudo_alterado)}')
    return conteudo_alterado
