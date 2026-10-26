---
id: "32040882123287"
titulo: "org.xml.sax.SAXException: Processing instructions are not allowed within SOAP messages. Esse erro pode ter ocorrido por falta de conexão com a Internet"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32040882123287-org-xml-sax-SAXException-Processing-instructions-are-not-allowed-within-SOAP-messages-Esse-erro-pode-ter-ocorrido-por-falta-de-conex%C3%A3o-com-a-Internet"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-16T14:26:18Z"
rotulos: ["MDF-e", "Configuração", "XML", "SEFAZ", "Passos para resolver", "Razão do erro", "Detalhe do erro", "instructions are not", "within SOAP messages", "org.xml.sax.SAXException: Processing", "Esse erro pode ter ocorrido", "por falta de conexão com a Internet", "Erro", "Documentos Fiscais Eletrônicos", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# org.xml.sax.SAXException: Processing instructions are not allowed within SOAP messages. Esse erro pode ter ocorrido por falta de conexão com a Internet

**MENSAGEM**

org.xml.sax.SAXException: Processing instructions are not allowed within SOAP messages. Esse erro pode ter ocorrido por falta de conexão com a internet.

**SITUAÇÃO**

Este erro ocorre durante operações que envolvem **comunicação com os servidores da SEFAZ**, como:

- Importação de XML no **"Portal de Importação de XML"** (Configurações >> Cadastros >> Portal de Importação de XML)
- Manifestação de destinatário no **"Portal de Importação de XML"** (Configurações >> Cadastros >> Portal de Importação de XML)
- Dar **"Ciência automática"** em notas fiscais eletrônicas
- Geração de **"CT-e"** (Configurações >> Cadastros >> Conhecimento de Transporte Eletrônico)
- Geração de **"MDF-e"** (Configurações >> Cadastros >> Manifesto Eletrônico de Documentos Fiscais)
- Consulta de **"MD-e/DF-e"** (Configurações >> Cadastros >> Manifestação do Destinatário)

**SOLUÇÃO**

A solução depende da causa identificada. Siga as orientações abaixo:

1-Caso seja intabilidade da SEFAZ:

**Solução 1: Aguarde a normalização do serviço da SEFAZ**

**(1)** Aguarde alguns minutos e tente realizar a operação novamente, pois o erro pode ser causado por **instabilidade momentânea nos servidores da SEFAZ**.
**(2)** Verifique se outros usuários ou empresas estão enfrentando o mesmo problema no mesmo período.
**(3)** Consulte o **"Status dos serviços da SEFAZ"** no portal oficial do seu estado para confirmar se há instabilidade reportada.

2- Importação de XML com erro:

**Solução 2: Atualize a versão de consulta do MD-e/DF-e**

**(1)** Acesse a tela **"Configuração MD-e/DF-e"** (Configurações >> Cadastros >> Configuração MD-e/DF-e).
**(2)** Localize o campo **"Versão de consulta"** e altere para **"NT-2014 Distribuição"**.
**(3)** Salve as alterações e tente realizar a operação novamente.

3-Transmissão das notas:

**Solução 3: Reimporte o certificado digital**

**(1)** Acesse a tela **"Preferências"** (Configurações >> Empresa >> Preferências).
**(2)** Localize a aba de **"Configurações fiscais"** e reimporte o **"Certificado digital"** da empresa.
**(3)** Certifique-se de que o certificado está válido.
**(4)** Salve as configurações e tente realizar a operação novamente.

**Solução 4: Habilite o modo síncrono para XML**

**(1)** Acesse a tela **"Preferências"** (Comercial >> Preferências >> Empresa).
**(2)** Navegue até a aba **"Documentos Fiscais Eletrônicos"**, em cada sub-aba disponível (como **NF-e, NFC-e, CT-e, MDF-e**, entre outras, conforme utilizado), localize o campo **“Usar modo síncrono para envio do XML”**.
**(3)** Altere o valor para **"Sim"** e salve.
![Print modo síncrono](https://ajuda.sankhya.com.br/hc/article_attachments/32040882109207)

Nota: Para utilizar esta funcionalidade é necessário estar na versão 4.24b234, 4.25b238, 4.26b209, 4.27b85, 4.28b26 ou superior.

**Solução 5: Atualize a nota técnica**

**(1)** Acesse a tela **"Preferências"** (Configurações >> Empresa >> Preferências).
**(2)** Em todas as abas (como **NF-e, NFC-e, CT-e, MDF-e**, entre outras)  atualize todas para a **última nota técnica disponível**.
**(3)** Salve as alterações e tente novamente.

![Imagem 2: (1) Acesse a tela "Preferências" (Configurações >> Empresa >> Preferências). (2) Em todas as abas (como NF-e, NFC-e,…](https://ajuda.sankhya.com.br/hc/article_attachments/43533781133591)

**CAUSA**

Este erro ocorre quando há **falha na comunicação** entre o sistema e os servidores da SEFAZ, resultando em um retorno inválido (não XML). Isso pode ser causado por:

- Instabilidade momentânea nos servidores da SEFAZ;
- Perda de conexão com a internet;
- Versão de consulta desatualizada;
- Certificado digital com problemas;
- Necessidade de ativação do modo síncrono para o envio de MDF-e, conforme as novas determinações da SEFAZ.
