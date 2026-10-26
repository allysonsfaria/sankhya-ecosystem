---
id: "25618080902807"
titulo: "Erro 183 - Ação não permitida. É necessário que o trabalhador esteja em atividade na data do afastamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25618080902807-Erro-183-A%C3%A7%C3%A3o-n%C3%A3o-permitida-%C3%89-necess%C3%A1rio-que-o-trabalhador-esteja-em-atividade-na-data-do-afastamento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:18:38Z"
rotulos: ["eSocial", "Configuração Funcionários", "Ação não permitida. É necessário que o trabalhador esteja em atividade na data do afastamento", "Erro 183", "Erro", "Afastamento Temporário", "Artigo atualizado KCS", "Sankhya RH - KCS", "Central de Projetos"]
---

# Erro 183 - Ação não permitida. É necessário que o trabalhador esteja em atividade na data do afastamento

[183] Ação não permitida. É necessário que o trabalhador esteja em atividade na data do afastamento.

### SITUAÇÃO

Esta mensagem ocorre ao tentar enviar o evento **"S-2230"** (Afastamento Temporário) para o eSocial. O sistema identifica que o trabalhador **não está com status "em atividade"** na data informada para o início do afastamento, impedindo o envio do evento.

### SOLUÇÃO

A solução varia conforme a situação identificada. Verifique qual cenário se aplica ao seu caso:

**(1)**  Verifique se a data do afastamento está correta.

**(2)**  Verifique se no portal do eSocial o funcionário está com afastamento em aberto.

Empregado **>>**Gestão de Empregados **>>**Busque pelo CPF do Funcionário **>>**Afastamento Temporário **>>**avalie os afastamentos lançados e suas datas de início e fim.

![Imagem 1: Empregado >> Gestão de Empregados >> Busque pelo CPF do Funcionário >> Afastamento Temporário >> avalie os afastamentos…](https://ajuda.sankhya.com.br/hc/article_attachments/40922722796311)

**(3)** Se o funcionário estiver com um afastamento sem data fim no portal do esocial, informe primeiramente a data fim do afastamento em aberto, para depois conseguir enviar o novo afastamento. Para isso:

     Entre na tela de ocorrência, verifique se o afastamento sem data fim no portal eSocial ainda está sem data de retorno. Se sim, informe a data fim do afastamento e gere os eventos S2230, para que seja feita a inclusão do fim do afastamento.

      Se na tela de ocorrências, o afastamento já tiver com data final informada e não gerou o S-2230 para envio, entre em contato com o suporte para auxílio na tratativa.

### CAUSA

O erro ocorre porque o eSocial identifica que o trabalhador **não está com status "em atividade"** na data do novo afastamento. O eSocial exige que o trabalhador esteja com status "em atividade" para aceitar um novo evento de afastamento, garantindo a **consistência cronológica** dos eventos trabalhistas.
