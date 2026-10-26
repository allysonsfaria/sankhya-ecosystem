---
id: "42892126435095"
titulo: "Processo trabalhista no eSocial: o que é e como funciona"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42892126435095-Processo-trabalhista-no-eSocial-o-que-%C3%A9-e-como-funciona"
trilha: "Manual do Produto > Pessoas+ > Processos Trabalhistas > Processo Trabalhista no eSocial"
atualizado_em: "2026-09-27T19:59:24Z"
rotulos: ["Processo Trabalhista", "br.com.sankhya.ProcessoTrabalhista", "S-3500 – Exclusão de Eventos de Processo Trabalhista", "S-2500 – Processo Trabalhista", "S-2501 – Informações dos Tributos Decorrentes de Processo Trabalhista", "S-5501 – Informações de Tributos Decorrentes de Processo Trabalhista"]
---

# Processo trabalhista no eSocial: o que é e como funciona

O **Processo Trabalhista** no eSocial permite que o empregador informe decisões judiciais e acordos trabalhistas que resultem no reconhecimento ou alteração de informações relativas ao vínculo de trabalho ou na necessidade de recolhimento de **FGTS, contribuições previdenciárias e Imposto de Renda**.

Essa obrigação é tratada no eSocial por meio de eventos específicos e é independente das demais rotinas de folha. Portanto, o processamento de um processo trabalhista não interfere no cálculo ou no fechamento da folha de pagamento.

No **Pessoal+**, o processo é cadastrado na rotina **Processo Trabalhista** (Pessoal+ > Rotinas Folha), que reúne as informações necessárias para geração dos eventos correspondentes ao eSocial.

#### Quando é necessário informar um processo trabalhista?

A informação deve ser enviada quando, em decorrência de um processo trabalhista ou de uma demanda submetida à **Comissão de Conciliação Prévia (CCP)** ou ao **Núcleo Intersindical (NINTER)**, o declarante precisar:

- reconhecer ou alterar informações relativas ao vínculo trabalhista;
- recolher FGTS;
- recolher contribuição previdenciária, inclusive destinada a terceiros; ou
- realizar a retenção de Imposto de Renda da pessoa física.

| ℹ️ **Nota**  Para que a obrigação se aplique, a decisão judicial deve estar transitada em julgado, ou o acordo deve estar homologado — no caso de acordo sindical — ou celebrado perante a CCP ou o NINTER. |
| --- |

O processo deve estar relacionado à **Justiça do Trabalho** ou às demandas de CCP/NINTER abrangidas pela obrigação. Processos de competência da Justiça Comum ou da Justiça Federal não são informados por esses eventos.

#### Quem deve transmitir as informações?

A responsabilidade pela transmissão das informações do processo trabalhista é do declarante responsável pelo cumprimento da obrigação decorrente da decisão ou acordo, inclusive nos casos em que houver responsabilidade indireta.

#### Quais eventos do eSocial estão relacionados ao Processo Trabalhista?

A obrigação envolve quatro eventos:

- **S-2500 – Processo Trabalhista**

  O **S-2500** registra as informações do processo, do trabalhador e do contrato de trabalho, incluindo alterações determinadas pela decisão judicial ou pelo acordo.

  É gerado um evento **S-2500 para cada trabalhador (CPF)** envolvido no processo. Portanto, é possível cadastrar mais de um trabalhador no mesmo processo. Nesse caso, o eSocial considera as informações de cada trabalhador individualmente para a geração dos eventos.

  O envio do S-2500 é obrigatório mesmo quando o processo não resultar em recolhimento de contribuição previdenciária, FGTS ou Imposto de Renda.  Deve ser realizado até o dia 15 do mês subsequente ao trânsito em julgado da decisão, à homologação do acordo, à decisão homologatória dos cálculos de liquidação ou à celebração do acordo perante CCP ou NINTER.
