---
id: "4420403259671"
titulo: "Para TOP Configurada com Modelo de Documento 55 - Nota Fiscal Eletrônica e o campo NF-e diferente de ‘Convencional (Não Usa NF-e)', ‘Import. Doc.(Emissão Própria)' e 'Terceiros’ a numeração da Nota deve ser automática"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4420403259671-Para-TOP-Configurada-com-Modelo-de-Documento-55-Nota-Fiscal-Eletr%C3%B4nica-e-o-campo-NF-e-diferente-de-Convencional-N%C3%A3o-Usa-NF-e-Import-Doc-Emiss%C3%A3o-Pr%C3%B3pria-e-Terceiros-a-numera%C3%A7%C3%A3o-da-Nota-deve-ser-autom%C3%A1tica"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:19:36Z"
rotulos: ["Configuração", "NF-e", "TOP", "Vendas", "#ValidadoFer", "#causaraiz", "Numeração Automática para Notas Fiscais Eletrônicas (NF-e)"]
---

# Para TOP Configurada com Modelo de Documento 55 - Nota Fiscal Eletrônica e o campo NF-e diferente de ‘Convencional (Não Usa NF-e)', ‘Import. Doc.(Emissão Própria)' e 'Terceiros’ a numeração da Nota deve ser automática

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16283184404631) MENSAGEM:**

Para TOP Configurada com Modelo de Documento 55 - Nota Fiscal Eletrônica e o campo NF-e diferente de ‘Convencional (Não Usa NF-e)', ‘Import. Doc.(Emissão Própria)' e 'Terceiros’ a numeração da Nota deve ser automática. Marque a opção 'Numeração somente automática' e use a base de numeração 'Venda’ ou 'Devolução de venda’.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16283212160151) SOLUÇÃO:**

Na tela **"Tipos de Operação - TOP",** aba 'Impressão, selecione a marcação **"Numeração somente automática"**, conforme print abaixo:

![Imagem 3: Na tela "Tipos de Operação - TOP", aba 'Impressão, selecione a marcação "Numeração somente automática" , conforme print…](https://ajuda.sankhya.com.br/hc/article_attachments/16283196593047)

**![Imagem 4: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16283212164631) OBSERVAÇÕES:**

![Imagem 5: Essa validação ocorre quando o parâmetro "Valida config. de Nr automática na TOP-VALNRAUTTOP" encontra-se ligado ;](https://ajuda.sankhya.com.br/hc/article_attachments/16283196600599) Essa validação ocorre quando o parâmetro **"Valida config. de Nr automática na TOP-VALNRAUTTOP"** encontra-se **ligado**;

![Imagem 6: Essa validação ocorre considerando:](https://ajuda.sankhya.com.br/hc/article_attachments/16283212170263) Essa validação ocorre considerando:

- TOP de Venda ou Compra, com o campo **"NF-e",** da aba "**[NF-e/NFC-e",](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce)** diferente de **"Convencional (Não Usa Nf-e)", "Import. Doc.(Emissão Própria)"**e **"Terceiros"**

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16283212176535) CAUSA:**

Se o parâmetro **"Valida config. de Nr automática na TOP-VALNRAUTTOP"** estiver ligado, ao criar ou alterar uma TOP de Venda ou Compra, com o campo **"NF-e",** da aba [NF-e/NFC-e,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce) diferente de **"Convencional (Não Usa Nf-e)", "Import. Doc.(Emissão Própria)"**e **"Terceiros"**, a marcação Numeração somente automática deverá estar selecionada e o campo Base de Numeração deverá indicar a opção **"Venda"** ou **"Devolução de venda"**. Caso não esteja marcada, ao tentar salvar a configuração o sistema apresentará a mensagem;
