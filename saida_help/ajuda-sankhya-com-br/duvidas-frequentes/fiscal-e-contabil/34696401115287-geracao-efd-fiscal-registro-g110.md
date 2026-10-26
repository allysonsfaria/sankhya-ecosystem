---
id: "34696401115287"
titulo: "Geração EFD Fiscal - Registro G110"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34696401115287-Gera%C3%A7%C3%A3o-EFD-Fiscal-Registro-G110"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:26:50Z"
rotulos: ["Configuração", "Fiscal", "ICMS", "Impostos", "EFD", "Geração EFD Fiscal - Registro G110", "regras aplicadas pelo sistema Sankhya na geração do G110", "Registro G110", "Geração do G110", "Sankhya"]
---

# Geração EFD Fiscal - Registro G110

A geração do Registro G110 na EFD Fiscal é um ponto crítico para empresas que utilizam o Sankhya, pois envolve a apuração de créditos de ICMS sobre o ativo imobilizado. Mais do que atender a uma exigência fiscal, esse processo depende de regras sistêmicas específicas que definem como as informações são tratadas e enviadas ao SPED.

Confira as **principais regras aplicadas pelo sistema Sankhya na geração do G110, destacando os critérios utilizados e os cuidados necessários** para garantir conformidade e precisão nos dados transmitidos:

**(1)** Nas Preferências da empresa (Comercial » Preferências » Empresa), aba **"EFD - Escrituração Fiscal Digital",** configure os blocos e registros do Registro G110;

**(2)** Registro **G125 deve estar sendo gerado** e com seus **devidos valores**;

**(3)** O campo **SALDO\_IN\_ICMS será a soma dos seguintes campos,** dos bens gerados no registro G125:

- Valor crédito de ICMS dif. alíquota
- Valor crédito ICMS sobre frete
- Valor do ICMS
- Valor crédito ICMS por subst. tributária

![Imagem 1: Valor crédito ICMS por subst. tributária](https://ajuda.sankhya.com.br/hc/article_attachments/35363906703767)

**(4)** O campo **SOM\_PARC** será a soma do **campo 10, do registro G125.** Para mais informações sobre campo 10, do registro G125, acesso o artigo: [EFD ICMS/IPI | Registro G125 - Campo 10 VL\_PARC\_PASS](https://ajuda.sankhya.com.br/hc/pt-br/articles/30877925152791-EFD-ICMS-IPI-Registro-G125-Campo-10-VL-PARC-PASS)

**(5)** O campo **"VL\_TRIB\_EXP"** será o **somatório do valor de todos os itens de saída que atendam às seguintes condições:**

- As notas estão cadastradas na tela **"Cadastro Livro ICMS IPI";**
- São de **notas fiscais de saída**;
- **Têm um CFOP** (Código Fiscal de Operações e Prestações)
- Pertencem à **empresa que selecionou ao gerar o .txt** e tem a sua **data do documento (não a data de entrada/lançamento) dentro do período de apuração;**
- O **valor será extraído conforme a configuração do CFOP** usada nos itens

![Imagem 2: O valor será extraído conforme a configuração do CFOP usada nos itens](https://ajuda.sankhya.com.br/hc/article_attachments/35364884242583)

**(6)** O campo **VL\_TOTAL** será calculado conforme explicado no **tópico 5.** Porém, de acordo com o que foi definido no campo **"Receita bruta p/EFD Contribuições"** da tela CFOP, e com o que foi usado no lançamento das notas que se enquadrem no tópico anterior também.

**(7)** Campo **IND\_PER\_SAI** será o cálculo do campo 9 dividido pelo campo 10.

**(8)** **Valor de ICMS a ser apropriado na apuração do ICMS**, correspondente à multiplicação do campo 05 pelo campo 08.

**(9)** O campo **SOM\_ICMS\_OC** será calculado conforme já apresentado no artigo [Crédito Extemporâneo - Registro G126 do SPED FISCAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044513733-Cr%C3%A9dito-Extempor%C3%A2neo-Registro-G126-do-SPED-FISCAL)
