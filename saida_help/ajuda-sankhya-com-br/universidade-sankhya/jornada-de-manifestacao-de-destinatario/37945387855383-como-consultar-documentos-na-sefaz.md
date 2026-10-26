---
id: "37945387855383"
titulo: "Como consultar documentos na SEFAZ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37945387855383-Como-consultar-documentos-na-SEFAZ"
trilha: "Universidade Sankhya > Jornada de Manifestação de Destinatário (MD-e)"
atualizado_em: "2026-08-18T12:40:36Z"
rotulos: ["Configuração", "Consulta", "Fiscal", "NF-e", "XML", "SEFAZ"]
---

# Como consultar documentos na SEFAZ

## Consulta de Documentos Fiscais

#### Por que a consulta de NF-e é essencial para a gestão fiscal?

A consulta de NF-e no ERP Sankhya deve ser entendida não apenas como uma rotina operacional, mas como um mecanismo de gestão fiscal e de controle de riscos. A SEFAZ disponibiliza as notas destinadas ao CNPJ do contribuinte dentro de parâmetros técnicos, como limitação de volume, periodicidade e necessidade de manifestação para manutenção do acesso ao XML. O sistema centraliza esse processo, permitindo que a empresa atue de forma estruturada e integrada.

O objetivo da consulta é fornecer visibilidade antecipada e confiável sobre os documentos fiscais recebidos, viabilizando planejamento de recebimentos, conferência de obrigações acessórias e mitigação de riscos de passivos fiscais.

Do ponto de vista de gestão, essa funcionalidade é essencial para:

- **Monitoramento de fornecedores:** identificar emissões não comunicadas previamente, assegurando controle sobre a entrada de mercadorias.
- **Prevenção de passivos:** detectar e bloquear notas emitidas indevidamente contra o CNPJ da empresa.
- **Eficiência nos processos de compras:** integrar automaticamente os XMLs ao ERP, otimizando o fluxo de conferência e registro.
- **Confiabilidade das informações fiscais:** reduzir intervenções manuais e dependência de consultas diretas ao portal da SEFAZ.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Consultar Documentos**

**Acesse:** Comercial » Rotinas » **Configuração MD-e/DF-e** 

- Clique no botão “**Consultar Documentos**” (Consultar documentos na SEFAZ)
- No pop-up apresentado, selecione e consulte a empresa e o tipo de documento a ser consultado

2. **Consulta Direta**

- Clique no botão “**Consulta Direta**” (Consultar documentos na Sefaz)
- Informe os campos obrigatórios:

  - **Empresa**
  - **Chave do Documento**
  - **Data do Documento**
  - **Tipo documento**
  - **Intervalo de NSU**, se necessário
- Clique em “**Consultar**” para buscar o documento fiscal.

**Atenção!**

- A base de treinamento opera em modo de homologação e não possui certificado digital válido. Por esse motivo, o retorno da consulta não será efetivo.
- No uso operacional, a mensagem exibida será de que a consulta foi realizada com sucesso e, nas linhas de registro, serão apresentados os campos **Sequência, Empresa, Chave NF-e e Motivo da Resposta**. Este último será preenchido com informações referentes às notas ou conhecimentos, incluindo autorizações de documentos posteriores ou o resumo de eventos associados.

**Importante**

Em ambiente de produção, conforme a configuração realizada na preparação desta jornada, os documentos consultados são baixados automaticamente e disponibilizados na rotina **Portal de Importação de XML**.

No entanto, para seguirmos a jornada em base de treinamento, o processo será simulado por meio da inserção manual do documento na próxima aula.
