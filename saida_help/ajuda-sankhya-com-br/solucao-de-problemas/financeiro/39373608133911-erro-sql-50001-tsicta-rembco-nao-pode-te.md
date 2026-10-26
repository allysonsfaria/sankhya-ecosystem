---
id: "39373608133911"
titulo: "[ERRO] SQL-50001 TSICTA.REMBCO nao pode ter o valor atualizado para menor!! CODCTABCOINT: XX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39373608133911--ERRO-SQL-50001-TSICTA-REMBCO-nao-pode-ter-o-valor-atualizado-para-menor-CODCTABCOINT-XX"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-10-06T14:01:31Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "Financeiro", "Erro", "Artigo criado KCS", "Financeiro - KCS"]
---

# [ERRO] SQL-50001 TSICTA.REMBCO nao pode ter o valor atualizado para menor!! CODCTABCOINT: XX

**Mensagem**

[ERRO] SQL-50001 TSICTA.REMBCO não pode ter o valor atualizado para menor!! CODCTABCOINT: XX

**Situação**

O erro ocorre ao tentar realizar o credenciamento de uma conta pelo Assistente de Melhores Práticas.

**Solução**

**(1)** Acesse a tela "**Contas**" (Configurações » Cadastros » Bancários » Contas) e localize a conta bancária que está sendo utilizada no credenciamento. Na sub-aba Intercâmbio Eletrônico de Dados (EDI), verifique o campo "Último Boleto".
![Imagem 1: (1) Acesse a tela " Contas " (Configurações » Cadastros » Bancários » Contas) e localize a conta bancária que está…](https://ajuda.sankhya.com.br/hc/article_attachments/44027851342103)

**(2)**  Retorne à tela do Assistente de Melhores Práticas, informe no campo correspondente exatamente o mesmo número que você encontrou na tela de Contas.

![Imagem 2: (2) Retorne à tela do Assistente de Melhores Práticas, informe no campo correspondente exatamente o mesmo número que…](https://ajuda.sankhya.com.br/hc/article_attachments/44027851342487)

**(3)** Clique em Avançar/Instalar para concluir o credenciamento da conta.

**Causa**

O problema acontece porque a numeração do "Último Boleto" preenchida na tela do Assistente é inferior à numeração que já está cadastrada e validada na tela de Contas. Como medida de segurança (para evitar quebra de sequência ou duplicidade), o sistema bloqueia atualizações de numeração para valores menores.
