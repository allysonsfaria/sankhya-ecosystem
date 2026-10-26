---
id: "34855694078743"
titulo: "Lançamento não está sendo apresentado na tela Geração de Lote GNRE? Saiba como resolver."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34855694078743-Lan%C3%A7amento-n%C3%A3o-est%C3%A1-sendo-apresentado-na-tela-Gera%C3%A7%C3%A3o-de-Lote-GNRE-Saiba-como-resolver"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:26:34Z"
rotulos: ["Configuração", "Movimentação Financeira", "Geração de Lote GNRE", "Impostos", "Nota Fiscal", "GNRE", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Lançamento não está sendo apresentado", "Saiba como resolver", "Status da Nota", "Vincula DAE/GNRE", "Fórmulas p/ Parcelas Independentes", "na tela Geração de Lote GNRE", "título de despesa", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Lançamento não está sendo apresentado na tela Geração de Lote GNRE? Saiba como resolver.

**SITUAÇÃO**

Ao acessar a tela **"Geração de Lote GNRE"** (Financeiro >> Rotinas >> Geração de Lote GNRE), os lançamentos ou notas fiscais emitidas não são apresentados para processamento.

**SOLUÇÃO**

Verifique e ajuste os requisitos para que o título seja incluído na consulta da tela Geração de Lote GNRE.

Execute os passos abaixo:

**(1)**  Verifique se o lançamento é um **título de despesa;**

**(2)**  Confirme que o título não está baixado em **Movimentação Financeira;**

**(3)**  Garanta que o **Status da Nota**esteja com valor **"L = Liberada"** (verificar no cabeçalho da nota); 

**(4)**  Confirme que o título **não é provisão** (campo **"Provisão"** = 'N'); 

**(5)**  Valide a existência de **Observação Padrão vinculada**:

- Na **"Alíquota de ICMS"** do item;
- No **"Cabeçalho da Nota".**

#### Sobre a Observação Padrão:

**(1)** Verifique se a Observação Padrão possui a marcação **"Vincular DAE/GNRE"** habilitada.

![Imagem Observação](https://ajuda.sankhya.com.br/hc/article_attachments/35707913423511)

**Importante:**

- Para **Guia GNRE ST**: garanta que o tipo de título usado no financeiro corresponde ao informado no parâmetro **TIPTITGNREST**.
- Para **Guia GNRE Difal**:

Certifique que o tipo de título **não seja** o mesmo informado no parâmetro **TIPTITGNREST;**

Confirme que o tipo de título esteja cadastrado na tela **"Fórmulas p/ Parcelas Independentes"** (Financeiro > Arquivos > Cadastros > Tipos de Título). 

(1)** Select realizado pelo sistema ao aplicar a consulta na tela Geração de Lote GNRE:**

SELECT \* FROM TGFFIN WHERE EXISTS (
SELECT 1 FROM TGFCAB C
JOIN TGFITE I   ON I.NUNOTA = C.NUNOTA
JOIN TGFPAR PARC ON C.CODPARC = PARC.CODPARC
JOIN TSICID CID  ON PARC.CODCID = CID.CODCID
JOIN TSIUFS UFS  ON CID.UF = UFS.CODUF
WHERE C.NUNOTA = TGFFIN.NUNOTA
AND C.STATUSNOTA = 'L'
AND (( TGFFIN.CODTIPTIT = '41' **--Informe aqui o tipo de título do parâmetro TIPTITGNREST**
OR TGFFIN.CODTIPTIT = UFS.TIPTITGNREFCPST
OR (TGFFIN.CODTIPTIT = 0 AND C.STATUSCTE = 'A'))
OR EXISTS (
SELECT 1 FROM TGFFPI FPI
WHERE FPI.CODTIPTIT = TGFFIN.CODTIPTIT
AND FPI.CODUF = UFS.CODUF
AND FPI.FINPARAGNRE = 'S'))
AND (EXISTS (SELECT 1
FROM TGFOBS O
JOIN TGFITE I2 ON O.CODOBSPADRAO = I2.CODOBSPADRAO
WHERE I2.NUNOTA = TGFFIN.NUNOTA
AND O.VINCDOCARREC = 'S')
OR EXISTS (
SELECT 1 FROM TGFOBS O
JOIN TGFCAB C2 ON O.CODOBSPADRAO = C2.CODOBSPADRAO
WHERE C2.NUNOTA = TGFFIN.NUNOTA
AND O.VINCDOCARREC = 'S')))
AND TGFFIN.RECDESP = -1
AND TGFFIN.PROVISAO = 'N'
AND TGFFIN.DHBAIXA IS NULL

É importante destacar que o select utilizado não contempla os filtros adicionais disponíveis na tela, podendo, assim, sofrer alterações conforme os parâmetros aplicados.

**CAUSA:**

O título não é apresentado porque não atende a uma ou mais premissas da consulta de geração de lote GNRE (por exemplo: não ser título de despesa, estar baixado, status da nota diferente de L, ser provisão, ausência de Observação Padrão com **"Vincula DAE/GNRE"**, ou tipo de título incompatível com o parâmetro **TIPTITGNREST**).
