---
id: "26998637309463"
titulo: "Erro MS1441 - vlrBaseAgreg e Erro MS1449 - vlrAgreg - EFD Reinf"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26998637309463-Erro-MS1441-vlrBaseAgreg-e-Erro-MS1449-vlrAgreg-EFD-Reinf"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:40:21Z"
rotulos: ["Configuração", "Impostos", "Natureza", "EFD Reinf", "Erro MS1441", "vlrBaseAgreg", "Erro MS1449", "vlrAgreg - EFD Reinf", "Erro", "Tributo"]
---

# Erro MS1441 - vlrBaseAgreg e Erro MS1449 - vlrAgreg - EFD Reinf

![Imagem 1: MENSAGEM](https://ajuda.sankhya.com.br/hc/article_attachments/27118915562135) **MENSAGEM**

**Erro MS1441 - vlrBaseAgreg** - Informação permitida apenas se, para a natureza do rendimento informada em (natRend), houver 'Agregado' na coluna 'Tributo' da Tabela 1. Localiza??o: - Campo: vlrBaseAgreg - XPATH: /Reinf/evtRetPJ/ideEstab/ideBenef/idePgto/infoPgto/retencoes/vlrBaseAgreg

**Erro MS1449 - vlrAgreg** - Informação permitida apenas se, para a natureza do rendimento informada em (natRend), houver 'AGREGADO' na coluna 'Tributo' da Tabela 1. Localiza??o: - Campo: vlrAgreg - XPATH: /Reinf/evtRetPJ/ideEstab/ideBenef/idePgto/infoPgto/retencoes/vlrAgreg

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27118899046551)SOLUÇÃO:**

Para corrigir os erros **MS1441** e **MS1449**, é necessário identificar as naturezas de rendimento associadas a tributos **agregados**. Essas informações são fundamentais para determinar quando os campos relacionados a agregados podem ser preenchidos.

**Tabela 1:** <http://sped.rfb.gov.br/arquivo/show/7134>

No link acima é possível baixar a tabela 1 que está disponível na extensão [xlsx](http://sped.rfb.gov.br/arquivo/download/7134), e na tabela tem uma coluna nomeada de tributo. Ao criar um filtro, pode-se filtrar nessa tabela as naturezas de rendimentos com tipo de tributo agregado.

![Imagem 3: No link acima é possível baixar a tabela 1 que está disponível na extensão xlsx , e na tabela tem uma coluna nomeada de…](https://ajuda.sankhya.com.br/hc/article_attachments/27116305636887)

Na tela **"Impostos",** sub-abas **"Parceiro"**, **"TOP", "Empresa", "Grupo de Produto", "Produto", "Serviço",** informe o Código da Receita no campo **"Cód.Receita"** que indica recolhimento com cálculo

![Imagem 4: Na tela "Impostos", sub-abas "Parceiro" , "TOP", "Empresa", "Grupo de Produto", "Produto", "Serviço", informe o Código…](https://ajuda.sankhya.com.br/hc/article_attachments/27116305645591)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27118915570199)CAUSA:**

Na **EFD-Reinf** as naturezas de rendimento e seus respectivos tributos (incluindo se são agregados ou não) estão listados na **Tabela 1** do manual da EFD-Reinf, que é essencial para definir corretamente os valores que podem ser informados nos campos como vlrBaseAgreg e vlrAgreg.
