---
id: "14651356449943"
titulo: "Configurações para geração dos eventos R-2050 e R-2055 EFD REINF Alterações decorrem da Medida Provisória nº 1.166/2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14651356449943-Configura%C3%A7%C3%B5es-para-gera%C3%A7%C3%A3o-dos-eventos-R-2050-e-R-2055-EFD-REINF-Altera%C3%A7%C3%B5es-decorrem-da-Medida-Provis%C3%B3ria-n%C2%BA-1-166-2023"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:58:18Z"
rotulos: ["Configuração", "Impostos", "EFD", "Validação de CNPJ", "R-2050: Indicador Comercialização", "R-2055: Indicador Aquisição", "Reinf", "MP 1166/2023"]
---

# Configurações para geração dos eventos R-2050 e R-2055 EFD REINF Alterações decorrem da Medida Provisória nº 1.166/2023

(1)** R-2050** **– Comercialização de produção:** receitas informadas com o indicativo de comercialização {indCom} igual a “8 - Comercialização da produção para entidade executora do PAA” não mais geraram o código de receita “1213” a recolher no totalizador R-9001.

![Imagem 1: O sistema busca a informação no campo " Indicador de Comercialização":](https://ajuda.sankhya.com.br/hc/article_attachments/16969625235991) O sistema busca a informação no campo **"Indicador de Comercialização":** 

![Imagem 2: O sistema busca a informação no campo " Indicador de Comercialização":](https://ajuda.sankhya.com.br/hc/article_attachments/14651232381335)

(1)** R-2055** **- Aquisição de produção rural:** aquisições informadas por contribuinte pessoa jurídica com os indicativos {indAquis} igual a “3 - Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA” ou “6 - Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA - Produção isenta (Lei 13.606/2018)” gerarão o código de receita “1213” a recolher no totalizador R-9001.

![Imagem 3: O sistema busca a informação no campo "I ndicador de aquisição":](https://ajuda.sankhya.com.br/hc/article_attachments/16969625235991)  O sistema busca a informação no campo **"Indicador de aquisição":**

![Imagem 4: O sistema busca a informação no campo "I ndicador de aquisição":](https://ajuda.sankhya.com.br/hc/article_attachments/14651175835799)

![Imagem 5: Se não tiver escolhido nenhuma opção acima, o sistema valida o CNPJ da empresa com 14 caracteres, se tiver, o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/16912762376983) Se não tiver escolhido nenhuma opção acima, o sistema valida o CNPJ da empresa com 14 caracteres, se tiver, o sistema vai lançar 1 na tag.

![Imagem 6: Se o CNPJ não tiver 14 caracteres, o sistema vai validar o seguinte campo nas preferências da " Empresa" (Caminho de…](https://ajuda.sankhya.com.br/hc/article_attachments/16912749714839) Se o CNPJ não tiver 14 caracteres, o sistema vai validar o seguinte campo nas preferências da **"Empresa"**(Caminho de acesso: Comercial » Preferências » Empresa):

![Imagem 7: Se o CNPJ não tiver 14 caracteres, o sistema vai validar o seguinte campo nas preferências da " Empresa" (Caminho de…](https://ajuda.sankhya.com.br/hc/article_attachments/14651179900951)

![Imagem 8: S e ele estiver desmarcado, o sistema vai lançar o valor 2 na tag, caso nenhuma configuração acima for verdadeira, o…](https://ajuda.sankhya.com.br/hc/article_attachments/16912749716631) Se ele estiver desmarcado, o sistema vai lançar o valor 2 na tag, caso nenhuma configuração acima for verdadeira, o sistema vai lançar o valor 3 na tag.

![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16969719491991) **OBSERVAÇÃO:**

[Alterações decorrentes da Medida Provisória nº 1.166/2023](http://sped.rfb.gov.br/pagina/show/7191)
