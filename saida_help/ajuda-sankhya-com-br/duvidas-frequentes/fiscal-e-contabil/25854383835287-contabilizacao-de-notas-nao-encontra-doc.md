---
id: "25854383835287"
titulo: "Contabilização de notas não encontra documentos para contabilizar - Tela Agendamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25854383835287-Contabiliza%C3%A7%C3%A3o-de-notas-n%C3%A3o-encontra-documentos-para-contabilizar-Tela-Agendamento"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:44:12Z"
rotulos: ["CT-e", "Configuração", "NF-e", "TOP", "Contabilização", "Documentos Eletrônicos"]
---

# Contabilização de notas não encontra documentos para contabilizar - Tela Agendamento

Ao executar a rotina de contabilização, na tela **"Agendamento"**(Caminho: Contabilização » Rotinas » Agendamento), tem-se a quantidade de documentos encontrados na busca realizada pela aplicação e a quantidade que foram ou não foram contabilizados.

Nesse artigo será tratado sobre a quantidade "encontrada para ser contabilizada".

![Imagem 1: Nesse artigo será tratado sobre a quantidade "encontrada para ser contabilizada".](https://ajuda.sankhya.com.br/hc/article_attachments/25912151208983)

A primeira análise a ser realizada é sobre o filtro criado na tela Agendamento, na aba **"Filtros"**.

![Imagem 2: A primeira análise a ser realizada é sobre o filtro criado na tela Agendamento , na aba "Filtros" .](https://ajuda.sankhya.com.br/hc/article_attachments/25912192450327)

As regras definidas pelo usuário (personalizadas no filtro) impactam nas buscas dos documentos e devem ser **validadas** sempre que houver esse tipo de problema, além das regras fixas da busca. Sobre estas regras "fixas":

![Imagem 3: A nota deve estar confirmada;](https://ajuda.sankhya.com.br/hc/article_attachments/25911404992151) A nota deve estar confirmada;

![Imagem 4: A TOP usada na operação, em seu cadastro, na aba "Geral" , deve estar com o campo "Atualiza Contabilidade" marcado;](https://ajuda.sankhya.com.br/hc/article_attachments/25911404998295) A TOP usada na operação, em seu cadastro, na aba **"Geral"**, deve estar com o campo **"Atualiza Contabilidade"** marcado;

![Imagem 5: Na tela "TOP Contabilização" o mesmo campo A tualiza contabilidade deve estar marcado;](https://ajuda.sankhya.com.br/hc/article_attachments/25911430129943) Na tela **"TOP Contabilização"** o mesmo campo Atualiza contabilidade deve estar marcado;

![Imagem 6: Se tratando de uma NF-e, existem as seguintes regras:](https://ajuda.sankhya.com.br/hc/article_attachments/25911405003159) Se tratando de uma NF-e, existem as seguintes regras:

**(1)** Nas preferências da empresa (Caminho: Comercial » Preferências » Empresa), aba Documentos Fiscais Eletrônicos **>** NF-e/NFC-e **>** Geral **>** o campo "**Ambiente NF-e/NFC-e:**" deve estar marcado como **produção ou homologação**.

(1)**Sendo uma nota de emissão própria:** no cadastro da TOP, o campo **"NF-e"** deve estar com uma dessas opções: **Ajuste, Complementar, Devolução, Import. Doc. (Emissão Própria) e Normal.**

**(1)** Campo STATUS NF-e deve estar como **APROVADA.**

**(1)** Se o STAUTUS NF-e estiver como "**denegada**", o campo Emissão NF-e (cabeçalho) deve estar com uma das opções: **Danfe de Segurança Ou Conting.Off-Line NFC-e**.

![Imagem 7: Se tratando de documento do tipo CT-e:](https://ajuda.sankhya.com.br/hc/article_attachments/25911405009175) Se tratando de documento do tipo CT-e:

**(1)** Nas preferências da empresa (Caminho: Comercial » Preferências » Empresa), na aba Documentos Fiscais Eletrônicos **> CT-e** > o campo **"Ambiente CT-e"** deve estar marcado como **homologação ou produção.**

**(1)**No cadastro da TOP, o campo CT-e, não pode estar como **"não usa"**.

**(1)** Sendo um documento de emissão própria, o STATUS CT-e deve ser '**aprovado**'.

![Imagem 8: O documento não pode já estar contabilizado, este é um dos pontos que mais causa este tipo de problema. Veja a seguir a…](https://ajuda.sankhya.com.br/hc/article_attachments/25911851539991) **O documento não pode já estar contabilizado, este é um dos pontos que mais causa este tipo de problema.** Veja a seguir a melhor forma via sistema para verificar se o documento foi contabilizado, e uma maneira via consulta no banco de dados (tela DBExplorer) que também vai ajudar nessa análise:

**(1)** Temos o parâmetro **"EXIBECOLANCONT"** que ativa na tela **"Lançamentos Contábeis"** (Caminho: Contabilidade » Arquivos » Lançamentos contábeis) o campo de número único. Dessa forma, é possível fazer uma consulta por esse número e, se retornar na consulta, tem-se o motivo pelo qual tal documento ou documentos, não foram contabilizados, pois só podem ser contabilizados uma única vez.

**Observação:** uma dica é realizar uma consulta do ano todo e em todas as empresas que recebem contabilizações, pois não é incomum documentos serem contabilizados em empresas e períodos incorretos, por acidente.

![Imagem 9: Observação: uma dica é realizar uma consulta do ano todo e em todas as empresas que recebem contabilizações, pois não é…](https://ajuda.sankhya.com.br/hc/article_attachments/25912192460055)

**(1)** Pela consulta no **DBExplorer** pode-se rodar o seguinte comando na tela citada, substituindo os pontos de interrogação, pelo número único do(s) documento(s) em questão. Se retornar alguma informação é porque de fato já está contabilizado e podemos verificar em qual empresa, referência, lote, lançamento que a contabilização foi realizada. Assim é possível ajustar a situação, excluindo a contabilização e refazendo corretamente:

**SELECT \* FROM TCBINT WHERE ORIGEM = 'E' AND NUNICO = ???**
