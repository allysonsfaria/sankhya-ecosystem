---
id: "9165565831447"
titulo: "RTMMI35707050 U USUARIO NAO AUTORIZADO PARA IP2X OU IPHX ou RTMCMODELO RISKSCORING INVALIDO"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9165565831447-RTMMI35707050-U-USUARIO-NAO-AUTORIZADO-PARA-IP2X-OU-IPHX-ou-RTMCMODELO-RISKSCORING-INVALIDO"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:10:01Z"
rotulos: ["Configuração", "Contrato", "Serasa", "Financeiro", "CORE_E02092", "Verifique configurações e contrato com o SERASA", "Decodifique URL e contate SERASA para mais informações", "RTMCMODELO inválido usuário não autorizado", "Erro"]
---

# RTMMI35707050 U USUARIO NAO AUTORIZADO PARA IP2X OU IPHX ou RTMCMODELO RISKSCORING INVALIDO

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16678059731223) MENSAGEM:**

[CORE\_E02092]:

- RTMMI35707050 U USUARIO NAO AUTORIZADO PARA IP2X OU IPHX;
- RTMCMODELO RISKSCORING INVALIDO.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16678059733015) SITUAÇÃO:**

Ao consultar a "Análise de Risco Serasa" a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16678059737367) SOLUÇÃO:**

- Sobre o erro: **RTMCMODELO RISKSCORING INVALIDO**, ele ocorre devido as marcações  da tela **"Configuração Serasa"** (Caminho de acesso: Financeiro » Preferências » Configuração Serasa) não estarem devidamente selecionadas, são elas:

![Imagem 4: Sobre o erro: RTMCMODELO RISKSCORING INVALIDO , ele ocorre devido as marcações da tela "Configuração Serasa" (Caminho…](https://ajuda.sankhya.com.br/hc/article_attachments/9165061086999)

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16678059738519) IMPORTANTE:**

Vale ressaltar que essas marcações tem a ver com o contrato firmado diretamente com o SERASA.

- Sobre o erro: **RTMMI35707050 U USUARIO NAO AUTORIZADO PARA IP2X OU IPHX,** este ocorre devido a tentativa de fazer uma consulta na tela **Análise de Risco Serasa** (Caminho de acesso: Financeiro » Consultas » Análise de Risco Serasa) que o contrato firmado com a SERASA não permite. Sendo assim, verifique no contrato o que foi acordado, pois essa mensagem vem direto do SERASA.

**(1)** Segue abaixo um passo a passo que deverá ser realizado para ter mais insumos no contato direto com a equipe do SERASA:

- Pegue a URLENVIO, na tabela TSERACS, nesse campo fica a URL que o sistema está gerando e mandando para o SERASA, se tiver qualquer coisa errada o SERASA irá reclamar.

![Imagem 6: Pegue a URLENVIO, na tabela TSERACS, nesse campo fica a URL que o sistema está gerando e mandando para o SERASA, se…](https://ajuda.sankhya.com.br/hc/article_attachments/9165416629911)

- Assim que pegar essa URL no sistema, descodifique pelo site <https://www.base64decode.org/>.  Feito isso, entre em contato direto com o SERASA e solicite mais informações sobre a recusa na consulta.

![Imagem 7: Assim que pegar essa URL no sistema, descodifique pelo site https://www.base64decode.org/ . Feito isso, entre em…](https://ajuda.sankhya.com.br/hc/article_attachments/9165440392471)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16678071523991) CAUSA:**

Quando é feita consulta ou acesso com as configurações diferentes do que foi acordado em contrato com o SERASA.
