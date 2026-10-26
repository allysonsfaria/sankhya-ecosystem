---
id: "43547851073815"
titulo: "Configuração do cálculo de ICMS/ST com crédito outorgado no MT (Caso de Uso de GO > MT)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43547851073815-Configura%C3%A7%C3%A3o-do-c%C3%A1lculo-de-ICMS-ST-com-cr%C3%A9dito-outorgado-no-MT-Caso-de-Uso-de-GO-MT"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-09-30T14:15:15Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Configuração do cálculo de ICMS/ST com crédito outorgado no MT (Caso de Uso de GO > MT)

**Situação:**

Adquirimos uma mercadoria de GO que possui ICMS/ST em MT. O recolhimento da guia já foi realizado, porém, ao lançar a nota no Sankhya, o valor calculado não está correspondendo ao valor recolhido.

Somos optantes pelo **crédito outorgado no MT**, sendo que o crédito de ICMS é limitado a **7%**, e o cálculo do ICMS/ST deve considerar o **MVA interno**. Na operação, o ICMS veio destacado a **12%**, porém o valor a ser considerado para o cálculo deve observar essa limitação.

Realizei a configuração em **Alíquotas de ICMS**, mas o cálculo do sistema não está chegando ao valor correto.

**Solução:**

**(1)**  Neste cenário em questão, como já existe uma regra de alíquota de ICMS que está sendo buscada no lançamento da nota, partiremos do ponto de que basta apenas ajustar tais configurações.

**(2)**  Após copiar o código da regra de alíquota de ICMS encontrada, abra a tela: (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS).

**(3)**  Ao abrir a regra, atende-se aos seguintes pontos:

- Verifique se o campo "Margem de Lucro (MVA)" deve estar preenchido;
- Verifique se o campo "Alíq**.** Subst. Tributação: " , deve estar preenchido; 12%
- Verifique se o campo "Alíq. Limite **de crédito**. ICMS p/ dedução no Valor ST: ", deve estar preenchido; 7%
- Verifique se o campo "Modalidade BC ICMS ST**"** deve estar preenchido com a opção = "Margem Valor Agregado (%)**".**
- Verifique se o campo "Tipo de Cálculo de ST Específico**"** deve estar preenchido com a opção = "11 - Calcular ST (Alíq. Limite **de crédito**. ICMS **para** dedução no Valor ST)"

Exemplo:

![Imagem 1: Após ajustar estas configurações, lance novamente o item na nota e valide que o valor calculado de substituição estará…](https://ajuda.sankhya.com.br/hc/article_attachments/43768385741847)

**(4)**  Após ajustar estas configurações, lance novamente o item na nota e valide que o valor calculado de substituição estará correto como esperado.

**Causa:**

Dúvida de configuração.
