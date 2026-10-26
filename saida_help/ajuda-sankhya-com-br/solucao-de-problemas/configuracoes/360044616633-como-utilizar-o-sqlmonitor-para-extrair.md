---
id: "360044616633"
titulo: "Como utilizar o SQLMonitor para extrair Log do MGE/MITRA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616633-Como-utilizar-o-SQLMonitor-para-extrair-Log-do-MGE-MITRA"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:53:45Z"
rotulos: ["Configuração", "MGE", "Mitra", "Log", "Utilização do SQLMonitor para Extração de Logs do MGE/MITRA", "SQLMonitor", "MGE/MITRA"]
---

# Como utilizar o SQLMonitor para extrair Log do MGE/MITRA

Será necessário baixar o arquivo que consta em anexo(no rodapé deste artigo), caso você não tenha. Ao descompactar serão gerados os seguintes arquivos: sqlmon.exe e smclient.dll.

Em seguida abra o utilitário e realize as configurações necessárias:

Clique em Options > Trace Options e configure as opções:

Na aba Buffer, preencha Buffer Size com 2048, e marque em Buffer Management como Page to Disk:

Clique em OK.

O SQL Monitor deve ser aberto antes do aplicativo ao qual deseja capturar as instruções SQL.

Após aberto, efetue login no sistema. Note que o SQL Monitor passará a capturar os comandos passados ao banco de dados.

Veja abaixo algumas funcionalidades:

- Para **Limpar** os comandos capturados na tela, clique no botão Clear;

- Para **Pausar**, utilize o botão Pause;

- Para **Salvar** o Log, clique no botão Save Log.

**Importante**:

- Recomenda-se antes de capturar o Log de uma operação efetuar a limpeza do log (botão Clear), em seguida executar o procedimento ao qual deseja capturar e em seguida salvar (botão Save Log). Isto evita que o arquivo fique muito extenso e que traga informações desnecessárias;
- Caso o sistema não capture informações, repita o procedimento, clicando com o botão direito no executável do SQL Monitor, e abrindo pela opção Executar como Administrador.

Download SQLMonitor aqui:
