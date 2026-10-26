---
id: "360044109774"
titulo: "Para o estado do '  ' o serviço de consulta de cadastro não está disponível"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109774-Para-o-estado-do-o-servi%C3%A7o-de-consulta-de-cadastro-n%C3%A3o-est%C3%A1-dispon%C3%ADvel"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:24Z"
rotulos: ["#PUBLIFER", "CORE_E04940", "Configuração", "Parceiro", "Importação", "SEFAZ", "Indisponibilidade do Serviço de Consulta de Cadastro por Estado", "Erro"]
---

# Para o estado do '  ' o serviço de consulta de cadastro não está disponível

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16947384309143) MENSAGEM:**

[CORE\_E04940] Para o estado do '  ' o serviço de consulta de cadastro não está disponível.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16947384312599) SITUAÇÃO:**

Ao utilizar a rotina **"Importar dados do parceiro"** a mensagem poderá ser retornada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16947384318871) SOLUÇÃO:**

![Imagem 4: Se essa mensagem foi retornada, esse serviço não está disponível para o respectivo Estado.](https://ajuda.sankhya.com.br/hc/article_attachments/16947391115671) Se essa mensagem foi retornada, esse serviço não está disponível para o respectivo Estado.

- Estados que não possuem o serviço: AL, DF, PA, PI, RJ, RO, SE, TO, RR;
- Estados que permitem a importação em ambiente de Produção e Homologação: AM, BA, CE, GO, MG, MS, MT, PE, PR, RS, SP;
- Estados que só permitem a importação em ambiente de Produção: AC, PB, PE, RN, SC.

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16947391117335) IMPORTANTE:**

No parâmetro **"UF's não possuem url para consulta de cadastro - UFNAOTEMCONSCAD"** deverão ser relacionadas as UF's que não possuem o serviço, sendo separadas por vírgula. Caso uma determinada UF passe a ter o serviço, retire a da lista.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16947384324503) CAUSA:**

Ao utilizar a rotina Importar dados do parceiro a mensagem poderá ser retornada, caso a UF do respectivo Estado não tenha esse serviço de consulta disponível.
