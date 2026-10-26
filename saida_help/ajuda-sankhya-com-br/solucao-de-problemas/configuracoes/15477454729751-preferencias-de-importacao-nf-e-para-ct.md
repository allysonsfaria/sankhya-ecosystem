---
id: "15477454729751"
titulo: "Preferências de importação NF-e para CT-e não encontrada. Configure as preferências para que possa realizar importação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15477454729751-Prefer%C3%AAncias-de-importa%C3%A7%C3%A3o-NF-e-para-CT-e-n%C3%A3o-encontrada-Configure-as-prefer%C3%AAncias-para-que-possa-realizar-importa%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:56:48Z"
rotulos: ["CT-e", "Configuração", "NF-e", "XML", "Importação", "SEFAZ", "CORE_E02462", "Configuração de Preferências de Importação NF-e para CT-e"]
---

# Preferências de importação NF-e para CT-e não encontrada. Configure as preferências para que possa realizar importação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16538041564695) MENSAGEM:**

[CORE\_E02462]: Preferências de importação NF-e para CT-e não encontrada. Configure as preferências para que possa realizar importação.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16538041579287) CAUSA:**

Ocorre quando as preferências de importação NF-e para CT-e não foram devidamente definidas.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16538025591575) SOLUÇÃO:**

Primeiro configure as [Preferências para importação de NF-e p/ CT-e.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDU0MTI2ODEyNTQsInRpY2tldF9pZCI6MTk4MTIxLCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTY1NzgwODA5MX0.77KU6KVQF-vQiu_rzADrBcyeSCc6-wlUef3Uj8xlZD8#prefernciasparaimportaodenf-epct-e)

Uma vez determinadas as preferências para importação, ao acionar a opção **"Importação de NF-e p/ CT-e"** será aberto o seguinte pop-up:

![Imagem 4: Uma vez determinadas as preferências para importação, ao acionar a opção "Importação de NF-e p/ CT-e" será aberto o…](https://ajuda.sankhya.com.br/hc/article_attachments/15477193812887)

![Imagem 5: O processo de importação dos dados da NF-e para lançar um CT-e tem a finalidade de agilizar a operação de lançamento do…](https://ajuda.sankhya.com.br/hc/article_attachments/16538041571095) O processo de importação dos dados da NF-e para lançar um CT-e tem a finalidade de agilizar a operação de lançamento do CT-e da transportadora. Deste modo, é possível que grande parte dos dados do CT-e e das notas transportadas sejam inseridos e em seguida transmitidos à SEFAZ. Através da opção "Importação de NF-e p/ CT-e", tem-se o ponto de partida para este procedimento.

Inicialmente, por meio do campo **"Dados da NF-e"**, determina-se como se dará a importação. Pode-se definir dentre três opções:

- **Importar XML da NF-e:** esta opção é utilizada para importar os dados da NF-e através de um arquivo XML. Por esta alternativa, será possível importar um arquivo na extensão **"XML"** ou ainda no formato **".ZIP"**, sendo este último, contendo vários arquivos. Ao selecionar o(s) arquivo(s) XML é feita uma validação do CNPJ/CPF do emitente, destinatário e transportadora da NF-e. No sistema, o **"Emitente"** e o **"Destinatário"** precisam estar cadastrados como Parceiros, enquanto que a **"Transportadora"** da mercadoria correspondente à nota, precisa estar cadastrada como Empresa.
- **Buscar nota do sistema:** esta indicará a utilização desta opção, quando a Empresa emitente da NF-e e a Empresa Transportadora emitente do CT-e estão na mesma base de dados. Definindo a forma de importação por esta opção, será aberto o pop-up **"Busca Nota Fiscal no Sistema"** para que seja feita a pesquisa de qual nota deseja-se importar para lançar o CT-e. A nota desejada pode ser importada clicando-se duas vezes sobre ela; assim que esta for selecionada, as mesmas validações existentes na importação do XML vão acontecer, exceto as ligadas à validações específicas do arquivo XML. Somente notas fiscais de modelo 1, 4 1B ou 55 confirmadas podem ser utilizadas para lançar o CT-e. uma vez selecionando-se a nota desejada, esta será inserida com as devidas informações.
- **Consultar nota na SEFAZ:** esta opção pode ser empregada em casos que a Empresa transportadora está de posse da chave de acesso da NF-e a ser transportada. Ao utilizar esta opção, será necessário digitar o CAPTCHA (caracteres correspondentes à imagem exibida no lado superior direito do pop-up **"Importação de NF-e p/ CT-e"**) e em seguida bipar, colar ou digitar a chave de acesso da nota. A partir disso, será feita uma consulta da nota no portal da NF-e, assim como é feito através do endereço:

[http://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=](http://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=completa&tip%20oConteudo=XbSeqxE8pl8=)

![Imagem 6: Pré-condição para uso da opção "Importação de NF-e p/ CT-e" , tem-se por meio da opção "Preferências para importação de…](https://ajuda.sankhya.com.br/hc/article_attachments/16538025597079) Pré-condição para uso da opção [**"Importação de NF-e p/ CT-e"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#importaodenf-epct-e), tem-se por meio da opção **"Preferências para importação de NF-e p/ CT-e"** as configurações necessárias para perfeita execução de tal importação. Ao acionar a referida opção, será aberto o seguinte pop-up:

![Imagem 7: Pré-condição para uso da opção "Importação de NF-e p/ CT-e" , tem-se por meio da opção "Preferências para importação de…](https://ajuda.sankhya.com.br/hc/article_attachments/15477303557783)

![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16538041575959) **OBSERVAÇÃO:**

Para mais informações sobre as abas presentes no pop-up, acesse o manual do [portal de vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#importaodenf-epct-e).
