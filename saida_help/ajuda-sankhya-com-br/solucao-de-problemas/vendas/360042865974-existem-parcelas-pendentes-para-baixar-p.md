---
id: "360042865974"
titulo: "Existem parcelas pendentes para baixar, porém o usuário não tem permissão para baixar títulos de receita."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865974-Existem-parcelas-pendentes-para-baixar-por%C3%A9m-o-usu%C3%A1rio-n%C3%A3o-tem-permiss%C3%A3o-para-baixar-t%C3%ADtulos-de-receita"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:43Z"
rotulos: ["#RevisadoGui", "Configuração", "Segurança", "Movimentação Financeira", "Financeiro", "Controle de Acesso", "Falta de permissão para baixar títulos", "Ajustar permissões do usuário", "Deslogar/logar e confirmar nota", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Existem parcelas pendentes para baixar, porém o usuário não tem permissão para baixar títulos de receita.

##### MENSAGEM:

Existem parcelas pendentes para baixar, porém o usuário não tem permissão para baixar títulos de receita

##### SITUAÇÃO:

Ao tentar realizar a **"baixa de títulos financeiros"** (via portal de vendas ao confirmar uma nota), o sistema impede a operação.

**(1)** Acesse: Configurações » Controle de Acesso » Usuários

**(2)** Aba: **"Segurança"**,  verifique os acessos a baixas de: **Receitas.**

![Imagem 1: (2) Aba: "Segurança" , verifique os acessos a baixas de: Receitas.](https://ajuda.sankhya.com.br/hc/article_attachments/39599639630487)

**(2)** Acesse: Configurações » Controle de Acesso » Acessos

**(2)** Selecione **"**[**Movimentação Financeira**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)**"**

![Imagem 2: (2) Selecione " Movimentação Financeira "](https://ajuda.sankhya.com.br/hc/article_attachments/15660526257559)

**(2)** Selecione o usuário e marque a opção de **"Baixa (todos)"** ou caso queira manter somente para Receitas, marque **Baixa de Receitas"**

![Imagem 3: (2) Selecione o usuário e marque a opção de "Baixa (todos)" ou caso queira manter somente para Receitas, marque Baixa…](https://ajuda.sankhya.com.br/hc/article_attachments/15660495051159)

**(3)** Após os ajustes, solicite ao usuário deslogar/logar novamente no sistema e efetuar a confirmação da Nota novamente.

##### CAUSA:

Ocorre quando o **"**[**Tipo de Negociação**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)**"** utilizado na nota está com a marcação **"Baixa na Confirmação"** nas parcelas, então quando a nota for confirmada, o sistema realizará a abertura da tela para baixar os títulos financeiros da nota e o usuário não tendo permissão para baixa, ocorrerá a mensagem.
