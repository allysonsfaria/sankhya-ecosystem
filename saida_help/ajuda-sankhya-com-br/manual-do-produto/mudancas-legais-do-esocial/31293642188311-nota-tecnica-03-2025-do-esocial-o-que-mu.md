---
id: "31293642188311"
titulo: "Nota Técnica 03/2025 do eSocial: o que muda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31293642188311-Nota-T%C3%A9cnica-03-2025-do-eSocial-o-que-muda"
trilha: "Manual do Produto > Pessoas+ > eSocial > Mudanças Legais do eSocial"
atualizado_em: "2026-09-27T19:40:40Z"
rotulos: ["Configuração", "Fiscal", "Atualização", "eSocial", "Central de Projetos", "Documentos Eletrônicos"]
---

# Nota Técnica 03/2025 do eSocial: o que muda

Em 30/01/2025 o eSocial publicou a Nota Técnica 03/2025 para apresentar ajustes nos leiautes do eSocial, garantindo maior precisão e adequação às legislações vigentes. Essas alterações visam aprimorar a estrutura dos eventos e melhorar a qualidade das informações prestadas.

Para ter acesso a todas as publicações realizadas pelo eSocial referentes a Nota Técnica acesse os links abaixo.

[**(1)**](https://www.gov.br/esocial/pt-br/documentacao-tecnica) [Documentação Técnica](https://www.gov.br/esocial/pt-br/documentacao-tecnica)

[**(1)**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf) [Manual de Orientação do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf)

[**(1)**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-03-2025/index.html#1000_infoEmpregador_inclusao_infoCadastro) [Leiaute S-1.3 atualizado Nota Técnica 03/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-03-2025/index.html#1000_infoEmpregador_inclusao_infoCadastro)

[**(1)**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-03-2025.pdf) [Nota Técnica 03/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-03-2025.pdf)

As principais mudanças incluem (eventos e campos atualizados):

**![Imagem 1: Evento S-1000 (Informações do Empregador/Contribuinte/Órgão Público): criação do campo {indPertIRRF} para atender à…](https://ajuda.sankhya.com.br/hc/article_attachments/31293841206551) Evento S-1000 (Informações do Empregador/Contribuinte/Órgão Público):** criação do campo {indPertIRRF} para atender à Instrução Normativa RFB n.º 2.239/2024.

São mudanças que impactam empregadores com as naturezas jurídicas abaixo:

- 126-0 - Fundação Pública de Direito Privado Estadual ou do Distrito Federal;
- 127-9 - Fundação Pública de Direito Privado Municipal;
- 129-5 - Fundo Público da Administração Indireta Estadual ou do Distrito Federal;
- 130-9 - Fundo Público da Administração Indireta Municipal.

Fonte: [IBGE](https://concla.ibge.gov.br/estrutura/natjur-estrutura/natureza-juridica-2021)

**![Imagem 2: Crédito do trabalhador (eConsignado):](https://ajuda.sankhya.com.br/hc/article_attachments/31323560651543) Crédito do trabalhador (eConsignado):**

**(1)** alteração no campo {nrDoc}, permitindo contratos com até 15 posições;

**(1)** S-1210 (Pagamentos de Rendimentos do Trabalho): ajustes nos grupos {penAlim}, {previdCompl}, {infoProcRet} e {planSaude} tornando obrigatório que as rubricas de pensão alimentícia, plano de saúde e previdência complementar sejam do tipo 'desconto'.

**![Imagem 3: S-5001, S-5002, S-5003, S-5011 e S-5501 (tabelas de retorno INSS, FGTS e IRRF): alterações na validação e descrição de…](https://ajuda.sankhya.com.br/hc/article_attachments/31323585446679) S-5001, S-5002, S-5003, S-5011 e S-5501 (tabelas de retorno INSS, FGTS e IRRF):** alterações na validação e descrição de campos para garantir melhor precisão nos cálculos e registros de bases do PIS/PASEP e valores de contrato (eConsignado).

**![Imagem 4: Tabelas atualizadas:](https://ajuda.sankhya.com.br/hc/article_attachments/31323585447959) Tabelas atualizadas:**

(1)** tabela 11 (Compatibilidade entre Categoria de Trabalhadores, Classif. Tributária e Tipos de Lotação**): ajuste na compatibilidade entre o código de categoria [741- Contribuinte individual - Microempreendedor individual] e a classificação tributária, permitindo o cadastro de trabalhadores nesta categoria para empregadores com classificação tributária [22-Segurado especial, inclusive quando for empregador doméstico];

(1)** tabela 21 (Códigos de Incidência Tributária da Rubrica para o IRRF):** criação do subgrupo "Dedução do rendimento tributável para uso exclusivo na Declaração de Ajuste Anual" e realocação do código [67- Plano privado coletivo de assistência à saúde].

**![Imagem 5: Regras de Validação Alteradas:](https://ajuda.sankhya.com.br/hc/article_attachments/31323560660119) Regras de Validação Alteradas:**

REGRA\_ADMISSAO\_POSTERIOR\_INICIO\_ATIVIDADES: impede admissões com datas anteriores à abertura da empresa.

REGRA\_RUBRICA\_COMPATIVEL\_CATEGORIA: ajustes para código de categoria [771-Contribuinte individual - Membro de conselho tutelar, nos termos da Lei 8.069/1990].

REGRA\_VALIDA\_ADMISSAO\_PRELIMINAR: Retorna alerta caso um evento S-2190 referente a "Empregado" ou "Agente Público" seja enviado sem o grupo {infoRegCTPS- Informações referentes ao registro eletrônico de empregados e à Carteira de Trabalho e Previdência Digital - CTPS Digital.} preenchido.

---

As **principais alterações** serão liberadas nos ambientes de produção restrita em **24/03/2025** e em ambiente de produção**22/04/2025**.

Dentre elas, destacam-se:

**![Imagem 6: S-2500 (Processo Trabalhista): criação do campo {ideSeqTrab} número sequencial atribuído pela empresa a cada conjunto…](https://ajuda.sankhya.com.br/hc/article_attachments/31293841206551) S-2500 (Processo Trabalhista):** criação do campo {ideSeqTrab} número sequencial atribuído pela empresa a cada conjunto de dados de processo trabalhista, quando for necessário enviar o mesmo processo em múltiplos S-2500, para o mesmo cpfTrab.};

**![Imagem 7: S-2501 (Informações de Tributos Decorrentes de Processo Trabalhista): ajuste no campo {perRef- referência das…](https://ajuda.sankhya.com.br/hc/article_attachments/31323560651543) S-2501 (Informações de Tributos Decorrentes de Processo Trabalhista):** ajuste no campo {perRef- referência das informações.} para melhor integração com o novo campo {ideSeqTrab-S-2500};

**![Imagem 8: S-5503 (Informações do FGTS por Trabalhador em Processo Trabalhista): alteração na origem do campo {categOrig} e…](https://ajuda.sankhya.com.br/hc/article_attachments/31323585446679) S-5503 (Informações do FGTS por Trabalhador em Processo Trabalhista):** alteração na origem do campo {categOrig} e ajustes nos valores válidos do campo {tpValorProcTrab};

**![Imagem 9: tabela 23 (Relacionamento entre Tipo de Valor do FGTS, Categoria, Origem, Código de Incidência do FGTS e Condição):…](https://ajuda.sankhya.com.br/hc/article_attachments/31323585447959) tabela 23 (Relacionamento entre Tipo de Valor do FGTS, Categoria, Origem, Código de Incidência do FGTS e Condição):** ajuste nos códigos de categoria para determinados tipos de valor.

REGRA\_REGISTRO\_PRELIMINAR: inclusão de nova alínea para melhor controle dos registros preliminares.

---

### Implementações no Pessoal+

As implementações estão sendo realizadas para atender a Nota Técnica e estarão disponíveis conforme a entrada em produção das mudanças. Há mudanças que não houve implementações, como a do evento S-1000 ligadas à natureza jurídica, que são voltadas a órgãos públicos.

Abaixo segue as implementações que serão realizadas no sistema:

**![Imagem 10: S-1210 (Pagamentos de Rendimentos do Trabalho)](https://ajuda.sankhya.com.br/hc/article_attachments/31293841206551) S-1210 (Pagamentos de Rendimentos do Trabalho)**

A partir da versão 5.26, o sistema só permitirá o cadastro de [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767) com natureza de rubrica de Pensão Alimentícia, Previdência Complementar e Plano de Saúde quando o tipo de evento for Desconto.

**![Imagem 11: crédito do trabalhador (eConsignado)](https://ajuda.sankhya.com.br/hc/article_attachments/31323560651543) crédito do trabalhador (eConsignado)**

Foi realizado ajuste no sistema para que o campo **Número do Contrato** (nrDoc) da tela [Lançamento de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/13968004985495) tenha o limite de até 15 caracteres, conforme determina o leiaute atual.

**![Imagem 12: S-2500 (Processo Trabalhista) cadastro de processo trabalhista com múltiplos contratos de trabalho para um mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/31323585446679) S-2500 (Processo Trabalhista) cadastro de processo trabalhista com múltiplos contratos de trabalho para um mesmo trabalhador**

O sistema preencherá automaticamente a sequência quando houver dois ou mais processos para o mesmo funcionário cujo contrato de trabalho, discutido no processo, não consta no eSocial através dos eventos S-2200/2300.

![Imagem 13: Para saber mais detalhes, acesse o artigo Processo trabalhista , menu Informações do Processo .](https://ajuda.sankhya.com.br/hc/article_attachments/31337990655511) Para saber mais detalhes, acesse o artigo **Processo trabalhista**, menu [Informações do Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/11592868813719-Processo-Trabalhista#informa%C3%A7%C3%B5esdoprocesso).

**![Imagem 14: S-2500 (Processo Trabalhista) Horas trabalhadas intermitentes no Processo Trabalhista](https://ajuda.sankhya.com.br/hc/article_attachments/31323585447959)  S-2500 (Processo Trabalhista) Horas trabalhadas intermitentes no Processo Trabalhista**

Com a publicação da Nota técnica 03/2025 que altera a versão S-1.3 do eSocial, a validação da classificação tributária da empresa para recepção da informação das horas trabalhadas do funcionário intermitente passa a ser por período de referência informado no pop-up, por isso o campo "Horas Trabalhadas" será apresentado em tela independentemente da classificação tributária do declarante, sendo necessário que o usuário faça o preenchimento quando o declarante no período de referência informado tiver a classificação tributária igual a 22-Segurado especial, inclusive quando for empregador doméstico.

![Imagem 15: Confira os detalhes na seção Períodos referentes às bases de cálculo do menu Informações do Contrato de Trabalho no…](https://ajuda.sankhya.com.br/hc/article_attachments/31337990655511) Confira os detalhes na seção **Períodos referentes às bases de cálculo** do menu [Informações do Contrato de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/11592868813719-Processo-Trabalhista#informa%C3%A7%C3%B5esdocontratodetrabalho) no **Processo trabalhista**.

**![Imagem 16: S-2501 (Informações de Tributos Decorrentes de Processo Trabalhista)](https://ajuda.sankhya.com.br/hc/article_attachments/31323560660119)  S-2501 (Informações de Tributos Decorrentes de Processo Trabalhista)**

O sistema impedirá inclusão, retificação e exclusão de cadastros de processos trabalhistas em que há mais de 3.000 (três mil) trabalhadores vinculados a único processo sem a reabertura do evento S-2555 (Solicitação de Consolidação das Informações de Tributos Decorrentes de Processo Trabalhista).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/31293642188311-Nota-T%C3%A9cnica-03-2025-do-eSocial-o-que-muda#top)
