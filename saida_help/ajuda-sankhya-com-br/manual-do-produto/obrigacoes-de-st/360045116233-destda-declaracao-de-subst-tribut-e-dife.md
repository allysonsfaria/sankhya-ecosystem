---
id: "360045116233"
titulo: "DeSTDA - Declaração de Subst. Tribut. e Difer. Alíquota - S.N."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116233-DeSTDA-Declara%C3%A7%C3%A3o-de-Subst-Tribut-e-Difer-Al%C3%ADquota-S-N"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Obrigações de ST"
atualizado_em: "2026-09-15T17:20:12Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Simples Nacional", "Alíquota", "SEFAZ", "ICMS", "Declaração", "DeSTDA", "Difer.", "Nacional", "SEDIF", "Simples", "Subst.", "Tribut.", "br.com.sankhya.mgeliv.rel.destdasimplesnacional", "DeSTDA - Declaração de Subst. Tribut. e Difer. Alíquota - S.N. manual", "Relatório DeSTDA: Geração obrigatória", "Campos Obrigatórios: Empresa Data", "Apuração Simples Nacional: Detalhes necessários"]
---

# DeSTDA - Declaração de Subst. Tribut. e Difer. Alíquota - S.N.

| ``` ![Imagem 1: Módulo: Livros Fiscais > Relatórios](https://ajuda.sankhya.com.br/hc/article_attachments/42313067170967) Módulo: Livros Fiscais > Relatórios ``` |
| --- |

---

Por meio desta tela, realiza-se a geração dos valores que serão lançados no aplicativo SEDIF, onde serão realizadas as apurações da nova declaração acessória imposta aos contribuintes optantes pelo Simples Nacional.

![Imagem 2: Por meio desta tela, realiza-se a geração dos valores que serão lançados no aplicativo SEDIF, onde serão realizadas as…](https://ajuda.sankhya.com.br/hc/article_attachments/360096510994)

Para geração do relatório, efetue obrigatoriamente o preenchimentos dos campos **"Empresa"**, **"Data Inicial"** e **"Data Final"**.

A marcação **"Apurar compras para industrialização e comercialização (CFOP 2101, 2102)"** deverá ser selecionada para as empresas optantes pelo Simples Nacional que estão sujeitas ao recolhimento do diferencial de alíquotas em relação às operações de entrada de mercadorias destinadas para uso e consumo, ativo permanente e industrialização ou comercialização. Desta forma, serão apuradas neste relatório as compras com CFOP 2101 e 2102.

**Observação:** a regra da marcação acima será aplicada apenas para empresas estabelecidas em São Paulo.

![Imagem 3: Para obter valores neste relatório, deve-se gerar anteriormente a Apuração do ICMS e do ST, onde ambos devem estar com…](https://ajuda.sankhya.com.br/hc/article_attachments/16287115697303) Para obter valores neste relatório, deve-se gerar anteriormente a Apuração do ICMS e do ST, onde ambos devem estar com seus respectivos dados.

É importante salientar que para o campo **"Empresa"** serão apresentadas para escolha, apenas as empresas optantes pelo Simples Nacional, ou seja, na tela **"Configurações > Cadastros > Empresas > aba Naturezas"** o campo **"Optante pelo SIMPLES"** deve estar assinalado, bem como o campo **"Cód. Regime Tribut."** deve estar definido com a opção **"Simples Nacional"**. Além disso, a empresa cadastrada deve estar inserida (cadastrada) na tela **"Comercial > Preferências > Empresa"**.

#### Estrutura do DeSTDA

Em relação a sua estrutura, o DeSTDA é composto por 3 blocos, sendo um de abertura, **"0"** (tabelas e referências), o **"G"** com os valores da apuração, e o bloco **"9"** sendo o final de encerramento.

![Imagem 4: Em relação a sua estrutura, o DeSTDA é composto por 3 blocos, sendo um de abertura, "0" (tabelas e referências), o "G"…](https://ajuda.sankhya.com.br/hc/article_attachments/8767554967831)

![Imagem 5: Em relação a sua estrutura, o DeSTDA é composto por 3 blocos, sendo um de abertura, "0" (tabelas e referências), o "G"…](https://ajuda.sankhya.com.br/hc/article_attachments/8767590039703)

![Imagem 6: Em relação a sua estrutura, o DeSTDA é composto por 3 blocos, sendo um de abertura, "0" (tabelas e referências), o "G"…](https://ajuda.sankhya.com.br/hc/article_attachments/8767591668503)

![Imagem 7: Em relação a sua estrutura, o DeSTDA é composto por 3 blocos, sendo um de abertura, "0" (tabelas e referências), o "G"…](https://ajuda.sankhya.com.br/hc/article_attachments/8767608812439)

O relatório construído visa fornecer os valores necessários a serem lançados no aplicativo **"SEDIF"** onde serão geradas as apurações da nova declaração acessória imposta aos contribuintes optantes pelo Simples Nacional.

A SEFAZ/PE desenvolveu e fornece o aplicativo SEDIF para todo Brasil, na primeira versão do aplicativo não será possível importar o arquivo TXT gerado pelo Sankhya-Om, dessa forma, vamos fornecer o relatório de apoio para digitação direta no aplicativo.

O relatório será composto por 4 (quatro) partes:

- Inscrições Estaduais em Outras UF's
- ICMS Retido com o Substituto Tributário
- ICMS devido por Aquisições Interestaduais
- PA – Partilha do ICMS na Venda Interestadual para Consumidor  Final

Aqui, teremos o exemplo da disposição dos dados de um relatório gerado:

![Imagem 8: Aqui, teremos o exemplo da disposição dos dados de um relatório gerado:](https://ajuda.sankhya.com.br/hc/article_attachments/8767594902679)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116233-DeSTDA-Declara%C3%A7%C3%A3o-de-Subst-Tribut-e-Difer-Al%C3%ADquota-S-N#top)
