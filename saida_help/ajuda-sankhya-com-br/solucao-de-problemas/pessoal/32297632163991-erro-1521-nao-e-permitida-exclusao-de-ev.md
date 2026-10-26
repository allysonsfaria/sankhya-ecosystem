---
id: "32297632163991"
titulo: "Erro 1521 - Não é permitida exclusão de evento de Registro Preliminar de Trabalhador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32297632163991-Erro-1521-N%C3%A3o-%C3%A9-permitida-exclus%C3%A3o-de-evento-de-Registro-Preliminar-de-Trabalhador"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:46Z"
rotulos: ["Eventos", "Admissão", "eSocial", "Central do eSocial", "Erro 1521", "Não é permitida exclusão", "Início definitivo (S-2200 ou S-2300)", "evento de Registro Preliminar de Trabalhador", "se já houver evento de Admissão ou TSVE", "referenciando o mesmo evento de admissão preliminar", "Erro"]
---

# Erro 1521 - Não é permitida exclusão de evento de Registro Preliminar de Trabalhador

**MENSAGEM:**

**Erro 1521** - Não é permitida exclusão de evento de Registro Preliminar de Trabalhador se já houver evento de Admissão ou TSVE - Início definitivo (S-2200 ou S-2300) referenciando o mesmo evento de admissão preliminar.

**SITUAÇÃO:**

Esse erro ocorre quando se tenta excluir o evento S-2190 (Registro Preliminar de Trabalhador) após já ter sido enviado um evento S-2200 (Admissão) ou S-2300 (Trabalhador Sem Vínculo Empregatício) para o mesmo colaborador.

**SOLUÇÃO:**

Para corrigir esse erro, é necessário seguir uma ordem específica para a exclusão dos eventos: 

![Imagem 1: Acesse o portal do ''eSocial'' (Pessoal+''» ''Rotinas Folha''» ''Central do eSocial) e verifique todos os eventos…](https://ajuda.sankhya.com.br/hc/article_attachments/32402231400599) Acesse o portal do **''eSocial''** (Pessoal+''» ''Rotinas Folha''» ''Central do eSocial) e verifique todos os eventos enviados para esse trabalhador;

![Imagem 2: Faça a exclusão dos eventos necessários em ordem cronológica inversa , ou seja, do evento mais recente para o mais…](https://ajuda.sankhya.com.br/hc/article_attachments/32402276955671) Faça a exclusão dos eventos necessários em **ordem cronológica inversa**, ou seja, do evento mais recente para o mais antigo:

**Importante:** comece excluindo o evento S-2200 ou S-2300, conforme o caso. Somente após concluir essa exclusão com sucesso, o sistema permitirá remover o evento S-2190.

![Imagem 3: ATENÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32402276958999) **ATENÇÃO:**

Este procedimento deve ser realizado apenas quando for realmente necessário, preferencialmente no mês de admissão, e somente se ainda não houver folha calculada ou envios de eventos de alteração cadastral (S-2205) ou contratual (S-2206).

**CAUSA:**

A exclusão do registro preliminar não é permitida pelo sistema, pois já existem eventos posteriores vinculados ao mesmo contrato de trabalho.
