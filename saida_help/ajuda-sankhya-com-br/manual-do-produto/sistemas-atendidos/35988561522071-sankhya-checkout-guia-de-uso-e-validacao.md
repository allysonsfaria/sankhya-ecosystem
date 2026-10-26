---
id: "35988561522071"
titulo: "Sankhya Checkout: Guia de uso e validação da Reforma Tributária (IBS, CBS, IS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35988561522071-Sankhya-Checkout-Guia-de-uso-e-valida%C3%A7%C3%A3o-da-Reforma-Tribut%C3%A1ria-IBS-CBS-IS"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Sistemas atendidos"
atualizado_em: "2026-10-16T12:26:21Z"
rotulos: ["Configuração", "Impostos", "Sankhya Checkout", "IBS", "CBS", "Reforma Tributária"]
---

# Sankhya Checkout: Guia de uso e validação da Reforma Tributária (IBS, CBS, IS)

Processo de configuração do sistema Sankhya Om para habilitar o correto funcionamento dos novos impostos da Reforma Tributária (IBS, CBS e IS) no Sankhya Checkout, especificamente para a emissão de NFC-e.

**Atenção:** Embora a configuração completa dos tributos seja necessária no Sankhya Om (item 1), o imposto **IS (Imposto Seletivo)** e as regras de **impostos Monofásicos AINDA não estão implementados** no Sankhya Checkout. A funcionalidade atual está focada na manipulação correta do **IBS** e **CBS** para a NFC-e.

### 1. Pré-requisitos e Configurações no Sankhya Om

É fundamental concluir as seguintes etapas no Sankhya Om para preparar a base de dados para a transição dos novos tributos:

#### 1.1. Pré-requisitos do sistema

- **Módulo de Livros Fiscais:** Deve estar atualizado na **versão 5.16.4 ou superiores**.
  - Atenção: Caso o módulo esteja desatualizado, os novos impostos não serão calculados.
- **Habilitação da Nota Técnica:** A **Nota Técnica 2025.002-RTC - v1.10** deve ser habilitada nas configurações da empresa.
  - Local de acesso: [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), [sub-aba NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos:~:text=voltar%20ao%20subt%C3%ADtulo%5D-,Sub%2Daba%20NF%2De/NFC%2De,-Nessa%20sub%2Daba) - [Nota Técnica NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos:~:text=voltar%20ao%20subt%C3%ADtulo%5D-,Nota%20T%C3%A9cnica%20NF%2De,-Nesta%20aba%2C%20no).

#### 1.2. Habilitação e regras por Tipo de Operação (TOP)

O cálculo dos novos impostos deve ser habilitado no TOP utilizado para vendas a consumidor (modelo 65 - Nota Fiscal Eletrônica de Venda a Consumidor):

- Local de acesso: Aba **Impostos**, seção [**Reforma Tributária**](https://ajuda.sankhya.com.br/hc/pt-br/articles/34971966800151-Guia-r%C3%A1pido-prepare-seu-sistema-para-a-Reforma-Tribut%C3%A1ria) do TOP.
- **Marcações requeridas:**
  - Marcar **“Tem IBS”** (substitui o ICMS e ISS).
  - Marcar **“Tem CBS”** (substitui o PIS e COFINS).
  - Marcar **“Tem IS”** (apenas para produtos aplicáveis; necessário para futura implementação/trânsito de dados).
  - Marcar **“Tem IBS/CBS Monofásico”** (se aplicável à operação; necessário para futura implementação).

#### 1.3. Configuração de Alíquotas e Regras Específicas

- As **Alíquotas** para os novos impostos (IBS, CBS e IS) devem ser configuradas.
- **Requisito Técnico:** Como o IBS e o CBS compartilham uma única tag no XML da nota, é mandatório que **possuam o mesmo CST e CCLASSTRIB**.

### 2. Processo de carga e sincronização no Sankhya Checkout

Após a correta parametrização no Sankhya Om, é necessário realizar a carga e sincronização dos dados no Checkout:

- **2.1. Cálculo de Impostos:**
  - Na tela de [**Administração de Checkout**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053-Administra%C3%A7%C3%A3o-de-Checkout), deve-se realizar o **cálculo dos impostos** para a empresa.
  - Função: Esta ação é responsável por carregar as configurações fiscais do Sankhya Om para a base de dados local do Checkout.
- **2.2. Sincronização:**
  - No **Sankhya Checkout**, após a conclusão do cálculo dos impostos, é obrigatória a **sincronização das atualizações**.

### 3. Objetivo e Validação da Implementação

Ao cumprir os passos descritos, o sistema garante que:

- As configurações dos novos impostos (IBS, CBS, IS) são **corretamente carregadas** do Sankhya Om e transitadas para a base de dados do Checkout.
- Os dados estão disponíveis e prontos para utilização na **emissão de NFC-e para Pessoa Física**.
- O Checkout **manipula, calcula e estrutura corretamente** os dados dos novos tributos (IBS, CBS, IS) para a correta geração do **XML da NFC-e**.

### 4. Artigos relacionados

- [Guia rápido: prepare seu sistema para a Reforma Tributária – Sankhya Gestão de Negócios](https://dictionary.cambridge.org/dictionary/portuguese-english/artigo)
