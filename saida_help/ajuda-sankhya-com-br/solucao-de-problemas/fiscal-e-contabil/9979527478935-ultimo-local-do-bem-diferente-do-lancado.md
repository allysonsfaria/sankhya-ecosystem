---
id: "9979527478935"
titulo: "Último local do bem diferente do lançado na nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9979527478935-%C3%9Altimo-local-do-bem-diferente-do-lan%C3%A7ado-na-nota"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:05:12Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "TOP", "CORE_E01210", "Divergência de Local do Bem na Nota", "Erro", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Último local do bem diferente do lançado na nota

**MENSAGEM**

[CORE\_E01210]: Último local do bem diferente do lançado na nota. / O local do bem é diferente do último local alocado.

**SITUAÇÃO**

Ao lançar notas de bens (venda ou demonstração) ou realizar movimentações de ativos fixos, a mensagem de erro referente à divergência entre o local do bem e o último local alocado é apresentada.

**CAUSA**

O erro ocorre pela divergência entre o local cadastrado no bem e o último local alocado via movimentações (validado na TCIIBE), visando garantir a integridade patrimonial, quando o campo **"Atualização do bem"** na TOP está configurado com as opções de validação ativa.

**SOLUÇÃO**

**(1)** Sempre que a nota possuir bens que são validados por locais, verifique a configuração do **"Tipo de operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP). A validação do local só ocorre se o campo **"Atualização do Bem"** da TOP for igual a: 

B - Baixa/Venda
D - Transf.Entrada/Retorno
T - Transf.Saída/Remessa

![Imagem 1: (1) Sempre que a nota possuir bens que são validados por locais, verifique a configuração do "Tipo de operação - TOP"…](https://ajuda.sankhya.com.br/hc/article_attachments/9979445762711)

**(2)** Caso a configuração da TOP esteja correta, acesse a **"Consulta/Movimentação de Bem"** (Imobilizado > Rotinas > Consulta/Movimentação de Bem), localize e verifique o campo **"Local"** do bem.

**(3)** Caso o local esteja diferente do físico, realize uma movimentação de transferência para atualizar o local antes de gerar a nota.

**(4)** O sistema utiliza a tabela TCIIBE para validar o maior Nro. Único do bem; Ou seja, se o local da nota atual divergir do local registrado no histórico (maior NUNOTA), o bloqueio ocorrerá.

**(5)** Para mais detalhes sobre as opções da TOP, acesse: [Tipos de Operação - TOP – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque).
