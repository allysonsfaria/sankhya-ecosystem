---
id: "31606556500631"
titulo: "Como corrigir divergências nos valores da Base de ICMS do Frete e do ICMS sobre o Frete em vendas de KITs com IPI embutido e frete incluso?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31606556500631-Como-corrigir-diverg%C3%AAncias-nos-valores-da-Base-de-ICMS-do-Frete-e-do-ICMS-sobre-o-Frete-em-vendas-de-KITs-com-IPI-embutido-e-frete-incluso"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-20T13:40:06Z"
rotulos: ["Configuração", "NF-e", "IPI", "ICMS", "Impostos", "TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "operações de venda", "KITs com IPI embutido", "frete incluso", "divergência nos valores", "valor do ICMS sobre o frete", "base do ICMS do frete"]
---

# Como corrigir divergências nos valores da Base de ICMS do Frete e do ICMS sobre o Frete em vendas de KITs com IPI embutido e frete incluso?

**SITUAÇÃO:**

Em operações de venda envolvendo KITs com IPI embutido e frete incluso, pode ocorrer divergência nos valores de base do ICMS do frete e no valor do ICMS sobre o frete.

**SOLUÇÃO:**

Para corrigir o problema, realize as seguintes configurações:

**(1)** Acesse a tela  **"Preferências"** (Configurações » Avançado » Preferências) **e a**tive a preferência **"KITIPIESPECIFIC"**.

**(2)** Em seguida, vá até a tela **"Tipos de Operação"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) selecione a TOP correspondente. Nela, acesse a aba **"Impostos"** e no campo **"IPI incide na base de ICMS"** selecione a opção **"Incide".**

Essas alterações garantem que o sistema aplique corretamente a alíquota de ICMS definida para o item e que o frete seja considerado adequadamente na base de cálculo.

#### Exemplo de cálculo após correção:

- **Valor do frete:** R$ 1.000,00
- **Redução da base:** 42,8571% (R$ 428,571)
- **Base de cálculo do ICMS sobre o frete:** R$ 571,429
- **Alíquota de ICMS aplicada na Operação**: 7,00%
- **Cálculo do ICMS sobre o frete:** R$ 571,429 × 7,00% = **R$ 40,00**

**CAUSA:**

O problema ocorre quando a preferência de cálculo de IPI para KITs não está devidamente configurada e a opção de incidência do IPI sobre a base de ICMS na TOP (Tipo de Operação) está incorreta.

**Em cenários onde o frete é incluso na nota fiscal e o KIT possui IPI embutido**, a ausência de configurações específicas faz com que o sistema calcule de forma incorreta a base de ICMS do frete e o valor correspondente do imposto.
