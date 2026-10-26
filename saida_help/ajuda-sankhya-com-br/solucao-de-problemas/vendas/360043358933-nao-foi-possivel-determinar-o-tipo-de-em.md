---
id: "360043358933"
titulo: "Não foi possível determinar o tipo de emissão das notas da empresa X para o estado 'UF'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043358933-N%C3%A3o-foi-poss%C3%ADvel-determinar-o-tipo-de-emiss%C3%A3o-das-notas-da-empresa-X-para-o-estado-UF"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:36Z"
rotulos: ["CORE_E04876", "Configuração", "NF-e", "Portal de Vendas", "SEFAZ", "CORE_E03988", "Verifique SEF rede certificado digital", "Não determinar tipo de emissão", "Configurar URLs e testes de conectividade", "Certificado Digital", "Erro"]
---

# Não foi possível determinar o tipo de emissão das notas da empresa X para o estado 'UF'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16115858504471) MENSAGEM:**

[CORE\_E04876] Não foi possível determinar o tipo de emissão das notas da empresa X para o estado 'UF'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16115858507415) SITUAÇÃO:**

Ao acessar o Portal de Vendas, selecionar uma NF-e e tentar consultar Situação do Serviço ou Gerar Lote, apresenta a mensagem.

**![Imagem 3: CAUSAS:](https://ajuda.sankhya.com.br/hc/article_attachments/16115841232663) CAUSAS:**

![Imagem 4: Serviço inoperante ou com instabilidade de Recepção/Consulta da SEFAZ Estadual/Nacional.](https://ajuda.sankhya.com.br/hc/article_attachments/16115858512663) Serviço inoperante ou com instabilidade de Recepção/Consulta da SEFAZ Estadual/Nacional.

![Imagem 5: Problemas na infra estrutura de rede ou no servidor onde está instalado o aplicativo SANNFE, impedindo a comunicação…](https://ajuda.sankhya.com.br/hc/article_attachments/16115841226391) Problemas na infra estrutura de rede ou no servidor onde está instalado o aplicativo SANNFE, impedindo a comunicação com a SEFAZ.

![Imagem 6: Certificado Digital vencido.](https://ajuda.sankhya.com.br/hc/article_attachments/16115841228311) Certificado Digital vencido.

![Imagem 7: Atualizou o(s) Certificado(s), porém não reiniciou o SANNFE ou o SankhyaW.](https://ajuda.sankhya.com.br/hc/article_attachments/16115841235863) Atualizou o(s) Certificado(s), porém não reiniciou o SANNFE ou o **SankhyaW.**

![Imagem 8: Empresa sem um tipo de contingencia definido nas preferências da empresa, campo "Envio em Contingência" configurado…](https://ajuda.sankhya.com.br/hc/article_attachments/16115858525207) Empresa sem um tipo de contingencia definido nas preferências da empresa, campo **"Envio em Contingência"** configurado como **"Não usar contingência"**.

**![Imagem 9: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16115858509719) SOLUÇÃO:**

![Imagem 10: Entre em contato via telefone ou outro canal disponível com a Sefaz Estadual, para verificar Instabilidades no Serviço…](https://ajuda.sankhya.com.br/hc/article_attachments/16115858512663) Entre em contato via telefone ou outro canal disponível com a Sefaz Estadual, para verificar Instabilidades no Serviço da SEFAZ.

![Imagem 11: Verifique com a área de TI da empresa se o Servidor onde está instalado o SANNFE está com acessos a porta 9090,…](https://ajuda.sankhya.com.br/hc/article_attachments/16115841226391) Verifique com a área de TI da empresa se o Servidor onde está instalado o SANNFE está com acessos a porta 9090, liberado em firewall ou proxy e com acesso a Internet.

![Imagem 12: Efetue a substituição caso o Certificado Digital esteja vencido. O Certificado Digital A1 é o único compatível com os…](https://ajuda.sankhya.com.br/hc/article_attachments/16115841228311) Efetue a substituição caso o Certificado Digital esteja vencido. O Certificado Digital A1 é o único compatível com os sistemas Sankhya, ele precisa ser substituído anualmente e podem ser adquiridos em sites específicos ou Correios, Caixa Econômica, Serasa e outros.

![Imagem 13: Verifique se a URL informada na aba Status do Serviço campo "Configuração e teste de conectividade com a internet" está…](https://ajuda.sankhya.com.br/hc/article_attachments/16115841235863) Verifique se a URL informada na aba Status do Serviço campo **"Configuração e teste de conectividade com a internet"** está correto.

**(1)**O SanNFe necessita de conexão com a internet para consumir os serviços da Receita Estadual ou Federal. Por esse motivo foi incluído teste de conectividade para evitar problemas na execução do serviços.

A lista de URLs informada no console tem por objetivo validar se a máquina a qual o SanNFe está instalado tem conexão com a Internet.
Ao ser instalado o SanNFe essa lista de URLs vem vazia, nesse caso, o SanNFe não executa a validação da conexão antes de executar algum serviço. Por isso, quando a máquina não tem conexão com a Internet, a falha vai ocorrer ao executar o serviço, ou seja, na emissão da nota pelo MGE, Mitra ou SankhyaW. Quando não configurado o teste e ao ocorrer o erro na execução a fim de facilitar a detecção de problemas o SanNFe faz o teste de conectividade com a URL: http://www.receita.fazenda.gov.br. Quando não há conexão, é incluído na mensagem de erro, que a possível causa pode ser a falta de conexão.
Quando informado alguma URL na lista, o SanNFe passa a validar a conexão por meio dessa URL, o teste de conexão consiste um acesso bem sucedido ao site endereçado pela URL. Em caso de falha, não será permitido a execução de nenhum serviço. Caso exista mais de uma URL na lista, a aplicação considera o teste bem sucedido para a primeira URL acessada.

(1)** Características do painel de testes:**

- Para adicionar uma url na lista, basta informar o endereço válido, exemplo: <http://www.sankhya.com.br> em seguida, selecione o botão com ícone de + para incluir na lista;
- Após adicionado as URLs é necessário selecionar o botão Salvar lista, esse botão salva lista de URLs no arquivo de configuração do SanNFe (conf/san-nfe.conf);
- O botão Testa efetua o teste de conexão para todas as URLs incluídas na lista, um teste bem sucedido marca a URL com o ícone na cor verde, caso contrário, um ícone na cor vermelha é apresentada.
- A lista de URL é armazenada no arquivo de configuração do SanNFe por meio da propriedade: internet.test.urls=<lista de URLs>, onde cada URL é separada por virgula. Por exemplo:
  internet.test.urls=http://www.sankhya.com.br,http://www.jiva.com.br
- As URLs para execução serviços Web(webServices) executados pelo SanNFe diferem de estado para estado. Para não ter que liberar acesso completo da máquina basta liberar por meio de NAT(Network Address Translation) os endereços referentes ao estado que será emitido a NFe para a porta 443(HTTPS).
- Como exemplo as URLs dos webservices para o estado de MG são:
  - <https://nfe.fazenda.mg.gov.br/nfe/services/NfeRecepcao>
  - <https://nfe.fazenda.mg.gov.br/nfe/services/NfeRetRecepcao>
  - <https://nfe.fazenda.mg.gov.br/nfe/services/NfeCancelamento>
  - <https://nfe.fazenda.mg.gov.br/nfe/services/NfeInutilizacao>
  - <https://nfe.fazenda.mg.gov.br/nfe/services/NfeConsulta>
  - <https://nfe.fazenda.mg.gov.br/nfe/services/NfeStatusServico>
- O endereço à liberar deve ser: nfe.fazenda.mg.gov.br para a porta 443.
- A lista dos endereços para os outros estados podem ser encontradas no arquivo de urls conf/url-webservices.xml ou no site da [Receita Federal.](http://www.nfe.fazenda.gov.br/portal/Default.aspx)

**(1)** A Sankhya recomenda que sempre mantenha o SANNFE atualizado e compatível com a versão do **SankhyaW**. Esta compatibilidade pode ser consultada através do site <http://downloads.sankhya.com.br/> em **Requisitos** opção encontrada logo a frente de cada pacote disponível.
