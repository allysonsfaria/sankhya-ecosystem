---
id: "33152358294167"
titulo: "Eventos de Cadastro no eSocial: S-1000, S-1005 e S-1020"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33152358294167-Eventos-de-Cadastro-no-eSocial-S-1000-S-1005-e-S-1020"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-10-06T04:29:38Z"
rotulos: ["Configuração", "Eventos", "eSocial", "Cadastro", "S-1000 S-1005 e S-1020", "eventos iniciais de cadastro", "Eventos de Cadastro no eSocial:", "eventos de tabela", "Central de Projetos"]
---

# Eventos de Cadastro no eSocial: S-1000, S-1005 e S-1020

O eSocial ajuda a organizar suas informações por meio de eventos eletrônicos. Os **eventos iniciais de cadastro** (ou eventos de tabela) são fundamentais para que os eventos periódicos e não periódicos sejam processados de maneira adequada. Entre os principais eventos de estrutura, temos o **S-1000 (Empregador)**, **S-1005 (Estabelecimento)** e **S-1020 (Lotação Tributária)**.

#### Evento S-1000 – Informações do Empregador/Contribuinte/Órgão Público:

É responsável por registrar os **dados cadastrais e classificações fiscais** da empresa no eSocial. Este evento é o **primeiro a ser enviado**, pois identifica o empregador no ambiente do governo.

(1)** Informações enviadas:**

- Tipo de inscrição (CNPJ/CPF);
- Nome empresarial ou nome civil;
- Natureza jurídica;
- Classificação tributária (ex: 01 – Empresa enquadrada no Simples Nacional);
- Indicativo de desoneração da folha (CPRB);
- Informações sobre cooperativas, entidades imunes/isentas;
- Informações do responsável legal;
- Dados de contato (telefone, e-mail);
- Informações do ambiente de produção/restrito;
- Data de início da validade do evento.

**Observação:** Alterações de dados cadastrais exigem envio de nova versão do S-1000 com nova data de validade.

#### Evento S-1005 – Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos

Este evento tem a função de informar os **estabelecimentos** (CNPJ completo), obras ou unidades administrativas relacionadas ao empregador. É importante para garantir a apuração correta do FGTS, INSS, RAT e outros encargos.

(1)** Informações enviadas:**

- CNPJ do estabelecimento ou CEI de obra de construção civil;
- Tipo de inscrição (CNPJ, CAEPF, CNO, etc.);
- CNAE preponderante;
- Fator acidentário de prevenção (FAP);
- Alíquota de RAT (Riscos Ambientais do Trabalho);
- Indicativo de atividade econômica preponderante;
- Indicativo de obra (própria ou empreitada);
- Indicativo de empresa com processo judicial;
- Informações de contato da unidade.

**Observação:** Cada estabelecimento precisa estar ativo e devidamente cadastrado para envio de eventos periódicos como o S-1200 (remuneração).

#### Evento S-1020 – Tabela de Lotações Tributárias

Este evento trata das **lotações tributárias** nas unidades da empresa. Ele estabelece como os encargos (INSS, terceiros, FGTS) serão coletados por centro de custo, departamento ou filial.

**(1)** **Informações enviadas:**

- Código interno da lotação (ID único no sistema);
- CNPJ do estabelecimento a que pertence;
- Código de FPAS (Fundo de Previdência e Assistência Social);
- Terceiros (códigos de entidade como SENAI, SEBRAE, etc.);
- Indicativo de desoneração da folha (CPRB);
- Indicativo de contribuição substituída (produção rural, exportações);
- Código de lotação conforme Tabela 10 do eSocial;
- Processo judicial, se houver, relacionado à contribuição.

**Observações:**

- A correta configuração de lotações evita erros na **DCTFWeb** e **recolhimentos indevidos de encargos**.
- Alterações de FPAS, terceiros ou CPRB implicam envio de nova versão com data de início da nova validade.

#### Importância dos Eventos de Cadastro

Esses eventos **não possuem valores**, mas são **importantes** para os cálculos e validações dos eventos periódicos como:

- **S-1200** – Remuneração;
- **S-1210** – Pagamentos;
- **S-1299** – Fechamento da folha;
- **S-1250** – Aquisição de produção rural, etc.
