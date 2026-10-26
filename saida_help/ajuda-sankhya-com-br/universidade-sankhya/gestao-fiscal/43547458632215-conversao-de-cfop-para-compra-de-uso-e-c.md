---
id: "43547458632215"
titulo: "Conversão de CFOP para compra de uso e consumo: melhores práticas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43547458632215-Convers%C3%A3o-de-CFOP-para-compra-de-uso-e-consumo-melhores-pr%C3%A1ticas"
trilha: "Universidade Sankhya > Gestão Fiscal"
atualizado_em: "2026-10-07T14:09:25Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Conversão de CFOP para compra de uso e consumo: melhores práticas

Saiba como configurar corretamente a conversão de CFOP para compras de uso e consumo no Sankhya.

A conversão de CFOP (Código Fiscal de Operações e Prestações) para compras de uso e consumo é fundamental para garantir a correta escrituração fiscal e o enquadramento tributário das operações no ERP Sankhya. O sistema realiza a conversão automática do CFOP de acordo com o tipo de uso do produto, a configuração do tipo de substituição tributária e a classificação do ICMS do parceiro. Seguir as melhores práticas evita erros fiscais e garante que as notas sejam lançadas corretamente nos livros fiscais.

Ao cadastrar uma nota de compra de material de uso e consumo, o sistema avalia as configurações do produto, da TOP (Tipo de Operação) e do parceiro para determinar o CFOP correto. É importante que o campo **"Uso do produto"** esteja definido como **"Consumo"** no cadastro do produto, e que a TOP utilizada esteja devidamente parametrizada com os CFOPs adequados para operações dentro e fora do estado.

### Configuração dos cadastros para conversão automática

Como parametrizar produto, TOP e parceiro para conversão correta do CFOP

Para garantir a conversão automática do CFOP em compras de uso e consumo, siga os passos abaixo:

**(1)** No cadastro de produtos (Configurações Cadastros Produtos Produtos), defina o campo **"Uso do produto"** como **"Consumo"**.

**(2)** No cadastro de tipos de operação - TOP (Configurações Cadastros Tipos de Operação - TOP), na aba **"Livro Fiscal"**, informe os CFOPs para **"Dentro do Estado"** e **"Fora do Estado"** conforme a operação de compra de consumo.

**(4)** No cadastro de parceiros (Configurações Cadastros Parceiros), na aba **"Fiscal"**, valide a **"Classificação ICMS"** para garantir que o sistema aplique o CFOP corretamente.

Com essas configurações, ao lançar uma nota de compra de uso e consumo, o sistema irá converter automaticamente o CFOP conforme as regras abaixo:

- Para operações **dentro do estado** (exemplo: CFOP 5202), se o produto for de consumo e o tipo de substituição for C, P ou A, o sistema converterá para **6413**. Se o tipo de substituição for "Não tem", converterá para **6556**.

- Para operações **fora do estado** (exemplo: CFOP 6202), as mesmas regras se aplicam: consumo com substituição tributária (C, P ou A) converte para **6413**; sem substituição, para **6556**.

### Cuidados na devolução de compras de uso e consumo

Como garantir a correta devolução fiscal de materiais de consumo

Ao realizar uma devolução de compra de material de uso e consumo, é essencial utilizar o CFOP correto para que a operação seja reconhecida fiscalmente. O sistema Sankhya possui CFOPs específicos para devolução de consumo:

- **6413**: Devolução de mercadoria destinada ao uso ou consumo, em operação com mercadoria sujeita ao regime de substituição tributária.

- **6556**: Devolução de compra de material de uso ou consumo (quando não há substituição tributária).

Certifique-se de que a TOP de devolução esteja configurada com o CFOP adequado para cada cenário. Caso a nota de origem possua CFOPs diferentes, ajuste manualmente o CFOP de cada item na devolução para garantir a conformidade fiscal.

### Parâmetros e observações importantes

Parâmetros do sistema e pontos de atenção para evitar erros fiscais

Alguns parâmetros do sistema influenciam diretamente na conversão de CFOP para compras de uso e consumo. Verifique se os seguintes parâmetros estão corretamente configurados:

- **"CFOP para FORA do Estado"** e **"CFOP para DENTRO do Estado"** na TOP.

- Parâmetros globais relacionados a serviços e substituição tributária, caso a operação envolva esses cenários.

Além disso, valide sempre se o CFOP utilizado está devidamente cadastrado na tela **"CFOP"** (Comercial Arquivo Cadastros CFOP) e se está classificado corretamente quanto ao tipo de operação. Isso evita rejeições fiscais e problemas na escrituração dos livros fiscais.

Seguindo essas melhores práticas, a conversão de CFOP para compras de uso e consumo será realizada de forma automática e segura, garantindo a conformidade fiscal e a integridade das informações no ERP Sankhya.
