---
id: "360044527393"
titulo: "Manual de balanças no sistema Sankhya "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044527393-Manual-de-balan%C3%A7as-no-sistema-Sankhya"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:55:43Z"
rotulos: ["#PUBLIFER", "Configuração", "#validadoFerreira", "Fast Service", "Sankhya Checkout", "Filizola BP15 Toledo Prix III Toledo 8217", "DLLs e balancas.ini para Fast Service", "Configuração com técnico; homologação necessária para Fast Service/Checkout", "Varejo", "Balanças"]
---

# Manual de balanças no sistema Sankhya 

(1)** Quais as balanças Homologadas para a frente de varejo (Fast Service/Checkout) ?**

- FILIZOLA BP15 (suporta até 30 Kg de pesagem)
- Toledo Prix III
- Toledo Modelo 8217

Para o Fast Service, os arquivos dll's necessários são:

- Balancas.dll
- P05.DLL
- PcScale.dll.
- Arquivo de configuração balancas.ini

As dll's estão anexas no final deste artigo.

Para o **Sankhya Checkout,** não existe a  necessidade Dll , a comunicação é direta

**![Imagem 1: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17005253741591) OBSERVAÇÃO:**

É de suma importância que para a configuração da Balança, o técnico responsável esteja presente no auxilio das configurações .

**![Imagem 2: ATENÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17005233755159) ATENÇÃO:**

- A balança para uso no Fast Service ou no Sankhya checkout necessita estar homologada;
- A balança para uso no Produção/W, Armazéns Gerais ou comercial não necessita estar homologada;
- Os módulos Produção/W, Armazéns Gerais ou Comercial, não se integram com as balanças, a integração é feita pelo WEB Connection e esses módulos apenas leem o que o Web Connection retorna de resultado;

Sobre o **fluxo de atendimento no Service Desk,** em casos de erros de integração da balança, serão revistas as configurações do Web connection, posteriormente, se estiver tudo correto, serão descritas com todas as informações pertinentes da balança e encaminhadas para a indústria realizar a análise.

**![Imagem 3: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/17005253741591) OBSERVAÇÕES:**

- Todas as balanças deverão estar na pasta C:\Windows\System32 (se 32 bits) ou C:\Windows\SysWOW64 (se 64 bits). Caso utilize as dll's atualizadas, anexadas nesse artigo, a pasta do Fast também poderá ser utilizada;
- Essas pastas devem estar liberadas com controle total;
- Na aba **"Parâmetros de Tela",** na Configuração dos Parâmetros do Fast, no campo **"Modelo da balança para cupom"** deve-se escolher a balança desejada;
- Quando for selecionado a Filizola, não será preciso alterar outras definições. Mas quando for informada a 'Toledo', o usuário deverá informar também, na opção **"Porta para balança Toledo"**, a porta em que a balança está conectada e ainda a velocidade de comunicação, na opção **"Velocidade da porta"**, que deve ser verificada no manual da balança;
- Não existe processo adaptativo para Web conection / Balanças;

Artigos relacionados: [Como testar a conexão do Sankhya Web Connection com a balança?](https://ajuda.sankhya.com.br/hc/pt-br/articles/4407158717591-Como-testar-a-conex%C3%A3o-do-Sankhya-Web-Connection-com-a-balan%C3%A7a-)