- **S-2501 – Informações dos Tributos Decorrentes de Processo Trabalhista**

  O **S-2501** registra os valores de contribuição previdenciária e Imposto de Renda decorrentes do processo.

  É gerado um evento **S-2501 por processo trabalhista**, independentemente da quantidade de trabalhadores envolvidos.

  Esse evento deve ser utilizado **somente quando houver tributos a recolher**. Ele é informado após o S-2500 e pode contemplar diferentes referências de pagamento quando houver parcelamento dos valores decorrentes da decisão ou acordo.

  O envio deve ser realizado até o dia 15 do mês subsequente à data de pagamento dos valores determinados na decisão ou no acordo
- **S-3500 – Exclusão de Eventos de Processo Trabalhista**

  O **S-3500** é utilizado para excluir informações enviadas anteriormente nos eventos S-2500 e S-2501, tornando-as sem efeito perante o eSocial.
- **S-5501 – Informações de Tributos Decorrentes de Processo Trabalhista**

  O **S-5501** é um evento de retorno do eSocial. Ele apresenta as informações dos tributos apurados a partir do S-2501.

#### Como funciona o Processo Trabalhista no Pessoal+?

No Pessoal+, o processo trabalhista é cadastrado em uma rotina própria, que reúne as informações necessárias para geração dos eventos do eSocial.

De forma geral, o fluxo envolve:

1. **Cadastro do processo** — informe os dados do declarante e do processo.
2. **Cadastro do trabalhador** — informe os dados do trabalhador envolvido no processo.
3. **Inclusão de dependentes** — quando aplicável, importe ou cadastre os dependentes.
4. **Cadastro do contrato de trabalho** — informe um ou mais contratos relacionados ao processo, conforme a decisão ou acordo.
5. **Confirmação do processo** — após a confirmação, as informações ficam aptas para geração do **S-2500**.
6. **Informações de tributos** — quando houver contribuição previdenciária ou Imposto de Renda a recolher, informe os dados necessários para geração do **S-2501**.
7. **Envio ao eSocial** — os eventos são tratados e enviados pela rotina de integração com o eSocial.

   | **⚠️** **Atenção**  O preenchimento deve considerar as informações determinadas na decisão judicial, ata ou acordo. O Pessoal+ realiza o tratamento dessas informações conforme as regras do sistema e do eSocial. |
   | --- |

Acesse os artigos abaixo para conhecer cada etapa do processo no Pessoal+:

| Artigo | O que você encontra |
| --- | --- |
| [**Cadastro de Processo Trabalhista**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42632245838871) | Como cadastrar o processo, o declarante e o trabalhador. |
| [**Inclusão de Dependentes do Trabalhador no Processo Trabalhista**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42862840302615) | Como importar ou incluir manualmente os dependentes. |
| [**Informações do Contrato de Trabalho no Processo Trabalhista**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42634479723671) | Como cadastrar os contratos e as informações determinadas no processo. |
| [**Informações de Tributos Decorrentes de Processo Trabalhista**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42834315267351) | Como informar períodos, bases de cálculo, tributos e referências de pagamento para o S-2501. |
| [**Consulta e Exclusão de Processos Trabalhistas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42844767586071) | Como consultar, editar e excluir processos cadastrados. |

### Artigos Relacionados

- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175-Central-do-eSocial)
- [Documentação oficial do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-11-2026-retificada.pdf)
  - [S-2500 - Processo Trabalhista](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-nt-06-2026-rev-09-04-2026/index.html#evtProcTrab)
  - [S-2501 - Informações de Tributos Decorrentes de Processo Trabalhista](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-nt-06-2026-rev-09-04-2026/index.html#evtContProc)
  - [S-3500 - Exclusão de Eventos - Processo Trabalhista](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-nt-06-2026-rev-09-04-2026/index.html#evtExcProcTrab)
  - [S-5501 - Informações Consolidadas de Tributos Decorrentes de Processo Trabalhista](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-nt-06-2026-rev-09-04-2026/index.html#evtTribProcTrab)
