---
id: "36859518583831"
titulo: "Erro for input string: \"F\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36859518583831-Erro-for-input-string-F"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:22:21Z"
rotulos: ["ERROMDFE", "MDF-e", "Configuração", "SEFAZ", "Transporte", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Viagens de Transporte (MDF-e)", "Controle de numeração", "for input string: \"F\"", "input string: \"F\""]
---

# Erro for input string: "F"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/36859518570135) **MENSAGEM:**

for input string: "F"

**SITUAÇÃO:**

Ao tentar confirmar o MDF-e pela tela **Viagens de Transporte (MDF-e)**, o sistema exibe a mensagem:

```
for input string: "F"
```

O caractere exibido entre aspas na mensagem pode variar conforme o valor configurado na **série do documento**. Dependendo da configuração, o sistema pode mostrar **"F"**, **"U"**, **"B"**, entre outros.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36859518573719)SOLUÇÃO:**

**(1)** Acesse a tela [**''Viagens de Transporte (MDF-e)''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e) (Comercial » Rotinas » Viagens de Transporte (MDF-e)).

**(2)** Clique no botão **“Outras Opções”** (ícone da engrenagem no canto superior direito).

**(3)** Selecione a opção **''Controle de Numeração''**.

**(4)** No campo **''Série''**, substitua o valor atual (exemplo: `MDf`) por uma **série numérica válida**, como **1** ou **2**, conforme o padrão utilizado pela empresa e aceito pela SEFAZ.

**(5)** Salve as alterações.

**OBSERVAÇÃO:**

Após ajustar a série no ''Controle de Númeração'', é necessário gerar uma nova **Ordem de Carga** ou um **novo MDF-e** para que a numeração correta seja aplicada.

O MDF-e que já foi emitido com a série inválida **não será atualizado retroativamente**.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36859502116247)CAUSA:**

O erro ocorre devido à configuração incorreta do **Controle de Numeração do MDF-e**, especificamente ao campo ''Série''.

No caso analisado, a série configurada com **letras**, por exemplo:

- Série configurada: `MDf`

Quando o sistema tenta interpretar a série como número, ocorre erro de conversão, gerando a exceção:

```
for input string: "F"
```

O comportamento segue um padrão: o erro aponta para o **último caractere inválido da série**:

- Se a série for **MDF** → erro **"F"**
- Se a série for **MDu** → erro **"U"**
- Se for **A1B**→ erro **"B"**

Ou seja, **qualquer série que contenha letras ou caracteres não numéricos causará o problema**.

A série do MDF-e **deve obrigatoriamente ser numérica** (recomenda-se a utilização da série 1), conforme o padrão da SEFAZ.
