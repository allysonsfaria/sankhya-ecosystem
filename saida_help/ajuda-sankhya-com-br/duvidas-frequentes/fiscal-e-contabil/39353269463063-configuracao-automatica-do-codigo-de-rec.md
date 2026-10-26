---
id: "39353269463063"
titulo: "Configuração Automática do Código de Receita para EFD-REINF em Serviços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39353269463063-Configura%C3%A7%C3%A3o-Autom%C3%A1tica-do-C%C3%B3digo-de-Receita-para-EFD-REINF-em-Servi%C3%A7os"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-09-02T14:40:47Z"
rotulos: ["Configuração", "Parceiro", "Impostos", "Nota Fiscal", "TOP", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Configuração Automática do Código de Receita para EFD-REINF em Serviços

**SITUAÇÃO**

Ao realizar o lançamento de uma nota fiscal nas centrais, o campo referente ao Código de Natureza de Rendimentos ou ao Código de Receita não é populado automaticamente conforme esperado, exigindo preenchimento manual.

**CAUSA**

A ausência do preenchimento automático pode ocorrer devido a configurações incompletas nos cadastros.

**SOLUÇÃO**

### **(1)** Cadastrar o Código de Natureza de Rendimentos.

Primeiro, verifique se o código de natureza de rendimentos está cadastrado:

**Caminho:** Livros Fiscais » Arquivos » Códigos de Naturezas de Rendimentos.

1. Verifique se o código que você precisa já está cadastrado.
2. Se não estiver, clique em **"Inserir novo código"**

**Aba "Geral":**

- ✅ **"Gera sem tributação?"** (Marque se deseja enviar rendimentos sem retenção de impostos).

**Campo "Tipo de Dedução":**

- Informe o código se houver dedução
- Se houver mais de um, separe por ponto e vírgula (;)

**Campo "Tipo Rendimento Isento":**

- Informe o código se houver rendimento isento.
- Se houver mais de um, separe por ponto e vírgula (;)

**Campo "Tipo Tributo":**

- Informe os tipos de impostos referentes aos rendimentos isentos.
- Separe por ponto e vírgula (,).

**Importante:** A marcação **"Gera sem tributação?"** permite que sejam enviadas notas sem retenção de impostos (considerando apenas o valor bruto) ou financeiro (considerando apenas o valor do desdobramento do título).

### **(2)** Configurar o Código de Natureza de Rendimentos no Cadastro de Serviços.

Esta é a configuração principal para que o código seja aplicado automaticamente:

**Caminho:** Comercial » Arquivo » Cadastros » Serviços.

1. Localize o serviço que deve alimentar a REINF.
2. Acesse a **aba "Impostos**".
3. Localize a seção **"EFD FISCAL/Contribuições/REINF/Sintegra**".

**Campo "Código Natureza de Rendimentos":**

- Informe o código cadastrado.
- Este código será aplicado automaticamente quando o serviço for lançado em uma nota fiscal.

**Importante:** este campo é **obrigatório** para que os eventos do Grupo 4000 da EFD-REINF e seus detalhamentos sejam gerados.

### **(3)** Configurar o Código de Natureza de Rendimentos no Cadastro de Produtos (se aplicável à nota de produtos).

Se você também trabalha com produtos que devem alimentar a REINF:

**Caminho:** Comercial » Arquivo » Cadastros » Produtos.

1. Localize o produto
2. Acesse a **aba "Impostos**".
3. Localize a seção **"EFD FISCAL/Contribuições/REINF/Sintegra**".

**Campo "Código Natureza de Rendimentos":**

- Informe o código cadastrado.
- Este código será aplicado automaticamente quando o serviço for lançado em uma nota fiscal.

### **(4)** Configurar a TOP para gerar informações do REINF Grupo 4000.

A TOP precisa estar configurada para gerar eventos do Grupo 4000:

**Caminho:** Comercial » Arquivo » Cadastros » Tipos de Operação - TOP.

1. Localize a TOP utilizada para serviços/produtos REINF.
2. Acesse a **aba "Impostos**".

**Marcação "Gerar informações do EFD Reinf Grupo 4000?":**

- **Marque esta** opção.
- Esta marcação é **obrigatória** para que os movimentos sejam considerados na geração da EFD-REINF

### **(5)** Configurar o Código de Receita DARF na Tela de Impostos.

Para que o código de receita também seja aplicado automaticamente:

**Caminho:** Comercial » Arquivo » Cadastros » Impostos.

1. Localize o cadastro de impostos utilizado
2. Acesse a aba adequada (**Serviço**, **Produto**, **TOP**, **Parceiro** ou **Empresa**).

**Para cada tipo de imposto (IRRF, INSS, etc.):**

**Campo "Cód.** "Receita**" ou "Código Receita (DARF)":**

- **Informe o código de receita** DARF.
- Este código deve estar previamente cadastrado em: Configurações » Cadastros » Cadastro de Receita - DARF.

###

### **(6)**Configurar Código de Receita para Agregado/CSRF/PCC

Para que impostos agregados sejam enviados para a REINF:

**Caminho:** Comercial » Preferências » Empresa.

1. Selecione a empresa.
2. Acesse a **aba "EFD - Reinf**".

**Campo "Código de Receita para atribuir Agregado/CSRF/PCC":**

- Informe o código de receita DARF.
- Este código deve ser o **mesmo** informado na tela de Impostos.

**Importante:** para que os valores de imposto Agregado/CSRF/PCC sejam enviados, o código de receita DARF deve estar informado tanto na tela de Impostos quanto neste campo.

###
