---
id: "24102304335767"
titulo: "Configurações necessárias para emissão da NFS-e Padrão Prefeitura através do Micro Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24102304335767-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-emiss%C3%A3o-da-NFS-e-Padr%C3%A3o-Prefeitura-atrav%C3%A9s-do-Micro-Servi%C3%A7o"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:42:41Z"
rotulos: ["Configuração", "Parceiro", "Prefeituras", "NFS-e", "Emissão da Nota Fiscal de Serviço Eletrônica via Micro Serviço", "\"Configurar Credenciais\"", "microserviço", "NFS-e Padrão Prefeitura", "Documentos Eletrônicos", "Micro Serviço"]
---

# Configurações necessárias para emissão da NFS-e Padrão Prefeitura através do Micro Serviço

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310508581911) Versão disponível: a partir da 4.23B212
```

---

Neste artigo serão apresentadas as etapas para a integração com Parceiros que realizam a emissão da NFS-e via Micro Serviço. 

| Configurações e telas envolvidas |
| --- |
| [Emissão da Nota Fiscal de Serviço Eletrônica via Micro Serviço - Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/24102304335767-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-emiss%C3%A3o-da-NFS-e-Padr%C3%A3o-Prefeitura-atrav%C3%A9s-do-Micro-Servi%C3%A7o#Emiss%C3%A3odaNotaFiscaldeServi%C3%A7oEletr%C3%B4nicaviaMicroServi%C3%A7oConfigura%C3%A7%C3%B5es) |
| [Emissão da Nota Fiscal de Serviço Eletrônica Padrão Nacional via Micro Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/24102304335767-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-emiss%C3%A3o-da-NFS-e-Padr%C3%A3o-Prefeitura-atrav%C3%A9s-do-Micro-Servi%C3%A7o#Emiss%C3%A3odaNotaFiscaldeServi%C3%A7oEletr%C3%B4nicaPadr%C3%A3oNacionalviaMicroServi%C3%A7o) |
| [Geração do JSON Processado](https://ajuda.sankhya.com.br/hc/pt-br/articles/24102304335767-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-emiss%C3%A3o-da-NFS-e-Padr%C3%A3o-Prefeitura-atrav%C3%A9s-do-Micro-Servi%C3%A7o#Gera%C3%A7%C3%A3odoJSONProcessado) |
| [Artigos relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/24102304335767-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-emiss%C3%A3o-da-NFS-e-Padr%C3%A3o-Prefeitura-atrav%C3%A9s-do-Micro-Servi%C3%A7o#Artigosrelacionados) |

---

### Emissão da Nota Fiscal de Serviço Eletrônica via Micro Serviço - Configurações

![Imagem 2: As empresas dos municípios implementados via Micro Serviço devem solicitar o credenciamento da empresa com o time de…](https://ajuda.sankhya.com.br/hc/article_attachments/25334215991831) As empresas dos municípios implementados via Micro Serviço devem solicitar o credenciamento da empresa com o time de atendimento.

![Imagem 3: No cadastro de Empresas , na aba Naturezas , realize os ajustes abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/24102320828951) No cadastro de [Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas), na aba [Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abanaturezas), realize os ajustes abaixo:

- No campo **"Cód. Regime Tribut."** escolha a opção relacionada ao regime tributário da empresa;
- Caso ela seja optante pelo Simples Nacional, selecione a opção que mais se enquadra na situação do contribuinte no campo **"Tipo de Partilha/Anexo SN"**.

![Imagem 4: Caso ela seja optante pelo Simples Nacional, selecione a opção que mais se enquadra na situação do contribuinte no…](https://ajuda.sankhya.com.br/hc/article_attachments/24127758086679)

Caso o município suporte a substituição ou o cancelamento de notas via webservice, siga as orientações:

![Imagem 5: Na tela Cidades , selecione as cidades a serem utilizadas na emissão e acione a marcação "Tem substituição NFS-e" da…](https://ajuda.sankhya.com.br/hc/article_attachments/24102304299927) Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), selecione as cidades a serem utilizadas na emissão e acione a marcação **"Tem substituição NFS-e"** da aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e).

Ainda na aba acima, configure o campo **"Tipo de Cancelamento para NFS-e"** e cadastre o **"Tipo"**, **"Código"**, **"Motivo/Descrição"** e **"Enviar à prefeitura"**, conforme definido pelo manual.

![Imagem 6: Ainda na aba acima, configure o campo "Tipo de Cancelamento para NFS-e" e cadastre o "Tipo" , "Código" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/24102304303639)

![Imagem 7: Em Preferências da Empresa , aba Documentos Fiscais Eletrônicos , sub-aba NFS-e > Geral configure conforme as regras do…](https://ajuda.sankhya.com.br/hc/article_attachments/24102304305687) Em [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) configure conforme as regras do município da empresa.

Para isso, se atente as configurações da seção **"Credenciais de Login de Prefeitura"**, caso a emissão da NFS-e seja por usuário e senha, estes deverão ser informados nessa sessão, como: token, frase de segurança, entre outros.

**Nota**: o botão ![Imagem 8: Nota : o botão "Configurar Credenciais" só estará visível para as prefeituras já contempladas no micro serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/24127798589847) **"Configurar Credenciais"** só estará visível para as prefeituras já contempladas no micro serviço.

![Imagem 9: Nota : o botão "Configurar Credenciais" só estará visível para as prefeituras já contempladas no micro serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/24102304316567)

Assim, ao clicar no botão Configurar Credenciais será apresentado o pop-up **"Credenciais de login da prefeitura"** onde os dados já cadastradas para gerar as credenciais serão apresentados e utilizadas para a emissão das NFS-e's junto à Prefeitura da cidade.

![Imagem 10: Lembre-se que, caso não possua as informações das credenciais, deverá procurar o contador de sua empresa ou sua…](https://ajuda.sankhya.com.br/hc/article_attachments/24102320859031) Lembre-se que, caso não possua as informações das credenciais, deverá procurar o contador de sua empresa ou sua Prefeitura.

![Imagem 11: Lembre-se que, caso não possua as informações das credenciais, deverá procurar o contador de sua empresa ou sua…](https://ajuda.sankhya.com.br/hc/article_attachments/24102304322199)

Caso o campo **"Cód. Regime Tribut."**do cadastro de Empresas, aba Naturezas, esteja configurado com a opção **"Regime Normal"**, selecione o **"Tipo de Regime"** que a empresa faça parte, podendo ser **"Lucro Presumido"** ou **"Lucro Real"**.

**Nota:** esse campo estará visível somente quando o campo Cód. Regime Tribut. estiver configurado com a opção Regime Normal.

Confira todas as informações e dados do Certificado Digital, e acione o botão ![Imagem 12: Confira todas as informações e dados do Certificado Digital, e acione o botão "Confirmar" .](https://ajuda.sankhya.com.br/hc/article_attachments/24104061535255) **"Confirmar"**.

Neste momento será efetuada uma validação das informações da Empresa, como: informações de login e informações do certificado digital válido para o CNPJ da empresa selecionada na tela.

Caso apresente alguma inconsistência no cadastro, o sistema exibirá mensagens de aviso, informando qual o erro encontrado.

Tendo concluído a configuração, será apresentada a seguinte mensagem:

**“Suas informações foram validadas e você está pronto para emitir NFS-e!”**

E o campo **"Status"** será alterado para **"Credenciais Configuradas"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/24102304335767-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-emiss%C3%A3o-da-NFS-e-Padr%C3%A3o-Prefeitura-atrav%C3%A9s-do-Micro-Servi%C3%A7o#top)

### Emissão da Nota Fiscal de Serviço Eletrônica Padrão Nacional via Micro Serviço

Para configurar a emissão de notas no padrão nacional via Micro Serviço, acesse o artigo [Emissão da Nota Fiscal de Serviço Eletrônica Padrão Nacional via Micro Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/22378207317783-Emiss%C3%A3o-da-Nota-Fiscal-de-Servi%C3%A7o-Eletr%C3%B4nica-Padr%C3%A3o-Nacional-via-Micro-Servi%C3%A7o).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/24102304335767-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-emiss%C3%A3o-da-NFS-e-Padr%C3%A3o-Prefeitura-atrav%C3%A9s-do-Micro-Servi%C3%A7o#top)

### Geração do JSON Processado

O JSON processado é utilizado para auxiliar na verificação das informações integradas com a prefeitura por meio de um Micro Serviço. 

Para gerar o JSON processado, acesse o [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), clique no botão **"NFS-e"** e selecione a opção **"Baixar JSON Processado"** para realizar o download do arquivo JSON. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/24102304335767-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-emiss%C3%A3o-da-NFS-e-Padr%C3%A3o-Prefeitura-atrav%C3%A9s-do-Micro-Servi%C3%A7o#top)

### Artigos relacionados

![Imagem 13: Para mais informações acesse os seguintes artigos:](https://ajuda.sankhya.com.br/hc/article_attachments/24102320862359)  Para mais informações acesse os seguintes artigos:

- [Configurações gerais para NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047599473-Configura%C3%A7%C3%B5es-gerais-para-NFS-e);
- [Nota Fiscal Eletrônica de Serviço - Prefeituras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras);
- [Funcionalidades relacionadas à NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e%C2%A0);
- [Cancelamento de NFS-e Prefeituras que não possuem o processo via webservices](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#cancelamentodenfs-e-prefeiturasquenopossuemoprocessoviawebservices);
- [Informações Complementares](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares%C2%A0);
- [Modelo de impressão de Nota Fiscal Eletrônica de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/13309860712087-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7os-NFS-e%C2%A0);
- [Nota Fiscal Eletrônica de Serviço - Prefeituras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras#Especifica%C3%A7%C3%B5esporPrefeituras%C2%A0);
- [Emissão da Nota Fiscal de Serviço Eletrônica Padrão Nacional via Micro Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/22378207317783-Emiss%C3%A3o-da-Nota-Fiscal-de-Servi%C3%A7o-Eletr%C3%B4nica-Padr%C3%A3o-Nacional-via-Micro-Servi%C3%A7o).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/24102304335767-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-emiss%C3%A3o-da-NFS-e-Padr%C3%A3o-Prefeitura-atrav%C3%A9s-do-Micro-Servi%C3%A7o#top)
