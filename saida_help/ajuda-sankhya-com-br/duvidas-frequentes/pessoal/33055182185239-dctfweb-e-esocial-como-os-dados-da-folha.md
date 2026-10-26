---
id: "33055182185239"
titulo: "DCTFWeb e eSocial: Como os Dados da Folha São Transmitidos à Receita Federal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33055182185239-DCTFWeb-e-eSocial-Como-os-Dados-da-Folha-S%C3%A3o-Transmitidos-%C3%A0-Receita-Federal"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-09-27T21:37:16Z"
rotulos: ["Receita Federal", "Impostos", "eSocial", "Folha de Pagamento", "DCTFWeb", "Documentos Eletrônicos"]
---

# DCTFWeb e eSocial: Como os Dados da Folha São Transmitidos à Receita Federal

#### **(1)** Introdução

A **DCTFWeb** (Declaração de Débitos e Créditos Tributários Federais Web) é a obrigação acessória da Receita Federal que **substitui a GFIP** para recolhimento de contribuições previdenciárias. Seu preenchimento não é feito manualmente: **os dados são alimentados automaticamente pelos sistemas do eSocial e da EFD-Reinf**, a partir dos eventos enviados pelas empresas.

Entender **como os dados da folha alimentam a DCTFWeb** é essencial para garantir a correta apuração e evitar divergências ou penalidades.

#### **(1)**Fluxo de Integração: da Folha à Receita

(1)** Envio dos Eventos ao eSocial**

- O sistema de folha de pagamento envia os eventos periódicos;
- S-1200 – Remuneração do trabalhador;
- S-1210 – Pagamento do trabalhador;
- S-2299 / S-2399 – Rescisão ou término de contrato.

**Esses eventos contêm as informações de remuneração e encargos previdenciários.**

(2)** Consolidação no Ambiente Nacional do eSocial**

- O eSocial processa as informações e **gera a base de cálculo para INSS** patronal e descontado.

(3)** Transmissão à Receita via DCTFWeb**

- A Receita Federal importa os débitos automaticamente para a **DCTFWeb** no ambiente do **e-CAC;**
- Também são importados créditos (ex: salário-maternidade, retenções de nota, compensações).

(4)** Apuração e Geração da Guia (DARF Previdenciário)**

- A empresa acessa a **DCTFWeb**, valida os débitos e **emite o DARF único** com vencimento até o **dia 20 do mês seguinte** à competência.

#### **(1)**Eventos que Alimentam a DCTFWeb

| Evento | Finalidade |
| --- | --- |
| `S-1200` | Define a **remuneração mensal** e a base de cálculo do INSS |
| `S-2299` | Define os valores de INSS incidentes na **rescisão contratual** |
| `S-2399` | Trata término de contrato (sem vínculo empregatício) |
| `S-1210` | Não alimenta débitos, mas é obrigatório para cruzamento com IRRF |
| `EFD-Reinf` | Complementa débitos de **autônomos, PJ, retenções** etc. |

#### **(1)**Prazo de Envio e Geração da DCTFWeb

| Etapa | Prazo limite |
| --- | --- |
| Fechamento da folha (S-1299) | Até o dia 15 do mês seguinte à competência |
| Transmissão da DCTFWeb | Automática após o fechamento |
| Emissão do DARF | Até o dia 20 |

**Não há envio manual da DCTFWeb**: ela é gerada **somente após o fechamento da folha no eSocial** com o evento **S-1299**.

#### **(1)**Erros e Divergências Comuns

- **Falta de envio de eventos (S-1200, S-2299)** → Débito não gerado na DCTFWeb;
- **Fechamento do eSocial sem todos os eventos enviados** → INSS não apurado corretamente;
- **Erro de classificação tributária ou FPAS incorreto** → Cálculo errado de terceiros;
- **Compensações indevidas** → Impede transmissão ou exige retificação;
- **Pagamento fora do prazo** → Gera multa automática.

#### Boas Práticas

- Validar o envio e aceite de **todos os eventos periódicos no eSocial** antes do fechamento;
- Conferir as bases de cálculo entre o sistema de folha e a **prévia da DCTFWeb;**
- Manter atualizadas as tabelas de **FPAS, FAP, RAT e CNPJ;**
- Gerar relatórios de auditoria antes do S-1299;
- Acompanhar a situação das declarações no **e-CAC > DCTFWeb > Situação da Declaração.**
