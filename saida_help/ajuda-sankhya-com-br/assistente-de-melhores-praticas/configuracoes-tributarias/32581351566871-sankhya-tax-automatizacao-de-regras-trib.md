---
id: "32581351566871"
titulo: "Sankhya Tax - Automatização de Regras Tributárias em Implantação (ICMS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32581351566871-Sankhya-Tax-Automatiza%C3%A7%C3%A3o-de-Regras-Tribut%C3%A1rias-em-Implanta%C3%A7%C3%A3o-ICMS"
trilha: "Assistente de Melhores Práticas > Configurações Tributárias"
atualizado_em: "2026-07-22T14:30:57Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "XML", "ICMS", "Impostos"]
---

# Sankhya Tax - Automatização de Regras Tributárias em Implantação (ICMS)

### Descrição

A funcionalidade **ICMS** permite a importação e análise de documentos fiscais (XML) com o objetivo de sugerir regras de ICMS conforme a legislação vigente. Através de um processo automatizado e validado pela ASIS, o sistema identifica divergências e propõe correções tributárias, oferecendo segurança e agilidade na criação das regras fiscais.

![e5e88f84-26c0-4fef-b3bb-ac623583c4d0](https://ajuda.sankhya.com.br/hc/article_attachments/32581404227735) Esta funcionalidade permite uma única instalação. Então, reúna as NF-es de **TODAS as empresas** em um único arquivo ZIP antes da sua execução.

Essa melhor prática permite:

- Importar documentos fiscais em lote.
- Validar os cenários tributários com apoio da ASIS.
- Visualizar divergências e aplicar correções recomendadas.
- Criar agrupamentos de NCMs ou grupos de produtos com regras otimizadas.
- Instalar as regras diretamente no sistema.

### Como instalar

1. Clique em **"Iniciar"**.
2. Faça o upload de um arquivo compactado (ZIP) contendo os XMLs das notas fiscais.
3. Aguarde a análise automática dos documentos e a validação dos cenários tributários com a ASIS.
4. Revise os cenários:

4.1 Cenários **"Conforme"** estão em conformidade com a legislação.

4.2 Cenários **"Com divergência"** devem ser revisados e corrigidos manualmente ou por meio das sugestões ASIS.

5. Aplique as correções sugeridas, se desejar.
6. Visualize a recomendação de agrupamento de regras:

6.1 Por NCMs.

6.2 Por Grupos de ICMS dos produtos + NCMs.

7. Revise o resumo da auditoria e clique em **"Instalar"** para finalizar a configuração.

### Detalhes da instalação

**Tabelas atualizadas**

- **TGFICM – Alíquotas de ICMS**
  • Inclusão das novas regras criadas com base nos agrupamentos recomendados.
  • Atualização das regras existentes, se aplicável.
- **TGFPRO – Produtos**
  • Vinculação dos produtos aos grupos de ICMS criados, se for o caso.

**![995dfb79-29b4-43bb-afbe-10f31d50936f](https://ajuda.sankhya.com.br/hc/article_attachments/32581367051799) Vale saber**

Tenha atenção redobrada ao reunir os XMLs das notas fiscais, pois apenas um único arquivo ZIP é permitido para a instalação. Estrategicamente, pense em como agrupar as NCMs e os grupos de produtos para otimizar suas regras de ICMS e facilitar futuras análises.
