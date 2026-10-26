---
id: "4412685460887"
titulo: "Atualização das Tabelas Dinâmicas e Importação do plano de Contas Referencial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4412685460887-Atualiza%C3%A7%C3%A3o-das-Tabelas-Din%C3%A2micas-e-Importa%C3%A7%C3%A3o-do-plano-de-Contas-Referencial"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-23T12:11:39Z"
rotulos: ["Configuração", "Tabelas Dinâmicas", "Fiscal", "Contas", "Atualização", "Importação", "#validadoThiagoArantes", "#tabeladinamica", "#planodecontas", "#tabela", "#planodecontasreferencial", "Atualização do SPED ECF", "Configurações do Web Connection", "SPED ECF"]
---

# Atualização das Tabelas Dinâmicas e Importação do plano de Contas Referencial

As tabelas Dinâmicas são usadas em algumas rotinas do sistema.  Uma das rotinas que são mais utilizadas as tabelas é a de importação de plano de contas referencial. Para isso, devem ser atualizadas as tabelas dinâmicas periodicamente seguindo os passos abaixo, e se for necessário  usar dados das tabelas em outras rotinas, também deverão ser atualizadas.

#### 1º Passo

Faça o download do SPED ECF no site da Receita Federal no link: <https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/sped-sistema-publico-de-escrituracao-digital/escrituracao-contabil-fiscal-ecf/sped-programa-sped-contabil-fiscal>

####

#### 2º Passo

Certifique-se das configurações do web Connection:

**(1)** Clique no Menu do **Navegador Sankhya >> Configurações;**

**(1)** Será aberto um poup-up, nele localize a sessão do web Connection;

**(1)** Clique no link para acessá-lo;

![Imagem 1: (1) Clique no link para acessá-lo;](https://ajuda.sankhya.com.br/hc/article_attachments/16192096141335)

        ![Imagem 2: (1) Clique no link para acessá-lo;](https://ajuda.sankhya.com.br/hc/article_attachments/16192096143255)

**(1)** Após clicar, irá iniciar um poup-up do Web Connection embarcado no Navegador Sankhya (usando o Web connection embarcado não é necessário baixar ele na máquina).

**(1)** No campo **"Porta de comunicação"** será rodada a aplicação, sendo que a porta informada no parâmetro de chave **"PORTAPPPRINT"** e a inserida neste campo devem ser a mesma; por padrão é a porta 9096.

**(2)** Na Aba Geral Configure o campo URL do sistema informando o link de acesso do sistema;
**(2)** Marque a opção Usa SPED ECF para habilitar a aba SPED ECF;
**(2)** Os campos **"Chave SSL"** e **"Arquivo certificado"** são de uso interno do sistema, o conselho é que não sejam modificados;
**(2)** Configure em **"Memória utilizada"** a memória RAM determinada pelo Web Connection. Em casos de visualização de uma grande quantidade de registros, a sugestão é aumentar a informação neste campo.

![Imagem 3: (2) Na Aba Geral Configure o campo URL do sistema informando o link de acesso do sistema; (2) Marque a opção Usa SPED…](https://ajuda.sankhya.com.br/hc/article_attachments/16192152868119)

#### 3° Passo

Na aba SPED ECF, faça as configurações para comunicar as tabelas Dinâmicas da ECF com o sistema.

![Imagem 4: Na aba SPED ECF, faça as configurações para comunicar as tabelas Dinâmicas da ECF com o sistema. Busque o Diretório…](https://ajuda.sankhya.com.br/hc/article_attachments/16192314826903)

Busque o Diretório onde está a pasta das tabelas do validador da ECF que foi anteriormente instalado.

O diretório possui um valor padrão e caso não seja informado nenhum valor, o que será salvo no arquivo de configuração do Web Connection será:
**C:/Arquivos de Programas RFB/Programas SPED/ECF/recursos/tabelas**

**(1)** Ao clicar no botão Testar, será testada a comunicação do Web Connection com o sistema.

**(1)** Ao clicar no botão Enviar Agora, será levado de forma compactada para o repositório de arquivos do sistema.

![Imagem 5: (1) Ao clicar no botão Enviar Agora, será levado de forma compactada para o repositório de arquivos do sistema.](https://ajuda.sankhya.com.br/hc/article_attachments/16192283911831)

#### 4° Passo

Abrir a Tela Plano de Contas referencial que automaticamente começará descompactar o arquivo das tabelas que estão no repositório e atualizando as tabelas dinâmicas no Sankhya.

**Importante:**
Na tela **"[Preferências"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)**a configuração de dois parâmetros, sendo eles:

**(1)** **"Utilizar aplicação externa para impressão? - USAAPPIMPRESSAO":** Ao ativá-lo, o sistema entende que a aplicação externa de impressão será utilizada; caso o parâmetro esteja desativado, o sistema irá tentar utilizar o plugin de impressão normalmente.

**(1)** **"Porta onde irá rodar a aplicação de impressão - PORTAPPPRINT:"** Este parâmetro se refere a porta na qual o **Sankhya Om** tentará encontrar a aplicação externa de impressão para se comunicar (padrão: 9096).

Para mais informações sobre web connection, acesse o artigo:**[Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDc4MDQxODgzNzQsInRpY2tldF9pZCI6MTQyMDE4LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTYzOTA1NTU4NX0.L3J_KTa8uU8OPfapIC_oMt5ayvKZo8ik9zkaJmpvITg).**
