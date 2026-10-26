---
id: "34976990562711"
titulo: "Como configurar o sistema para solicitar a liberação do Evento 76"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34976990562711-Como-configurar-o-sistema-para-solicitar-a-libera%C3%A7%C3%A3o-do-Evento-76"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:26:13Z"
rotulos: ["Configuração", "Eventos", "Fiscal", "Liberação de Limites", "XML", "Impostos", "Portal de Importação de XML", "Diferença de Impostos", "Evento 76", "Liberadores", "Squad Docs"]
---

# Como configurar o sistema para solicitar a liberação do Evento 76

O evento **76 – Diferença de Impostos** está diretamente ligado à rotina do **Portal de Importação de XML** e é acionado quando o sistema identifica **divergências nos impostos dos produtos** durante o processo de importação.

Quando devidamente configurado, o sistema **passa a exigir a liberação por um usuário autorizado** sempre que essa diferença for detectada, garantindo controle e conformidade no recebimento fiscal.

### Como configurar o sistema para solicitar a liberação do Evento 76

###

#### 1. Liberar acesso á configuração do Portal de Importação de XML

##### **(1)** Acesse a tela [''Acessos''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) (Configurações » Controle de Acesso » Acessos).

**(2)** Pesquise pela tela [**''Portal de Importação de XML''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) e verifique a permissão do campo **''Configurar''.**

![Imagem 1: (2) Pesquise pela tela ''Portal de Importação de XML'' e verifique a permissão do campo ''Configurar''.](https://ajuda.sankhya.com.br/hc/article_attachments/36645155602327)

#### 2. Habilitar a exigência de liberação por divergência de impostos no Portal de Importação (XML)

##### **(1)** Acesse o ''Portal de Importação de XML''.

**(2)** Clique no botão ''**Outras Opções''** (ícone de três pontos) e selecione a opção **''Configuração para liberações de divergências''**.

**(3)** No pop-up exibido, marque a opção **''Exigir liberação p/ impostos''**.

![Imagem 2: (3) No pop-up exibido, marque a opção ''Exigir liberação p/ impostos'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36645173866007)![Imagem 3: (3) No pop-up exibido, marque a opção ''Exigir liberação p/ impostos'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36645155604375)

#### 3. Definir liberadores do Evento 76

##### **(1)** Acesse a tela [''Usuários''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) (Configurações » Controle de Acesso » Usuários).

**(2)** Selecione o usuário que será responsável pela liberação.

**(3)** Clique em ''**Outras Opções''** (ícone de três pontos) e escolha a opção **''Limites para Liberação''**.

**(4)** Configure a permissão para o evento **''76 – Diferença de Impostos''**.

![Imagem 4: (4) Configure a permissão para o evento ''76 – Diferença de Impostos'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36645173868183)![Imagem 5: (4) Configure a permissão para o evento ''76 – Diferença de Impostos'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36645155608471)

**(1)** Após as configurações, sempre que ocorrer divergência de impostos durante a importação de XML, o sistema solicitará a liberação de um responsável.

Somente os usuários previamente configurados como liberadores do **Evento 76** poderão efetuar essa liberação.
