---
id: "37880676091287"
titulo: "Validação do cadastro de Cidades"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880676091287-Valida%C3%A7%C3%A3o-do-cadastro-de-Cidades"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:27Z"
rotulos: ["Configuração", "Fiscal", "Cidades", "Impostos", "Prefeituras", "NFS-e"]
---

# Validação do cadastro de Cidades

## Cidades

O cadastro de cidades é essencial para a emissão correta da NFS-e, pois define as regras fiscais de cada município. Nele são configuradas alíquotas de ISS, retenções, deduções, formatos de envio e limites de notas por lote, além de prazos e regras para substituição ou cancelamento. Sem esse cadastro padronizado, o sistema pode gerar rejeições na transmissão. Em resumo, é ele que garante que a NFS-e siga as exigências de cada prefeitura e seja emitida de forma segura e válida.

#### Siga as orientações para realizar a configuração no ERP Sankhya

**Importante:** para este treinamento utilizaremos a cidade de Uberlândia/MG como referência.

1. **Acesse a tela Cidades**

**Menu:**Configurações » Cadastros » Endereços » Cidades

- Nome - Uberlândia
- Cód. UF - MG
- Nome + UF - Uberlândia - MG

**Aba Geral**

- Mun. domicílio fiscal - (Para este treinamento utilize 3170206)
  Código de referência municipal IBGE utilizado para documentos fiscais
- Cód. município SIAFI - (Para este treinamento utilize 5403)
  Código de referência federal - SISTEMA INTEGRADO DE ADMINISTRAÇÃO FINANCEIRA - utilizado para integração com o governo

**Aba NFS-e**

- Nos campos abaixo, informe as quantidades correspondentes:

  - Qtd. máxima de notas em um lote NFS-e - 50
  - Prazo para substituição de NFS-e - 1
  - Quantidade de substituições permitidas - 1
  - Valor limite para cancelamento NFS-e - 500
- Nos campos abaixo, selecione as opções correspondentes:

  - Tipo de cancelamento para NFS-e - "Via web service com valor limite de cancelamento"
  - Tipo de envio do CNAE - “Normal”
- Marque os campos abaixo:

  - Permite cancelamento de NFS-e substituta? - marcado
  - Tem substituição NFS-e - marcado
- Verificar a tabela de cancelamento
  **Máscara LC116**
- Ao preencher o campo "Máscara LC116", será considerada apenas a sua configuração.

A máscara deve ser informada da seguinte forma:

Cada dígito é representado pelo caractere #.

**Exemplo para o código item lista 107:**

Se o valor repassado ao município for **01.07**, a máscara deve ser **##.##**.

Se o valor repassado ao município for **0107**, a máscara deve ser **####**.

Se o valor repassado ao município for **1.07**, a máscara deve ser **#.##**.

Se o valor repassado ao município for **107**, a máscara deve ser **###**.
