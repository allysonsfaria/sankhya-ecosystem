---
id: "360044295353"
titulo: "Cálculos de ICMS: Usando Grupo de exceção por \"Produto\" ou \"Grupo de produtos\" ou \"Grupo de ICMS do Produto\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044295353-C%C3%A1lculos-de-ICMS-Usando-Grupo-de-exce%C3%A7%C3%A3o-por-Produto-ou-Grupo-de-produtos-ou-Grupo-de-ICMS-do-Produto"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-08-21T18:27:43Z"
rotulos: ["Produtos", "Alíquotas", "Configuração", "Fiscal", "ICMS", "Impostos", "Utilizando Grupo de Exceção para o ICMS"]
---

# Cálculos de ICMS: Usando Grupo de exceção por "Produto" ou "Grupo de produtos" ou "Grupo de ICMS do Produto"

(1)** ICMS** - **Imposto sobre Operações relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual** **e Intermunicipal e de Comunicação:** imposto não cumulativo que incide sobre as operações relativas à circulação de mercadorias e prestações de serviços de transporte interestadual e intermunicipal e de comunicação. De competência dos Estados e do Distrito Federal, conforme previsto no art. 155, II, da Constituição de 1988, apresenta-se como uma das principais fontes de recursos financeiros para a consecução das ações governamentais.

![Imagem 1: Usando Grupo de exceção por "Produto" ou "Grupo de produtos" ou "Grupo de ICMS do Produto":](https://ajuda.sankhya.com.br/hc/article_attachments/17322428203415) Usando Grupo de exceção por "Produto" ou "Grupo de produtos" ou "Grupo de ICMS do Produto":

Configurações básicas disponível no post**: "**[Configurações necessárias para o calculo básico de ICMS, sem exceções."](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044295053)

**(1)** **1º Cadastro de Alíquotas de ICMS:**

- Considerando que seja uma venda, Origem (Empresa) MG e Destino (SP);
- Na árvore hierárquica do lado esquerdo da tela, selecione MG-Minas Gerais e depois o filho SP-São Paulo. Verifique se existe alguma regra por "Produto" ou "Por Grupo de Produto" ou "Grupo de ICMS do Produto"; 
  Se existir, terá alguma regra com as descrições "Por produto" ou "Por Grupo de Produtos" ou  "Por grupo de ICMS do produto".
- Caso não tenha, pode incluir pelo botão **"+"** Incluir;
- Em UF de origem busque o estado de Minas gerais e no campo UF de destino, busque o estado de São Paulo.

**(1)** **Em Exceções:**

- Em TIPO 1 (\*), pode selecionar uma das três opções passadas:
  - Por Produto: abrirá uma opção para informar o **código** do produto;
  - Por Grupo de Produtos: abrirá uma opção para informar o **Grupo de produtos;**
  - Por Grupo de ICMS do Produto: abrirá uma opção para informar o grupo de ICMS do   produto.
- Diferente das outras opções, para usar esta opção informe o grupo de ICMS no cadastro de produtos > ABA Imposto campo "Grupo de ICMS".

![Imagem 2: Diferente das outras opções, para usar esta opção informe o grupo de ICMS no cadastro de produtos > ABA Imposto campo…](https://ajuda.sankhya.com.br/hc/article_attachments/13135783928599)

![Imagem 3: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17322428224023) **OBSERVAÇÃO:**

Sempre é bom verificar/configurar as prioridades desta tela, em **"outras opções"** da tela. Caso o sistema não calcule os Impostos(ICMS/ST/IPI) para alguns produtos e, ao verificar toda a configuração de Cálculo dos imposto, constatar que tudo está certo, pode verificar se os produtos são "Matérias Primas/Uso Consumo", configuração do Cadastro de produto "Usado como:".
Para cálculo de impostos destes produtos observe o **"CALCIMPMP"** (Configurações >> Avançando >> Preferencias), este parâmetro deve ser ligado.
