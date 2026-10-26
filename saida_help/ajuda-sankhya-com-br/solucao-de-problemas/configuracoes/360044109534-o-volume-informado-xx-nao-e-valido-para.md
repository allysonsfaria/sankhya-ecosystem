---
id: "360044109534"
titulo: "O volume informado 'XX' não é válido para este produto 'Y' e controle ' '"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109534-O-volume-informado-XX-n%C3%A3o-%C3%A9-v%C3%A1lido-para-este-produto-Y-e-controle"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:53Z"
rotulos: ["#PUBLIFER", "#revisadohugo", "Produtos", "Configuração", "Importação", "Estoque", "CORE_E02742", "CORE_E01632", "erro de Volume Inválido para Produto Específico", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# O volume informado 'XX' não é válido para este produto 'Y' e controle ' '

[CORE\_E02742] O volume informado 'PC' não é válido para o produto '817067' e controle.

### SITUAÇÃO

Esta mensagem aparece ao tentar **"Importar uma Nota Fiscal"** no sistema, quando a unidade de medida informada no documento fiscal não está configurada corretamente no cadastro do produto. O erro impede a conclusão da importação da nota.

### SOLUÇÃO

Para resolver este erro, siga os passos abaixo:

**(1)** Acesse o cadastro de **"Produtos"** (Configurações >> Cadastros >> Produtos) e localize o produto pelo código informado na mensagem de erro.
**(2)** Na tela do produto, verifique qual é a **"Unidade Padrão"** configurada e confirme se a unidade informada na nota é a correta para este produto.
**(3)** Acesse a aba **"Unidades Alternativas"** dentro do cadastro do produto.

![Imagem 1: (1) Acesse o cadastro de "Produtos" (Configurações >> Cadastros >> Produtos) e localize o produto pelo código informado…](https://ajuda.sankhya.com.br/hc/article_attachments/14990362513303)

**(4)** Verifique se a unidade está cadastrada nesta aba. Caso não esteja, adicione-a como unidade alternativa com os **"Fatores de conversão"** adequados.
**(5)** Certifique-se de que a unidade está marcada como **"Ativa"**. Caso esteja inativa, ative-a.
**(6)** Se necessário, verifique também se o **"Código de barras"** está preenchido para a unidade alternativa, pois alguns processos podem exigir esta informação.
**(7)** Salve as alterações realizadas no cadastro do produto.
**(8)** Tente importar a nota fiscal novamente.

### CAUSA

O erro **[CORE\_E02742]** ocorre quando:

- A unidade de medida informada na nota fiscal não existe no cadastro do produto;
- A unidade existe no cadastro, mas está inativa;
- A unidade não está configurada como **"Unidade Alternativa"** do produto;
- A unidade alternativa está cadastrada, mas sem as informações complementares necessárias, como **"Código de barras"** (em integrações com WMS, por exemplo).

O sistema valida se a unidade de medida utilizada no documento fiscal está devidamente configurada no cadastro do produto antes de permitir a importação, garantindo a integridade dos dados e o correto controle de estoque.
