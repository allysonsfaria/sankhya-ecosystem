---
id: "360042753354"
titulo: "Regras para Buscar a CST de IPI e o cálculo do imposto no Sistema SankhyaW"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753354-Regras-para-Buscar-a-CST-de-IPI-e-o-c%C3%A1lculo-do-imposto-no-Sistema-SankhyaW"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-21T16:08:33Z"
rotulos: ["#RevisadoGui", "Produtos", "Alíquotas", "Configuração", "IPI", "Impostos", "Regras para CST de IPI e Cálculo no Sistema SankhyaW", "SankhyaW"]
---

# Regras para Buscar a CST de IPI e o cálculo do imposto no Sistema SankhyaW

#### IPI - IMPOSTO SOBRE PRODUTOS INDUSTRIALIZADOS

O imposto sobre produtos industrializados (IPI) incide sobre produtos industrializados, nacionais e estrangeiros.

Suas disposições estão regulamentadas pelo **[Decreto 7.212/2010](http://www.normaslegais.com.br/legislacao/decreto7212_2010.htm)** (RIPI/2010).

O campo de incidência do imposto abrange todos os produtos com alíquota, ainda que zero, relacionados na Tabela de Incidência do IPI (TIPI), observadas as disposições contidas nas respectivas notas complementares, excluídos aqueles a que corresponde a notação "NT" (não-tributado).

#### Regras para Buscar a CST de IPI e o cálculo do imposto

(1)** Processo de Venda (Saída)**

![Imagem 1: TOP](https://ajuda.sankhya.com.br/hc/article_attachments/17801273201175) TOP

Tem IPI?

Não: pega a CST de Saída informada neste cadastro.

Sim: passa para o próximo cadastro.

![Imagem 2: Cadastro de Produto](https://ajuda.sankhya.com.br/hc/article_attachments/17801273204247) Cadastro de Produto

Tem IPI na venda?

Não: pega a CST de Saída informada neste cadastro.

Sim: passa para o próximo cadastro.

![Imagem 3: Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/17801273209111) Empresa

Tem IPI?

Não: pega a CST de Saída informada neste cadastro.

Sim: passa para o próximo cadastro.

![Imagem 4: PARCEIRO](https://ajuda.sankhya.com.br/hc/article_attachments/17801260732567) PARCEIRO

Tem IPI?

Não: pega a CST de Saída informada neste cadastro.

Sim: passa para o próximo cadastro.

![Imagem 5: Alíquota de IPI](https://ajuda.sankhya.com.br/hc/article_attachments/17801260734871) Alíquota de IPI

Faz o cálculo e pega a CST de saída informada neste cadastro

(1)** Processo de COMPRA (Entrada):**

![Imagem 6: TOP](https://ajuda.sankhya.com.br/hc/article_attachments/17801273201175) TOP

Tem IPI?

Não: pega a CST de ENTRADA informada neste cadastro.

Sim: passa para o próximo cadastro.

![Imagem 7: CADASTRO DO PRODUTO](https://ajuda.sankhya.com.br/hc/article_attachments/17801273204247) CADASTRO DO PRODUTO

Tem IPI na compra?

Não: pega a CST de ENTRADA informada neste cadastro.

Sim: passa para o próximo cadastro.

![Imagem 8: PARCEIRO](https://ajuda.sankhya.com.br/hc/article_attachments/17801273209111) PARCEIRO

TEM IPI?

Não: pega a CST de ENTRADA informada neste cadastro.

Sim: passa para o próximo cadastro.

![Imagem 9: ALIQUOTA DE IPI](https://ajuda.sankhya.com.br/hc/article_attachments/17801260732567) ALIQUOTA DE IPI

Faz o cálculo e pega a CST de ENTRADA informada neste cadastro.

**![Imagem 10: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17801273226519) IMPORTANTE:**

- Existe a exceção da hierarquia quando o Parceiro é Isento de ICMS (Cadastro do Parceiro » Aba Fiscal » Classificação de ICMS) neste caso a C.S.T. IPI utilizada é a do Cadastro do **"Parceiro"**.
- A opção tem ICMS do cadastro da **"Empresa"** (Comercial » Preferências » Empresa) tem que estar marcada para realizar o cálculo.
