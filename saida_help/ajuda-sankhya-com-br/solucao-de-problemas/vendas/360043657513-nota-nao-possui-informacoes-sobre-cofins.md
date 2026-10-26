---
id: "360043657513"
titulo: "Nota não possui informações sobre COFINS e esta informação é obrigatória para NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043657513-Nota-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-COFINS-e-esta-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-NF-e"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:28Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "COFINS obrigatório na NF-e", "Falta configuração em operação empresa e produto", "Necessário cadastrar alíquota de COFINS"]
---

# Nota não possui informações sobre COFINS e esta informação é obrigatória para NF-e

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16136521773975) MENSAGEM:**

Nota não possui informações sobre COFINS e esta informação é obrigatória para NF-e.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16136502073239) SITUAÇÃO:**

Ao tentar confirmar/aprovar uma NF-e de Venda, Devolução de Compra (Emissão Própria), ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16136521781015) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Tela " Tipos de Operação " (Comercial » Arquivos » Cadastros)](https://ajuda.sankhya.com.br/hc/article_attachments/16136535941655) Tela **"[Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Comercial » Arquivos » Cadastros)

**(2)** Aba **"Impostos",** Campo **"Tem COFINS":**marcado

**(2)** Aba **"Livro Fiscal"**, Campo **"Atualização de Livro de ICMS":** diferente de Não Atualiza

![Imagem 5: Tela " Empresa " (Comercial » Preferências)](https://ajuda.sankhya.com.br/hc/article_attachments/16136502076823) Tela **"[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)"** (Comercial » Preferências)

**(2)** Aba **"Propriedades"**,  Campo **"Calcula COFINS":**marcado

![Imagem 6: Tela " Produtos " (Configurações » Cadastros)](https://ajuda.sankhya.com.br/hc/article_attachments/16136521785495) Tela **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** (Configurações » Cadastros)

**(2)** Aba **"Impostos"**, Campo **"Grupo COFINS":**informe o grupo

![Imagem 7: Tela " Alíquotas de COFINS " (Caminho para acesso: Comercial » Arquivo » Cadastros » Alíquotas)](https://ajuda.sankhya.com.br/hc/article_attachments/16136521788567) Tela **"[Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS)"** (Caminho para acesso: Comercial » Arquivo » Cadastros » Alíquotas)

**(2)** Crie uma Alíquota de COFINS, considerando o tipo de Movimento e os campos (\*) marcados como obrigatórios.

**(2)** Considere selecionar o **Tipo** adequadamente e o **Cód. sit. tributária** (seguindo orientações do contador).

**(2)** Feito o cadastro, insira o **Grupo** criado no cadastro do Produto, conforme dito no item 3.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16136521791127) CAUSA:**

Por se tratar de uma Nota Fiscal Eletrônica, é imprescindível que se tenha o cálculo de COFINS. Mesmo que a incidência da Alíquota seja 0(zero), é preciso criar uma Alíquota com incidência zero, para que no ato da confirmação/aprovação da NF-e seja gerado os dados de COFINS no XML da NF-e.
