---
id: "39352719540247"
titulo: "Erro na Base de Cálculo de IBS/CBS em Devolução de Compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39352719540247-Erro-na-Base-de-C%C3%A1lculo-de-IBS-CBS-em-Devolu%C3%A7%C3%A3o-de-Compra"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Dúvidas Frequentes"
atualizado_em: "2026-09-15T17:09:21Z"
rotulos: ["Configuração", "Devolução de Compra", "Impostos", "TOP", "IBS", "CBS", "Reforma Tributária", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Erro na Base de Cálculo de IBS/CBS em Devolução de Compra

**Mensagem**

Divergência nos valores de **"IBS"** (Imposto sobre Bens e Serviços) e **"CBS"** (Contribuição sobre Bens e Serviços) na devolução de compra, com base de cálculo não correspondente aos valores da nota fiscal de origem.

**Situação**

Ao processar uma **"Devolução de Compra"** no sistema, os valores dos tributos da reforma tributária (**"IBS"** e **"CBS"**) não estão sendo calculados ou copiados corretamente da nota fiscal de origem. A **"Base de Cálculo"** apresenta divergências, especialmente quando a configuração do campo **"Cálculo de ICMS, IPI, ISS, IBS, CBS e IS"** não está adequada para contemplar os novos impostos. Além disso, em devoluções realizadas em 2026 referentes a vendas de 2025, o sistema pode calcular indevidamente **"IBS"** e **"CBS"**, mesmo quando a nota de origem não possuía esses tributos.

**Solução**

**(1)**  Acesse a tela **"Tipo de Operação"** (Configurações Impostos Tipo de Operação) e localize o tipo de operação utilizado na devolução de compra.

**(2)**  Verifique a configuração do campo **"Cálculo de ICMS, IPI, ISS, IBS, CBS e IS"** e ajuste conforme a necessidade da operação:

    • **Calcula e digita**  ou **Calcula e não digita** – Calcula na inclusão: os tributos **"IBS"**, **"CBS"** e **"IS"** serão calculados automaticamente no momento da inclusão da nota de devolução, com base nas configurações tributárias vigentes.

    • **Não Calcula e digita** ou **Não Calcula e não digita** – Copia da nota de origem: os valores de **"IBS"**, **"CBS"**, **"ICMS"**, **"ST"**, **"PIS"** e **"Cofins"** serão copiados proporcionalmente da nota fiscal de origem, respeitando a quantidade devolvida.

**(3)**  Ao incluir a nota de devolução de compra, acesse a tela **"Central de Compras"** (Portal de Compras) e valide os valores no **"Resumo de Impostos"** ou no **"Consultar/Alterar Dados do Imposto do Item...**".

**(4)**  Verifique se a base de cálculo (**"vBC"**) e os valores de **"IBS"** e **"CBS"** estão corretos e proporcionais à nota de origem.

**(5)**  Caso a devolução seja referente a uma venda realizada em 2025 (antes da vigência da reforma tributária), certifique-se de que o sistema não calcule **"IBS"** e **"CBS"**, mesmo que a devolução ocorra em 2026. Para isso, utilize filtros pela data de emissão da nota de origem nas telas de identificação de **"IBS"** e **"CBS"**.

**(6)**  Confirme a nota de devolução e valide os lançamentos financeiros, garantindo que o valor total da nota esteja correto e sem divergências.
