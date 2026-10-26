---
id: "360044615413"
titulo: "O parceiro 'X' não está habilitado na SEFAZ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615413-O-parceiro-X-n%C3%A3o-est%C3%A1-habilitado-na-SEFAZ"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-31T02:48:43Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "SEFAZ", "TOP", "CORE_E04217", "CORE_E04216", "Configurar validação cadastro SEFAZ", "Parceiro não habilitado SEFAZ/Receita", "TOP configurado para validar SEFAZ", "Erro", "Artigo atualizado KCS", "CVE - KCS"]
---

# O parceiro 'X' não está habilitado na SEFAZ

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16609557072279) MENSAGEM:**

[CORE\_E04217]:  O parceiro 'X' não está habilitado na SEFAZ.

[CORE\_E04216] O parceiro 'X' não está habilitado na Receita Federal.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16609603797015)SOLUÇÃO:**

Para correção seguir os passos abaixo:

![Imagem 3: Para correção seguir os passos abaixo: Verifique a configuração da TOP Acesse Comercial » Arquivo » Cadastros » Tipos…](https://ajuda.sankhya.com.br/hc/article_attachments/16609603799319) **Verifique a configuração da TOP** Acesse **Comercial » Arquivo » Cadastros » Tipos de Operação – TOP**, aba **Geral**, opção **"Valida situação cadastro na SEFAZ"**.

Quando marcada, o sistema valida a situação cadastral na confirmação de **Pedidos/Notas**, **Formação de Carga** e **Faturamento**.

> A consulta é feita por um WebService da própria SEFAZ. Como essa informação é de responsabilidade do órgão, pode haver casos em que o retorno esteja desatualizado.

A validação de SEFAZ vale para qualquer tipo de parceiro (física ou jurídica). Já a validação de **Receita Federal** (CORE\_E04216) só se aplica a parceiros **pessoa jurídica**

![Imagem 4: Verifique a situação cadastral do parceiro Acesse Configurações » Cadastros » Parceiros , aba Fiscal , campo "Situação…](https://ajuda.sankhya.com.br/hc/article_attachments/16609603800855) **Verifique a situação cadastral do parceiro** Acesse **Configurações » Cadastros » Parceiros**, aba **Fiscal**, campo **"Situação Cadastral SEFAZ"**. Se estiver **"Não Habilitado"**, o sistema bloqueia a confirmação mesmo para não contribuintes.

**Observação:** caso o parceiro esteja como **"Não Habilitado",** **a validação será efetuada mesmo sendo um parceiro não contribuinte.**

(3)**  Se a restrição não se aplicar, use "Suspender validação SEFAZ"** A SEFAZ pode retornar "Não Habilitado" sem que isso impeça de fato o parceiro de comprar ou realizar operações com ICMS. Nesse caso, no cadastro do Parceiro, aba Fiscal → **Outras Opções » Suspender validação SEFAZ**, informe no pop-up **"Data para nova Consulta"** a partir de quando o retorno da SEFAZ deve voltar a ser considerado. O sistema libera a confirmação imediatamente e só consulta a SEFAZ novamente na data informada.

**(4)** No parâmetro **"QTDDIACONSSEFAZ - Qtde de dias para realizar nova consulta na SEFAZ"**, deverá ser informado a quantidade de dias em que será realizado nova consulta, para verificar a situação do Parceiro junto a SEFAZ:

- Se o número de dias desde a última consulta for menor que o valor definido no parâmetro, a validação será feita pelo campo 'Situação Cadastral SEFAZ' do Cadastro do Parceiro, sem nova consulta à SEFAZ.
- Se ao tenta confirmar o Pedido/Nota o campo "Sit. Cad. SEFAZ", retornar zero, o sistema não confirmará o Pedido.

![Imagem 5: Se ao tenta confirmar o Pedido/Nota o campo "Sit. Cad. SEFAZ", retornar zero, o sistema não confirmará o Pedido.](https://ajuda.sankhya.com.br/hc/article_attachments/15021605550999)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16609603802647)CAUSA:**

A TOP usada no pedido/nota está configurada para validar a situação cadastral do parceiro. Ao confirmar o documento, o sistema consulta a SEFAZ (e, se aplicável, a Receita Federal) e identifica alguma restrição/suspensão/irregularidade que impede a emissão do documento eletrônico para esse parceiro.
