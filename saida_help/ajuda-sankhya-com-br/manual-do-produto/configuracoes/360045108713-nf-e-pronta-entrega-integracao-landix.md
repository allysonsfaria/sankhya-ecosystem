---
id: "360045108713"
titulo: "NF-e Pronta Entrega - Integração Landix"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108713-NF-e-Pronta-Entrega-Integra%C3%A7%C3%A3o-Landix"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:55:03Z"
rotulos: ["Configuração", "NF-e Pronta Entrega - Integração Landix", "NF-e Pronta Entrega - Integração Landix manual", "NF-e", "XML", "SEFAZ", "Impostos", "Automação do Processamento de NF-e com Integração Landix", "Documentos Eletrônicos", "Landix"]
---

# NF-e Pronta Entrega - Integração Landix

Automatização do envio e consulta do resultado das NF-e à SEFAZ, cálculo de PIS/COFINS e geração da CHAVE NF-e das notas originadas do LMMS (Landix).

Para o funcionamento da NF-e, o NF-e Pronta Entrega necessita da correta configuração para emissão de NF-e (Empresa, TOP, Produto... etc.).

Como premissa, para o funcionamento da rotina de cálculo de impostos acontecer as alíquotas de PIS e COFINS deverão estar configuradas.

Veja a documentação completa das configurações necessárias para a emissão da Nota Fiscal Eletrônica, no Manual da NFe disponível na área restrita do site Sankhya e\ou no Help On Line do sistema Sankhya.

