---
id: "360046326313"
titulo: "Discriminação do Serviço 999 Campo Discriminação de Serviço não informado e/ou fora dos padrões estabelecidos no layout Informar a Discriminação do Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046326313-Discrimina%C3%A7%C3%A3o-do-Servi%C3%A7o-999-Campo-Discrimina%C3%A7%C3%A3o-de-Servi%C3%A7o-n%C3%A3o-informado-e-ou-fora-dos-padr%C3%B5es-estabelecidos-no-layout-Informar-a-Discrimina%C3%A7%C3%A3o-do-Servi%C3%A7o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:32:39Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "Prefeituras", "NFS-e", "Corrigir parâmetros", "Redigitar serviço", "Discriminação inválida", "Erro"]
---

# Discriminação do Serviço 999 Campo Discriminação de Serviço não informado e/ou fora dos padrões estabelecidos no layout Informar a Discriminação do Serviço

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18979319550231) MENSAGEM**:

Discriminação do Serviço 999 Campo Discriminação de Serviço não informado e/ou fora dos padrões estabelecidos no layout Informar a Discriminação do Serviço

**![Imagem 2: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/18979336259351) CAUSA**:

Ocorre quando a discriminação do serviço esta com caracteres inválidos, ou caso haja observação, devera ser precedido do |(pipe) como separador de informação, sem Enter, para pular de linha.

**![Imagem 3: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/18979336268311) SOLUÇÃO**:

![Imagem 4: Acesse a tela Preferências (Configurações » Avançado » Preferências) informe a chave do parâmetro "Campos para montar a…](https://ajuda.sankhya.com.br/hc/article_attachments/18979336278039) Acesse a tela **Preferências** (Configurações » Avançado » Preferências) informe a chave do parâmetro **"Campos para montar a descrição dos serviços NFSE - NFSEDESCRSERV".**

Verifique a condição do parâmetro acima, para a montagem da Discriminação do serviço.
Se houver informação neste parâmetro, sistema usara para montar a discriminação do serviço, então acesse o cadastro do Serviço.

![Imagem 5: Verifique a condição do parâmetro acima, para a montagem da Discriminação do serviço. Se houver informação neste…](https://ajuda.sankhya.com.br/hc/article_attachments/18979319571607) Acesse o cadastro do **Serviço** (Configurações » Cadastros » Produtos » Serviço). Sugerimos analisar os campos: Descrição, Descrição para complemento, Características

**Observação:** Algumas prefeituras, aceitam o campo Observação dos itens como parte da Discriminação do Serviço, sempre precedido do carácter **|**(pipe), para separar as informações. Não podendo haver caracteres inválidos ou espaço entre as informações.

**Exemplo:**

Unidade Cejam**|**Produtividade referente ao mês de marco/20 = Qtde de exames: 83.963 = R$ 7.800,16**|**Unidade Rodeio**|**Produtividade referente ao mês de marco/20 = Qtde de exames: 4.016 = R$ 373,09

![Imagem 6: Após os ajustes, redigite o serviço na Nota Fiscal de serviço e faça a transmissão novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/18979319576599) Após os ajustes, redigite o serviço na Nota Fiscal de serviço e faça a transmissão novamente.
