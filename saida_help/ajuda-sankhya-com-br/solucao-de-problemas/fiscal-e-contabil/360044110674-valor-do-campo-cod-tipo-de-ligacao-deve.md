---
id: "360044110674"
titulo: "Valor do campo 'Cód. tipo de ligação' deve estar entre 1 e 3"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110674-Valor-do-campo-C%C3%B3d-tipo-de-liga%C3%A7%C3%A3o-deve-estar-entre-1-e-3"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:19Z"
rotulos: ["#PUBLIFER", "#revisadojunior", "Configuração", "Fiscal", "NF-e", "CORE_E00914", "Ajuste: Atualize notas antigas via banco de dados ou reemita com a configuração correta.", "Solução: Configure o campo na tela \"Empresa\" com valores 1 (Monofásico) 2 (Bifásico) 3 (Trifásico).", "Erro: Valor de 'Cód. tipo de ligação' deve ser entre 1 e 3", "SPED Fiscal", "Erro"]
---

# Valor do campo 'Cód. tipo de ligação' deve estar entre 1 e 3

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16611249606039) MENSAGEM:**

Valor do campo 'Cód. tipo de ligação' deve estar entre 1 e 3.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16611249608343) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Verifique na tela "Empresa" (Caminho de acesso: Comercial » Preferências) » aba Livros Fiscais » Nota fiscal de conta…](https://ajuda.sankhya.com.br/hc/article_attachments/16611249614999) Verifique na tela **"Empresa"** (Caminho de acesso: Comercial » Preferências) » aba Livros Fiscais » Nota fiscal de conta de Energia Elétrica » Campo **"Cód.Tipo de Ligação"**:

![Imagem 4: Verifique na tela "Empresa" (Caminho de acesso: Comercial » Preferências) » aba Livros Fiscais » Nota fiscal de conta…](https://ajuda.sankhya.com.br/hc/article_attachments/14919353871895)

![Imagem 5: Defina esse campo de acordo com a necessidade da empresa, com uma das opções abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16611222178327) Defina esse campo de acordo com a necessidade da empresa, com uma das opções abaixo:

- Bifásico
- Monofásico
- Trifásico

Quando preenchidos os campos "**Cód.Tipo de Ligação**" e "**Cód.Grupo de Tensão**", o sistema usará os dados inseridos e os informará no lançamento do Pedido/Nota na Central em seus correspondentes do Pedido/Nota, isso quando a opção "**Permite informar Ligação na Central**", estiver **desmarcada**.

Se a opção Permite informar Ligação na Central estiver **marcada** e na Configuração do Layout da Nota estiver configurado para visualização destes campos, no menu do **["Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)"**, serão apresentados os campos sem preenchimento e ficará a cargo do usuário informar estes campos na central.

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16611222187799) IMPORTANTE:**

![Imagem 7: Estes dados são de responsabilidade do usuário;](https://ajuda.sankhya.com.br/hc/article_attachments/16611249614999) Estes dados são de responsabilidade do usuário;

![Imagem 8: Além de informá-los na Configuração do Layout da Nota é necessário também que a top utilizada para o lançamento tenha o…](https://ajuda.sankhya.com.br/hc/article_attachments/16611222178327) Além de informá-los na Configuração do Layout da Nota é necessário também que a top utilizada para o lançamento tenha o código do modelo de Nota Fiscal igual a 6;

![Imagem 9: Os dados inseridos nesses campos nas movimentações da Central irão compor o registro C500 referente a Notas de Energia…](https://ajuda.sankhya.com.br/hc/article_attachments/16611222190231) Os dados inseridos nesses campos nas movimentações da Central irão compor o registro C500 referente a Notas de Energia Elétrica do SPED Fiscal;

![Imagem 10: Para as notas lançadas antes da configuração feita na empresa, será necessário ajuste via banco de dados, setando a…](https://ajuda.sankhya.com.br/hc/article_attachments/16611249622167) Para as notas lançadas antes da configuração feita na empresa, será necessário ajuste via banco de dados, setando a informação na tabela. Ou, relançar as notas setando a marcação Permite informar Ligação na Central e preencher o campo ao efetuar o lançamento.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16611255783447)CAUSA:**

Na validação do SPED Fiscal, a mensagem é retornada quando realizado emissão/lançamentos de notas com Modelo de Documento 6 e não informado o Cód. Tipo de Ligação.
