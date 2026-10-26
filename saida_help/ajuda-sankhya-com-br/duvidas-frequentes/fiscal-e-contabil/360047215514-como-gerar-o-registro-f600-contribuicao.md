---
id: "360047215514"
titulo: "Como gerar o \"Registro F600: Contribuição Retida na Fonte\" no EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360047215514-Como-gerar-o-Registro-F600-Contribui%C3%A7%C3%A3o-Retida-na-Fonte-no-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:32:01Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "TOP", "Financeiro", "avulsa", "EFD Contribuições", "Gerar o \"Registro F600", "Configurar tipo de escrituração", "Contribuição Retida na Fonte"]
---

# Como gerar o "Registro F600: Contribuição Retida na Fonte" no EFD Contribuições

- O registro Registro F600: Contribuição Retida na Fonte, é um registro para que as pessoas jurídicas beneficiadas por retenções, informe as mesmas neste registro, e este servirá de redução dos cálculos do PIS, COFINS, e CSLL apurados.

Para mais detalhes veja o Guia Prático da EFD Contribuições Página 273 de 425: [Clique aqui](http://sped.rfb.gov.br/estatico/20/6E34811D4F98083196E2A09880F048189788FC/Guia_Pratico_EFD_Contribuicoes_Versao_1_31%20-%2029_04_2019.pdf)

#### Quais as configurações necessárias no sistema, para geração F600 ?

![Imagem 1: Acesse a tela Empresa (Comercial » Preferências » Empresa), Aba EFD- Escrituração Fiscal Digital:](https://ajuda.sankhya.com.br/hc/article_attachments/18667413935255) Acesse a tela **Empresa** (Comercial » Preferências » Empresa), Aba EFD- Escrituração Fiscal Digital:

Para o 'Tipo de Escrituração' = EFD Contribuições, o registro **F600** deve estar marcado para gerar:

![Imagem 2: Para o 'Tipo de Escrituração' = EFD Contribuições, o registro F600 deve estar marcado para gerar:](https://ajuda.sankhya.com.br/hc/article_attachments/18667403864599)

![Imagem 3: Verifique na tela Impostos (Configurações » Cadastros » Impostos) como está configurado o campo " Gerar reg.F600 P/EFD…](https://ajuda.sankhya.com.br/hc/article_attachments/18667403869719) Verifique na tela **Impostos** (Configurações » Cadastros » Impostos) como está configurado o campo "Gerar reg.F600 P/EFD Contribuições:"

![Imagem 4: Verifique na tela Impostos (Configurações » Cadastros » Impostos) como está configurado o campo " Gerar reg.F600 P/EFD…](https://ajuda.sankhya.com.br/hc/article_attachments/18667403874327)

- Se marcado para atualizar como 'Saída' irá gerar F600 desta nota/financeiro de saída.
- Se marcado para "Não gerar" , o registro não será gerado.

Se estiver marcado **"Usar da TOP"**, serão verificadas as marcações de "**Atualização de Livro ICMS**" e "**Atualização Livro de ISS**"  presentes na aba 'Livro Fiscal' da tela 'Tipos de Operação-TOP', considerando as seguintes regras:

- Se marcado para atualizar como 'Saída' irá gerar F600 desta nota/financeiro de saída.
- Se marcado para atualizar como 'Entrada' irá gerar  F600 desta nota/financeiro de entrada
- Se marcado para "Não atualizar" , o registro não será gerado.

Para gerar exclusivamente os registros F600 no SPED Contribuições com base nos financeiros que foram baixados no período, basta habilitar o parâmetro '**F600RETDHBAIXA'**.

O campo 'Gerar reg. F600 p/EFD Contribuições' se selecionado a opção 'Usar da TOP', condiciona a geração do F600 com o valor do imposto referente a receita ou a despesa de acordo com a atualização dos livros fiscais (Livro de ICMS /IPI e ou Livro de ISS).

**Importante:**

- Dúvidas sobre geração do Campo 02 do Registro F600, acesse: [Campo de preenchimento obrigatório - Campo 2 - IND\_NAT\_RET[Registro F600]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047855033)
- Dúvidas sobre a geração do Campo 03 do Registro F600, acesse: [Como é gerado o Campo 3 - DT\_RET do Registro F600 - EFD Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047219634)
