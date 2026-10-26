---
id: "360055968653"
titulo: "E0061: Verificação da situação da nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360055968653-E0061-Verifica%C3%A7%C3%A3o-da-situa%C3%A7%C3%A3o-da-nota"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:28:08Z"
rotulos: ["#criadoRoger", "Configuração", "Impostos", "TOP", "Prefeituras", "NFS-e", "Correção de Erro de Situação Fiscal", "Solução para Erro E0061", "Erro"]
---

# E0061: Verificação da situação da nota

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18586832193175) MENSAGEM**:

Erro NFS- E prefeitura de Londrina:

E0061: Verificação da situação da nota
Possível solução: Para esta nota a situação pode estar como: Tributado Tomador(tt).

**![Imagem 2: CAUSA: Ocorre quando a situação enviada à prefeitura esta incorreto na tag SITUAÇAO.](https://ajuda.sankhya.com.br/hc/article_attachments/18586832203671) CAUSA:**Ocorre quando a situação enviada à prefeitura esta incorreto na tag SITUAÇAO.

Ex: <situacao>tp</situacao> onde deveria ser <situacao>tt</situacao>

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18586832224023) SOLUÇÃO:**

![Imagem 4: Acesse o Tipo de Operação em Comercial » Arquivo » Cadastros » Tipos de Operação - TOP Aba: Natureza da Operação…](https://ajuda.sankhya.com.br/hc/article_attachments/18586848834711) Acesse o Tipo de Operação em Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
Aba: [Natureza da Operação ISS/Município](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanaturezadaoperaoissmunicpio)
Observação: a ativação do parâmetro **"Utilizar Cód. Nat. Operação ISS por Top/Empresa - NATOPEISSTOPEMP"** fará com que a aba **"Natureza da Operação ISS/Município"** seja apresentada no Cadastro de Tipos de Operação - TOP,

**Preencha o campo:** Empresa, para que possa ser selecionado uma das opções de Natureza de Operação, e selecione a opção 'Tributado Tomador (tt).

Exemplo de script - Solicitar apoio de um consultor para alinhar com a prefeitura os códigos que são aceitos, para a correta criação do script.

**Insert into TGFNAS (CODNATOPER, SEQUENCIA, CODMUNFIS, DESCRNATOPER) Values ('0', 1, 4300604, 'Tributada Integralmente');**

![Imagem 5: Após os ajustes , excluir a nota e fazer uma nova nota e transmiti-lo.](https://ajuda.sankhya.com.br/hc/article_attachments/18586848843159)Após os ajustes , excluir a nota e fazer uma nova nota e transmiti-lo.
