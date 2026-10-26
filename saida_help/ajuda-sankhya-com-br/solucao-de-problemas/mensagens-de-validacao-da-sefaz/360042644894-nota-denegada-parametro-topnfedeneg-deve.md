---
id: "360042644894"
titulo: "Nota Denegada - parâmetro TOPNFEDENEG deve ter uma TOP informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042644894-Nota-Denegada-par%C3%A2metro-TOPNFEDENEG-deve-ter-uma-TOP-informada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:18Z"
rotulos: ["ERRONF", "#RevisadoGui", "CORE_E01230", "Configuração", "NF-e", "SEFAZ", "TOP", "Nota Denegada - Configuração de TOP Necessária", "Erro", "Documentos Eletrônicos"]
---

# Nota Denegada - parâmetro TOPNFEDENEG deve ter uma TOP informada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16334400033943) MENSAGEM:**

[CORE\_E01230] Nota Denegada. Parâmetro TOPNFEDENEG deve ter uma TOP informada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334400035607) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Vincule no cadastro da TOP utilizada na emissão da respectiva NF-e um Tipo de Operação NF-e DENEGADA, conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/16334400039319) Vincule no cadastro da TOP utilizada na emissão da respectiva NF-e um Tipo de Operação NF-e DENEGADA, conforme detalhado abaixo:

**(2)** Tela **"[Tipos de Operação -TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivo » Cadastros), aba **"[NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)"**:

(3)** Tipo Operação NF-e Denegada**: A TOP informada aqui irá sobrepor as TOPS informadas no parâmetro **"TOPNFEDENEG"**. Isto será necessário quando a operação da NF-e for diferente das operações das TOPS informadas neste parâmetro (normalmente TOPS de Venda, Compra, Devoluções etc.).

![Imagem 4: Após criação da TOP Denegada e inserção em seu devido campo, consulte a situação atual da nota no botão NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16334400040471) Após criação da TOP Denegada e inserção em seu devido campo, consulte a situação atual da nota no botão NF-e.

![Imagem 5: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16334400038679) **OBSERVAÇÕES:**

![Imagem 6: Usualmente, a configuração da TOP Denegada é uma 'duplicação' da TOP utilizada na operação, porém com ressalvas:](https://ajuda.sankhya.com.br/hc/article_attachments/16334400039319) Usualmente, a configuração da TOP Denegada é uma 'duplicação' da TOP utilizada na operação, porém com ressalvas:

**(2)** Financeiro: Não atualiza
**(2)** Estoque: Não atualiza
**(2)** Livro: Não atualiza

As atualizações são retiradas para que seja desfeito o processo realizado na TOP anterior, realizando a "anulação" desta nota.

![Imagem 7: Caso a nota de origem é advinda de pedidos, é necessário que o parâmetro "DENEGDEIXAPEND" esteja habilitado. Pois,…](https://ajuda.sankhya.com.br/hc/article_attachments/16334400040471) Caso a nota de origem é advinda de pedidos, é necessário que o parâmetro **"DENEGDEIXAPEND"** esteja habilitado. Pois, somente com tal parâmetro habilitado, é possível refaturar o pedido após os ajustes da IE, seja do emitente ou destinatário.

![Imagem 8: A TOP Denegada a ser vinculada no campo mencionado acima, deve ter o mesmo Tipo de Movimento da TOP utilizada no…](https://ajuda.sankhya.com.br/hc/article_attachments/16334385379607) A TOP Denegada a ser vinculada no campo mencionado acima, deve ter o mesmo **Tipo de Movimento** da TOP utilizada no lançamento. Exemplo: Se emitida uma NF-e de Devolução de Compra, e essa for denegada pela SEFAZ, será necessário cadastrar uma **Top Denegada** com o Tipo de movimento DEVOLUÇÃO DE COMPRA.

![Imagem 9: Caso não possua essa TOP configurada, valide se existe uma "padrão" com tipo de movimento 'Venda' devidamente…](https://ajuda.sankhya.com.br/hc/article_attachments/16334400041367) Caso não possua essa TOP configurada, valide se existe uma "padrão" com tipo de movimento 'Venda' devidamente cadastrada, duplicando a mesma e ajustando o tipo de movimento conforme desejado. Certifique que esse cadastro padrão foi realizado e validado junto a um consultor e encontra-se de acordo com o esperado. Caso contrário o direcionamento para criação dessa TOP será realizado para sua Filial.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16334400042647) CAUSA:**

Ocorre quando o parâmetro não esta configurado com o código da TOP de Denegada.
