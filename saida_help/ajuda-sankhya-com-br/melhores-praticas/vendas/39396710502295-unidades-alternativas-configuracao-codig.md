---
id: "39396710502295"
titulo: "Unidades Alternativas: configuração, código de barras e boas práticas de uso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39396710502295-Unidades-Alternativas-configura%C3%A7%C3%A3o-c%C3%B3digo-de-barras-e-boas-pr%C3%A1ticas-de-uso"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-09-18T14:29:22Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Código de Barras", "Preferências", "Unidades Alternativas", "Artigo criado KCS", "CVE - KCS"]
---

# Unidades Alternativas: configuração, código de barras e boas práticas de uso

No Sankhya, um produto pode ser vendido em mais de uma unidade de medida (ex: caixa, fardo, pacote), além da unidade padrão do estoque. Cada uma dessas "Unidades Alternativas" pode ter seu próprio código de barras (EAN), usado nas consultas e no lançamento de itens em pedidos e notas fiscais.

### Cadastro de unidades alternativas

1. Acesse **Cadastros > Produtos**.
2. Localize o produto e abra a aba **Unidades Alternativas**.
3. Preencha:
   - **Unidade de medida** alternativa (ex: CX, FD, PCT).
   - **Fator de conversão** entre a unidade padrão e a alternativa.
   - **Código de barras (EAN)**, se essa unidade tiver um código próprio.
   - Marque **Ativo** para liberar o uso da unidade.

### Onde o sistema guarda cada código de barras

O Sankhya reconhece código de barras em três lugares, e todos são considerados nas buscas por EAN (consulta de produto, Ctrl+B no lançamento de itens, etc.):

| Onde | Tabela | Uso |
| --- | --- | --- |
| Campo Código/Referência do produto | TGFPRO | código principal do produto |
| Aba Código de Barras | TGFBAR | códigos de barras adicionais do produto |
| Aba Unidades Alternativas | TGFVOA | código de barras específico de cada unidade alternativa |

Se um código cadastrado em Unidades Alternativas não for reconhecido, o problema normalmente é de cadastro, não de limitação do sistema. Confira:

- O campo **EAN** foi preenchido e não está duplicado em outro produto/unidade.
- O **tipo de código de barras** (EAN-13, EAN-14, etc.) corresponde ao padrão do código digitado/lido.
- A unidade está marcada como **Ativo.**

### Impedir o uso de unidades alternativas inativas

Por padrão, o sistema pode permitir a seleção de uma unidade alternativa mesmo estando **Inativa**. Para bloquear isso:

1. Acesse **Configurações > Avançado > Preferências**.
2. Localize o parâmetro **VALCODVOLATIVO** (Validar código/volume ativo).
3. Selecione a opção de validação desejada.

Com a validação habilitada, o sistema passa a bloquear o uso de unidades alternativas inativas nos lançamentos. 

### Usando a unidade alternativa em vendas

1. No lançamento do item, selecione a unidade alternativa no campo de unidade, ou use **Ctrl+B** para buscar o produto diretamente pelo código de barras cadastrado (padrão, TGFBAR ou da unidade alternativa).
2. O sistema converte a quantidade automaticamente pelo fator de conversão cadastrado.
3. Se a unidade alternativa exigir quantidade fracionada, confirme que o campo **Decimais p/ quantidade** está configurado na aba **Medidas e Estoque** do produto.

### Corrigindo uma unidade alternativa cadastrada errada

1. Verifique se já existe estoque lançado com a unidade incorreta.
2. Se não houver estoque, inative a unidade errada.
3. Cadastre a unidade correta.
4. Refaça os lançamentos de estoque usando a unidade correta.

> **Importante:** teste o cadastro e o ajuste de unidades alternativas em ambiente de teste antes de replicar em produção.
