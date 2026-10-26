---
id: "360043179774"
titulo: "Numeração não configurada TOP XX série XX. Verifique no cadastro de TOP de Operação/Impressão/Controle de Numeração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179774-Numera%C3%A7%C3%A3o-n%C3%A3o-configurada-TOP-XX-s%C3%A9rie-XX-Verifique-no-cadastro-de-TOP-de-Opera%C3%A7%C3%A3o-Impress%C3%A3o-Controle-de-Numera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-06T18:45:22Z"
rotulos: ["ERRONF", "#RevisadoCarmen", "CORE_E02247", "Configuração", "Impressão", "NF-e", "TOP", "Ajuste na tela \"Tipos de Operação - TOP\"", "Numeração não configurada", "Número/série não cadastrado", "Erro", "Documentos Eletrônicos"]
---

# Numeração não configurada TOP XX série XX. Verifique no cadastro de TOP de Operação/Impressão/Controle de Numeração

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16165965504407) MENSAGEM:**

[CORE\_E02247] Numeração não configurada TOP XX série XX. Verifique no cadastro de TOP de Operação/Impressão/Controle de Numeração.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16165917261079) SITUAÇÃO:**

Ao tentar emitir um pedido ou nota a seguinte mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16165965554071) CAUSA:**

Mensagem apresentada ao realizar lançamentos no sistema com número/série nota não cadastrados no controle de numeração da respectiva TOP.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16165917264023) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 5: Acesse a tela " Tipos de Operação - TOP " (Caminho de acesso: Comercial »> Arquivos » Cadastros » Tipos de Operação -…](https://ajuda.sankhya.com.br/hc/article_attachments/16165965513623) Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial »> Arquivos » Cadastros » Tipos de Operação - TOP)

![Imagem 6: Campo "Outras Opções" » " Controle de Numeração":](https://ajuda.sankhya.com.br/hc/article_attachments/16165965516567) Campo **"Outras Opções"** » "**Controle de Numeração":**

![Imagem 7: Campo "Outras Opções" » " Controle de Numeração":](https://ajuda.sankhya.com.br/hc/article_attachments/14707938360983)

![Imagem 8: Deverá existir uma linha para a 'Empresa', 'Série' e 'Modelo de Documento' referente ao lançamento realizado.](https://ajuda.sankhya.com.br/hc/article_attachments/16165965533207) Deverá existir uma linha para a 'Empresa', 'Série' e 'Modelo de Documento' referente ao lançamento realizado.

![Imagem 9: Deverá existir uma linha para a 'Empresa', 'Série' e 'Modelo de Documento' referente ao lançamento realizado.](https://ajuda.sankhya.com.br/hc/article_attachments/12235796078871)

(1)** EXEMPLO¹:**

Numeração não configurada.
Top: 1018
Empresa: 2
Série: 1
CodModDoc = 0 ou 1
Verifique no Cadastro de Tipo de Operação/Impressão/Controle de Numeração.

Conforme mensagem de erro, o sistema está solicitando o cadastro de uma linha de numeração na TOP 1018, para empresa 2, série 1, Modelo do documento 0 ou 1.

Dessa forma, teríamos:

![Imagem 10: Dessa forma, teríamos:](https://ajuda.sankhya.com.br/hc/article_attachments/14708000718999)

O**"Tipo de Numeração"**serve para identificar qual será a opção de numeração da top, conjuntamente ao campo Base de Numeração e **"Outras Opções – Controle de Numeração"**. Exemplo: Base de Numeração é Venda e o Tipo de Numeração é Empresa e nas Outras Opções – Controle de Numeração cadastra-se a empresa 1.

- **Única:** Todas as notas criadas com este tipo de Numeração respeitarão a mesma sequência para uma empresa, sem série, etc.
- **Empresa/Série:** Todas as notas criadas com este tipo de Numeração terão para cada empresa/série terá uma sequência a ser seguida.

**(1)** **EXEMPLO²:**

Caso a empresa trabalhe com cupom fiscal, necessariamente deverá configurar a TOP por Empresa/Série.

**![Imagem 11: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16165917273111) IMPORTANTE:**

- Lembre-se de verificar se o campo **"Série"** informado no cabeçalho da nota, corresponde a série necessária para o respectivo lançamento.
- Caso não visualize esse campo no lançamento, faça a inserção do mesmo através do **"[Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)"**, para mais detalhes acesse: [Como inserir um campo no layout da nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)
