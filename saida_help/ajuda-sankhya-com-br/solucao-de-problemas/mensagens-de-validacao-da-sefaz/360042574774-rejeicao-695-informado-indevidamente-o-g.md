---
id: "360042574774"
titulo: "Rejeição 695: Informado indevidamente o grupo de ICMS para a UF de destino(NT2015/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042574774-Rejei%C3%A7%C3%A3o-695-Informado-indevidamente-o-grupo-de-ICMS-para-a-UF-de-destino-NT2015-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-01T15:26:40Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "DIFAL", "SEFAZ", "Impostos", "695", "Ajuste campos para cálculo DIFAL", "ICMSUFDest incorreto em operações especificadas", "Rejeição [695] - Grupo ICMS incorreto para UF", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Rejeição 695: Informado indevidamente o grupo de ICMS para a UF de destino(NT2015/003)

**SITUAÇÃO:**

Esta rejeição ocorre ao tentar transmitir uma nota fiscal eletrônica (NF-e) para a Secretaria da Fazenda (SEFAZ). O sistema identifica que o grupo de ICMS foi informado incorretamente para operações destinadas a uma determinada Unidade Federativa (UF), considerando a classificação fiscal do destinatário.

**SOLUÇÃO:**

Siga os passos abaixo para que todas as tags e informações do DIFAL sejam geradas corretamente, solucionando essa questão.

Acesse a tela **"Parceiros"** (**Configurações > Cadastros > Parceiros**) e, na aba **"Fiscal"**, verifique o campo **"Classificação ICMS"**.

Para operações em que há cálculo do **DIFAL**, a classificação do parceiro deve estar configurada como **"Consumidor Final Não Contribuinte"**, quando esse for o enquadramento correto.

Caso seja necessário realizar a alteração, salve o cadastro, redigite o parceiro na nota fiscal para que as informações sejam atualizadas e, em seguida, tente transmitir a nota novamente.

Caso o parceiro deva ser cadastrado com a **Classificação ICMS = "Consumidor Final Não Contribuinte"**, acesse a tela **"Tipos de Operação - TOP"** (**Comercial > Arquivo > Cadastros > Tipos de Operação - TOP**).

Nessa tela, na aba **"Impostos"**, desmarque a opção **"Calcular DIFAL Partilhado"**. Essa configuração fará com que, para a TOP em questão, o cálculo do diferencial de alíquota partilhado (DIFAL) não seja realizado.

Outra alternativa é realizar a configuração no cadastro do produto. Para isso, acesse a tela **"Produtos"** (**Configurações > Cadastros > Produtos**) e, na aba **"Impostos"**, desmarque a opção **"Calcular DIFAL?"**.

Após efetuar essa alteração, redigite o produto na nota fiscal para que os impostos sejam recalculados e, em seguida, gere novamente o lote da nota.

**CAUSA:**

A rejeição **695** ocorre quando o grupo de ICMS destinado ao **DIFAL (ICMSUFDest)** é informado em operações nas quais a legislação não permite o seu envio. Esse cenário pode estar relacionado a uma configuração incorreta do cadastro do parceiro destinatário (como a classificação de ICMS) ou a operações em que o cálculo do DIFAL não deve ser realizado.

Assim, **a rejeição será apresentada sempre que o grupo ICMSUFDest for gerado no XML e a operação se enquadrar em uma das situações abaixo:**

- Operação Estadual (idDest = 1) ou com Exterior (idDest = 3);
- Operação com Consumidor Normal (indFinal = 0);
- Operação com Contribuinte (indIEDest = 1) ou com Contribuinte Isento (indIEDest = 2);
- Operação de prestação de serviços (ISSQN);
- Operação com combustível (comb) derivado de petróleo. Código ANP diferente de: 820101001, 820101010, 810102001, 810102004, 810102002, 810102003, 810101002, 810101001, 810101003, 220101003, 220101004, 220101002, 220101001, 220101005, 220101006, 560101001;
- Data de Emissão anterior a 01/01/2016, em Produção.

**EXCEÇÕES:**

1. A critério da UF a regra de validação 695 não se aplica na devolução (finNFe = 4) por NFe Avulsa com IE do Emitente = ISENTO;
2. A regra de validação 695 não se aplica se informada UF do local de entrega diferente da UF do emitente;
3. A regra de validação 695 não se aplica, em produção, para NFe com data de emissão anterior a 01/07/2016.

**OBSERVAÇÃO:**

([NT2015/003](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=)) Nota Técnica.

**Parâmetros:**

No parâmetro **"UFs destino NF-e com benefício fiscal para DIFAL - UFDESTNFEBENFIS"**, que por padrão é vazio, informa-se a sigla de cada UF da SEFAZ de destino (separada por vírgula); caso a SEFAZ de origem/destino estejam amparadas por benefícios fiscais, ou seja, a alíquota interestadual é igual a zero. Em alguns casos, pode ser necessário atualizar a versão do sistema se o erro persistir.
