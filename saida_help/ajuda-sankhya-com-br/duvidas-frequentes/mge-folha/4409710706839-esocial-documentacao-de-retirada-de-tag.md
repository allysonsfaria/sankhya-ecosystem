---
id: "4409710706839"
titulo: "ESocial - Documentação de retirada de Tag's e Layout"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4409710706839-ESocial-Documenta%C3%A7%C3%A3o-de-retirada-de-Tag-s-e-Layout"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:36:12Z"
rotulos: ["Configuração", "XML", "Atualização", "#validadoRayssa", "eSocial", "Central do eSocial", "Versões atualizadas necessárias", "Simplificação do eSocial conforme nova legislação", "Redução de campos e eventos no eSocial", "Documentos Eletrônicos"]
---

# ESocial - Documentação de retirada de Tag's e Layout

#### Requisitos mínimos

**Versão banco de dados:** 4.40.0.21

**Versão executável:** 4.40.0.21

**Versão Do Sanesocail:** 3.0b1218

**Script do SanEsocial:** Atualizado

#### Imagem 1: Introdução Introdução

Conforme publicada na Portaria Conjunta SEPRT/RFB nº 82, foi aprovado o layout final do eSocial Simplificado, versão S-1.0. O eSocial Simplificado foi previsto na Lei nº 13.874/19.

Os prazos para entrada em vigor de cada fase e da versão Simplificada estão na Portaria Conjunta SEPRT/RFB/ME Nº 71, de 06/2021 e Notas Orientativas e Técnicas.

Houve redução em mais de 30% do número de campos dos layout do eSocial, o que inclui a simplificação de vários eventos e a exclusão total de 12 eventos transmitidos/a transmitir pelas empresas.

#### Imagem 2: Detalhamento das informações retiradas dos respectivos eventos: Detalhamento das informações retiradas dos respectivos eventos:

Todo o projeto original do eSocial passou por uma reformulação e algumas informações foram reduzidas. 

Estas informações não foram retiradas do sistema, porque elas são utilizadas por vários processos. Por exemplo, “nmRazao, natJurid, situacaoPJ” que representam respectivamente Razão Social, Natureza Jurídica e a Situação da Pessoa Jurídica, são utilizadas por processos como NFEe e DIRF.

Vale ressaltar que na prática quando o cliente estiver na tela da Central do eSocial (Pessoal+ ou Pessoal/G) ele verá os eventos, entretanto, se ele observar o arquivo “XML” algumas das informações não estarão mais presentes. A previsão de liberação para o SESMT seria a versão disponível no dia 05/10/2021, e para os demais eventos do eSocial 19/10/2021.

A retirada das informações está condicionada à liberação da versão Simplificada nos respectivos sistemas.

Neste link estão as tag’s, por evento, que foram retiradas na versão simplificada: [Planilha com Detalhamento](https://docs.google.com/spreadsheets/d/1Ngx6EF08Gt9e6gaOxzdR1o9WifNVx9RZLGUIE35dkp8/edit?usp=sharing)

**![Imagem 3: Detalhamento da retirada dos layout (eventos enviados ao RET):](https://ajuda.sankhya.com.br/hc/article_attachments/16089572560407) Detalhamento da retirada dos layout (eventos enviados ao RET):**

Além das informações suprimidas, citadas acima, alguns eventos deixaram de ser enviados na versão Simplificada. Portanto, o cliente quando gerar os eventos na tela Central do eSocial, não verá mais os eventos “S-1030, S-1035, S-1040, S-1050, S-1060, S-1080, S-1250, S-1295, S-1300, S-2221, S-2245, S-2250, S-2260”. Estes eventos deixam inclusive de serem retificados.

Vale ressaltar que alguns eventos deixaram de ser enviados, entretanto, eles estão presentes de forma reduzida em outros eventos. Por exemplo, o S-1030 (Cargos) não será mais enviado, mas o Nome do Cargo e CBO passaram a integrar o evento S-2200 e S-2206, ou o evento S-1060 (Ambiente de Trabalho) que algumas de suas informações compõem o evento S-2240 ou o evento S-2245 que no S-2200 o Código do Treinamento/Capacitação continua sendo exigido. Estes são alguns exemplos, mas há outros casos em outros eventos.

Dos layout mencionados tivemos duas alterações necessárias em telas dos sistemas, que seria a Central do eSocial (Pessoal/G) e a Treinamentos e Capacitações (Pessoal/G e Pessoal+).

**(1)**O botão “Totalização Pagamento Contingência” da **tela Central do eSocial** não estará mais disponível em tela em função da extinção do S-1295;

**(2)**Junto com essa mudança, esta versão passa a aceitar o Fechamento (S-1299) sem que todos os funcionários tenham sido enviados para o Ambiente do eSocial. Nesta situação, junto com o fechamento terá como Aviso/Advertência os funcionários que não foram enviados.

![Imagem 4: (2) Junto com essa mudança, esta versão passa a aceitar o Fechamento (S-1299) sem que todos os funcionários tenham sido…](https://ajuda.sankhya.com.br/hc/article_attachments/4409716778903)

**(1)**Na tela **"Treinamentos e Capacitação"** o campo **“Código do Treinamento/Capacitação no eSocial”** e a aba **"Funcionários"** continuam como obrigatórios, os demais que estavam como obrigatório deixam de ser. Neste local, seriam inseridas informações relativas aos treinamentos, capacitações, exercícios simulados cuja obrigação constar no registro de empregado e prevista nas respectivas NR's. Os códigos de treinamentos escolhidos, são aqueles previstos na “Tabela 28 - Treinamentos, Capacitações, Exercícios Simulados e Outras Anotações” do eSocial.
