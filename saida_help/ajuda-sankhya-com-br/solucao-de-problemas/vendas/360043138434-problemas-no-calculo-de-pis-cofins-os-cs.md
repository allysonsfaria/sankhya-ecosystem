---
id: "360043138434"
titulo: "Problemas no cálculo de PIS/COFINS: Os CST's devem ser iguais e não vazios"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043138434-Problemas-no-c%C3%A1lculo-de-PIS-COFINS-Os-CST-s-devem-ser-iguais-e-n%C3%A3o-vazios"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-24T18:15:21Z"
rotulos: ["Configuração", "NF-e", "Impostos", "TOP", "Verificar e ajustar configurações de PIS/COFINS em TOP empresa e produto", "Erro na validação de PIS/COFINS ao confirmar nota", "Regras e CSTs incoerentes ou configurações inadequadas", "Erro", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Problemas no cálculo de PIS/COFINS: Os CST's devem ser iguais e não vazios

**MENSAGEM:**

Validar TGFDIN: Validação da TGFDIN. Nota Nro.Único: xxxxxx.
Problemas no cálculo de PIS/COFINS: Os CSTs devem ser iguais e não vazios.
PIS é obrigatório para NF-e.
COFINS é obrigatório para NF-e.
Procure o administrador do sistema

**SITUAÇÃO:**

Ao tentar confirmar uma Nota Fiscal de Venda ou Devolução de Compra, ocorre a mensagem de erro acima, indicando falha no cálculo de PIS e COFINS.

**SOLUÇÃO:**

Para correção, verifique as parametrizações seguindo a ordem:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros)
      **(2)** Aba **"Impostos",**campos: **"TEM PIS"** / **"TEM COFINS"**: Marcados

**(2)** Aba **"Livros Fiscais"**, campo: **"Atualização de Livro de ICMS"**: Configure de acordo com o movimento

**(2)** Acesse a tela **"Empresa"** (Comercial » Preferências)
      **(2)** Aba: **"Propriedades"**, campos: **"Calcula PIS"**/**"Calcula COFINS"**: Marcados

**(3)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos)
     **(2)** Aba: **"Impostos"**, campos: **"Grupo PIS"**/**"Grupo COFINS"**: Insira os respectivos grupos criados nas telas de alíquotas de PIS e COFINS, conforme orientados nos passos 4 e 5 que seguem abaixo. 

**(4)** Acesse a tela "**Alíquotas de PIS**" (Comercial » Arquivo » Cadastros » Alíquotas):
    **(2)** Nessa tela deverá criar uma regra para o Grupo de PIS vinculado ao respectivo produto, para o tipo de movimento utilizado (Entrada ou Saída). Atente-se a compreender o processo atual da empresa, validando exceções por TOP ou Parceiro, por exemplo.

**(2)** Informe o **Cód. sit. tributária** compatível com suas operações. Vale destacar que essa informação deve ser validada com o Contador da empresa.

**(5)** Acesse a tela "**Alíquotas de COFINS**" (Comercial » Arquivo » Cadastros » Alíquotas):
    **(2)** Nessa tela deverá criar uma regra para o Grupo de COFINS vinculado ao respectivo produto, para o tipo de movimento utilizado (Entrada ou Saída). Atente-se a compreender o processo atual da empresa, validando exceções por TOP ou Parceiro, por exemplo.

**(2)** Informe o **Cód. sit. tributária** compatível com suas operações. Vale destacar que essa informação deve ser validada com o Contador da empresa.

**CAUSA:**

O erro ocorre por configurações inadequadas (CST's vazios ou incoerentes), falta de grupos de impostos vinculados ao produto ou parametrizações de TOP ou Empresa incorretas para o tipo de movimentação realizada.