![Imagem 1: Veja a documentação completa das configurações necessárias para a emissão da Nota Fiscal Eletrônica, no Manual da NFe…](https://ajuda.sankhya.com.br/hc/article_attachments/9827356940951)![Imagem 2: Veja a documentação completa das configurações necessárias para a emissão da Nota Fiscal Eletrônica, no Manual da NFe…](https://ajuda.sankhya.com.br/hc/article_attachments/9827356951447)

|  | **É possível observar na imagem que a ilustração foi dividida em duas partes, onde a parte superior (passos 1 a 8 e 21 a 30) é de competência da Landix e a parte inferior (passos 9 a 20) é de competência da Sankhya.** |
| --- | --- |

---

A seguir, confira a descrição de cada etapa demonstrada na imagem acima:

**1.** O PDA (Assistente Pessoal Digital (Palm, Pocket)) descarrega a negociação e junto envia uma solicitação de autorização de NF-e.

**2.** A descarga é feita através da internet e é recebida pelo LMMS (Landix Mobile Middleware Server).

**3.** O LMMS aciona o Middleware para processar a negociação e a solicitação de autorização de NF-e.

**4.** O Middleware grava a negociação com o estado "confirmada" nas tabelas do Mitra e grava um registro na tabela de integração para enfileirar as solicitações de autorização de NF-e.

**5.** O Mitra indica para o Middleware o NUNOTA referente à negociação gravada.

**6.** O Middleware devolve ao LMMS o NUNOTA referente à negociação gravada no Mitra.

**7.** O LMMS envia através da internet o NUNOTA referente à negociação descarregada.

**8.** O PDA recebe NUNOTA para futuramente verificar se a NF-e foi autorizada e assim concretizar a venda.

**9.** De tempo em tempo um agendador da Sankhya (integrado com o web service da Sankhya que se comunica com o web service da Sefaz) verifica na tabela de integração se há solicitações de NF-e e monta um pacote com todas as solicitações de NF-e, que ainda não foram enviadas à SEFAZ.

**10.** O agendador envia através da internet o pacote com notas que necessitam de autorização da SEFAZ.

**11.** A SEFAZ recebe as solicitações de autorização de NF-e.

**12.**  A SEFAZ devolve o protocolo de recebimento de solicitação.

**13.** O agendador recebe o protocolo de recebimento da SEFAZ.

**14.** O agendador grava no banco de dados do Mitra o protocolo de recebimento das solicitações que foram recebidas.

**15.** De tempo em tempo o agendador verifica no banco de dados e monta um pacote com as solicitações que já foram enviadas para a SEFAZ e estão aguardando a resposta sobre a autorização.

**16.** O agendador envia o pacote à SEFAZ para verificar se as notas foram autorizadas.

**17.** A SEFAZ recebe o pacote e verifica se as solicitações de NF-e indicadas no pacote foram autorizadas.

**18.** A SEFAZ monta um pacote indicando as solicitações de NF-e que foram aprovadas e indicando o código de autorização de cada NF-e.

**19.** O agendador recebe o pacote com as solicitações autorizadas e os códigos de autorização da NF-e.

**20.** O agendador grava no banco de dados do Mitra a marcação das notas que foram autorizadas e os códigos das NF-e autorizadas.

**21.** O PDA descarrega as notas que estão aguardando autorização da SEFAZ e junto envia a solicitação de verificação de NF-e aprovada.

**22.** A descarga é feita através da internet e é recebida pelo LMMS (Landix Mobile Middleware Server).

**23.** O LMMS aciona o Middleware para verificar se as notas descarregadas foram autorizadas.

**24.** O Middleware conecta ao banco de dados do Mitra e verifica quais notas já foram autorizadas pela SEFAZ.

**25.** O Middleware copia do banco do Mitra os XML das notas que foram autorizadas.

**26.** O Middleware monta um envelope onde são armazenados todos os XML copiados do banco do Mitra e disponibiliza o envelope para o LMMS.

**27.** O LMMS envia através da internet, o envelope com as XML das NF-e.

**28.** O PDA recebe o envelope, identifica através dos XML as notas que foram autorizadas.

**29.** O PDA interpreta o XML, monta o arquivo de DANFE simplificado e envia para impressora.

**30.** A impressora imprime o DANFE simplificado.

---

O NF-e Pronta Entrega visa automatização do envio e consulta do resultado das NF-e à SEFAZ, cálculo de PIS/COFINS e geração da CHAVE NF-e das notas originadas do LMMS (Landix).

Ao entrar no sistema, o mesmo solicita o **"Intervalo de Execução"** para processamento (segundos entre as execuções) e a base que será executada a rotina.

![Imagem 3: Ao entrar no sistema, o mesmo solicita o "Intervalo de Execução" para processamento (segundos entre as execuções) e a…](https://ajuda.sankhya.com.br/hc/article_attachments/9460490604439)

| ``` Imagem 4: É recomendado que seja estipulado um intervalo mínimo de 15 segundos. É recomendado que seja estipulado um intervalo mínimo de 15 segundos. ``` |
| --- |

As rotinas abrangentes nesse executável são:

- Cálculo de impostos;
- Montar Chave NF-e (Notas Modelo 1 ou 1A, a responsabilidade da Chave NF-e é do LMMS (Landix));
- Enviar solicitação à SEFAZ;
- Consultar resultado na SEFAZ.

Todo o funcionamento do módulo é baseado na tabela TGFPEL, onde serão inseridos os registros:

- Nota Fiscal (Modelo 1 ou 1A);
- Nota Fiscal Eletrônica;
- Cancelamento de NF-e;
- FS-DA (Contingência).

Como se trata de Pronta Entrega, o recolhimento do ST é sempre na entrada do item.

**Processos para cada movimentação:**

**(2)** **Nota Fiscal (Modelo 1 ou 1A):** Nesta modalidade, as notas não tem obrigatoriedade de envio à SEFAZ. Então o sistema verifica os registros modelo 1 ou 1A, realiza apenas o cálculo de PIS/COFINS e avisa ao PDA que a nota está pronta para ser impressa.

**(2)** **Nota Fiscal Eletrônica:** Essas notas têm obrigatoriedade de envio à SEFAZ. O sistema verifica os registros cujo modelo seja NF-e e realiza o cálculo de PIS/COFINS. Após os cálculos de PIS/COFINS, o sistema envia as notas à SEFAZ em busca de autorização das mesmas. Na próxima etapa, o sistema realiza a consulta para verificar se a NF-e foi Aprovada, Rejeitada ou Denegada. Ao receber o resultado da consulta, o sistema avisa ao PDA se a nota está pronta para ser impressa (DANFE), se a NF-e precisa de alguma correção (Rejeição) ou se a NF-e foi inutilizada (Denegada).

(2)** Cancelamento de NF-e:** Para o cancelamento de NF-e. A solicitação de cancelamento tem a obrigatoriedade de envio à SEFAZ. O sistema solicita o cancelamento de determinada NF-e e após o retorno da SEFAZ, o sistema desfaz o financeiro e o estoque envolvido, na NF-e cancelada.

(2)** Emissão FS-DA:** tipEmiss = 5 (Contingência) Formulário de Segurança – Documento Auxiliar. Esta contingência é específica para usuários de Pronta Entrega, que por algum motivo (seja por falta de Internet, SEFAZ fora do ar, etc.) não conseguiram emitir a NF-e.

Neste caso, é emitida a contingência FS-DA, com impressão do DANFE em formulário de segurança.

O FS-DA é emitido e o PALM preenche a tabela de integração com os dados referente ao FS-DA emitido. No momento em que a situação for regularizada (conexão à Internet ou SEFAZ volte a funcionar), o FS-DA será enviado para a SEFAZ.

Observação: FS-DA - Contingência com uso do Formulário de Segurança para impressão de Documento Auxiliar do Documento Fiscal eletrônico.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108713-NF-e-Pronta-Entrega-Integra%C3%A7%C3%A3o-Landix#top)
