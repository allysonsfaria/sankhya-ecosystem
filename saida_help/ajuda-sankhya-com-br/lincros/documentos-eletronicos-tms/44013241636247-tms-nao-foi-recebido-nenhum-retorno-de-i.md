---
id: "44013241636247"
titulo: "[TMS] - Não foi recebido nenhum retorno de integração após aceite/rejeição da fatura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013241636247--TMS-N%C3%A3o-foi-recebido-nenhum-retorno-de-integra%C3%A7%C3%A3o-ap%C3%B3s-aceite-rejei%C3%A7%C3%A3o-da-fatura"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T19:51:10Z"
rotulos: ["sync_hc", "lincros", "sync_hash_b123b013d175", "lincros_13432818"]
---

# [TMS] - Não foi recebido nenhum retorno de integração após aceite/rejeição da fatura

**Menu**: Documentos Eletrônicos > Ct-es

           Financeiro > Faturas

**Objetivo**: Como resolver o erro 'Não foi recebido nenhum retorno de integração após aceite/rejeição da fatura' na integração do CT-e ou da fatura'

**Considerações**:

- Possuir o CT-e/fatura importado no sistema e que consta a mensagem de erro na integração 'Não foi recebido nenhum retorno de integração após aceite/rejeição da fatura';
- Se já faz mais de 30 minutos que um CT-/fatura foi enviado para integração e não houve um retorno de sucesso ou erro, o sistema automaticamente coloca a situação de integração para Erro e a mensagem de integração é apresentada como "Não foi recebido nenhum retorno de integração após aceite/rejeição da fatura".

Abaixo segue os procedimentos:

1. Quando ocorre essa mensagem de erro é porque ainda não foi recebido um retorno de interação pelo TMS;
2. Nestes casos, o TMS apresenta a mensagem "Não foi recebido nenhum retorno de integração após aceite/rejeição da fatura", conforme exemplo abaixo:

![Imagem 1: Nestes casos, o TMS apresenta a mensagem "Não foi recebido nenhum retorno de integração após aceite/rejeição da…](https://ajuda.sankhya.com.br/hc/article_attachments/44013229092631)

## Vamos relembrar um pouco sobre o fluxo de integração:

A etapa final, após a fatura ter sido recuperada pelo ERP, é enviar para o TMS através da API "/fatura" o método "/salvarRetorno", onde é informada se a integração foi ou não concluída.

Nestes casos, o cliente deve verificar junto ao seu TI se realmente as API's de busca das faturas estão rodando.

## O fluxo de integração via webservice segue a seguinte ordem:

1.O usuário aceita fatura e a mesma fica com status "Aguardando integração", neste momento, a fatura fica disponível para ser consumida pelo ERP  através do método "/buscarRegistrosParaIntegracao".

Neste método GET, o TMS devolve uma lista com todos OIDs (respeitando limite imposto na chamada) com faturas aguardando integração;

![Imagem 2: Neste método GET, o TMS devolve uma lista com todos OIDs (respeitando limite imposto na chamada) com faturas aguardando…](https://ajuda.sankhya.com.br/hc/article_attachments/44013204022551)

2.  Tendo o OID (conforme exemplo acima) o cliente chama o método '"/recuperarDados", enviando na requisição o 'OID' e o TMS devolve a fatura por completo (JSON completo da fatura);

3.  ERP grava a fatura e chama o método "/salvarRetornoFatura" para determinar qual status de integração tem este documento de cobrança;

4.  Necessário entender com TI do cliente se essas chamadas estão sendo realizadas, visto que uma vez disponível para integração, a fatura deve ser recuperada pelo cliente conforme fluxo descrito acima;

5.  Depois de um período, caso não tenha recebido um retorno de aceite/rejeição, a situação da fatura é alterada para "Erro durante a integração";

Caso o cliente possua integração com o Remote, algumas validações devem ser realizadas:

1. Acessar o Remote da empresa;
2. Acessar a pasta de Logs;
3. Identificar possíveis erros nos logs;
4. Validar se o Remote está sendo executado;
5. Caso tiver alguma dúvida, entrar em contato com o HelpDesk da Lincros.

**Obs.:**  Ao realizar o processo de integração de faturas a mesma fica com situação 'Aguardando Integração' até que haja o retorno do Remote ou então o Processo de Situação de Integração da Fatura seja executado (API´s).

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
