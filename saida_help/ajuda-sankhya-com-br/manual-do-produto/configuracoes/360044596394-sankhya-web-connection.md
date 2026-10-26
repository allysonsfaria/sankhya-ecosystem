---
id: "360044596394"
titulo: "Sankhya Web Connection"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-09T20:16:14Z"
rotulos: ["Configuração", "Impressão", "Segurança", "http", "https", "PORTAPPPRINT", "Sankhya Web Connection", "USAAPPCUBO", "USAAPPIDENT", "USAAPPIMPRESSAO", "Sankhya Web Connection manual", "Integração", "Navegador", "Implementação e Configuração do Sankhya Web Connection"]
---

# Sankhya Web Connection

Configurações ›› Conectividade

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#oque) [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#antes)    ↳ [Compatibilidade de versões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#compatibilidade)    ↳ [Quais máquinas precisam](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#quais-maquinas)    ↳ [Parâmetros do sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#parametros) [1. Download e instalação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#download)    ↳ [Fazendo o download](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#fazendo-download)    ↳ [Instalando](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#instalando)    ↳ [Iniciando manualmente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#h_01KQYT4HPRCQ08523E7XMD6ENG)  [2. Configuração do navegador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#config-navegador)    ↳ [Chrome](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#chrome)    ↳ [Edge](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#edge) | [3. Configurações do Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#config-wc)    ↳ [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#aba-geral)    ↳ [Aba Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#aba-impressao)    ↳ [Aba Integração balança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#aba-balanca)    ↳ [Aba SPED ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#aba-sped) [4. Identificação de computadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#identificacao) [5. Visualizar/Exportar para cubo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#visualizar) [6. Cubo — Variáveis de filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#cubo)    ↳ [Variáveis de filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#cubo-filtros)    ↳ [Seleção de campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#cubo-selecao) [⚠️ Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#pontos-atencao) |
| --- | --- |

---

## O que é e para que serve

O Sankhya Web Connection é uma aplicação instalada na máquina do usuário que permite ao Sankhya Om se comunicar com dispositivos físicos externos, como impressoras, balanças e coletores de depósito. Sem ele, o sistema não consegue enviar comandos de impressão, capturar pesos de balança nem identificar o computador para controle de acesso.

Navegadores como Chrome e Edge não permitem, de forma nativa, que sites se comuniquem diretamente com programas ou dispositivos locais por questões de segurança. O Web Connection resolve essa limitação atuando como intermediário entre o Sankhya Om e os dispositivos da máquina.

**ℹ️  Nota**

Até maio de 2025, o Web Connection vinha integrado ao navegador Sankhya. Com a descontinuação do navegador Sankhya, ele passou a ser instalado separadamente em cada máquina que utiliza impressoras, balanças, coletores ou controle de acesso por computadores liberados. Se você usava o navegador Sankhya e está migrando para Chrome ou Edge, este artigo guia você em todo o processo.

---

## Antes de começar

### Compatibilidade de versões

A versão do Web Connection deve ser compatível com a versão do Sankhya Om instalada no ambiente:

| Versão do Web Connection | Compatível com Sankhya Om |
| --- | --- |
| Versão 1.0 | Até versão 3.12 |
| Versão 2.0 | A partir da versão 3.13 |

**⚠️  Atenção**

Instalar a versão errada do Web Connection impede a comunicação com o sistema. Verifique a versão do Sankhya Om antes de fazer o download. Consulte: [Atualização do sistema Sankhya Om via WPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943).

### Quais máquinas precisam do Web Connection

O Web Connection precisa estar instalado e em execução em toda máquina que realiza ao menos uma das seguintes ações:

- Impressão de documentos (notas fiscais, cupons, relatórios)
- Integração com balanças ou coletores de depósito
- Login com configuração de acesso apenas por computadores liberados
- Visualização de cubos analíticos
- Uso do PDV Web — o Web Connection fornece o identificador único da máquina, necessário para a abertura de caixa

**ℹ️  Nota**

A instalação é por máquina, não por usuário. Cada computador que realiza essas operações precisa do Web Connection instalado, independentemente de quantos usuários o utilizam.

### Parâmetros do sistema

Alguns recursos do Web Connection dependem de parâmetros que precisam estar ativos no Sankhya Om. Esses parâmetros são configurados no menu **Preferências** (Configurações ›› Avançado). Consulte também: [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834) e [Outros parâmetros importantes de se conhecer](https://ajuda.sankhya.com.br/hc/pt-br/articles/37882732649111).

| Parâmetro | Função | Padrão |
| --- | --- | --- |
| USAAPPIMPRESSAO | Ativa o uso do Web Connection para impressão. Deve estar ligado em toda máquina que imprime pelo sistema. | Desligado |
| PORTAPPPRINT | Porta de comunicação entre o Sankhya Om e o Web Connection. Deve ser a mesma configurada na aplicação. | 9096 |
| USAAPPIDENT | Necessário para identificação de computadores e controle de acesso por máquina. | Desligado |
| USAAPPCUBO | Necessário para visualização de cubos analíticos via Web Connection. | Desligado |

**ℹ️  Nota**

Alterações nos parâmetros USAAPPIMPRESSAO e PORTAPPPRINT só têm efeito após fechar e reabrir a tela de impressão.

###

---

## 1. Download e instalação

### Fazendo o download

Acesse o [site de downloads do Web Connection](https://downloads.sankhya.com.br/downloads?app=WebConnection&c=1). Se preferir navegar manualmente, o Web Connection fica em **Navegadores ›› Web Connection**.

Na lista de versões, escolha a compatível com o Sankhya Om do seu ambiente (consulte a tabela **Compatibilidade de versões** em Antes de começar) e clique em **Baixar (.exe)** na linha correspondente à arquitetura da máquina (32 ou 64 bits).

![Central de Downloads — Web Connection (05/2026)](https://ajuda.sankhya.com.br/hc/article_attachments/40271854869783)

### Instalando

1. Clique no arquivo baixado para iniciar a instalação.
2. Uma tela azul de segurança do Windows (**Windows Smart Screen**) será exibida. Clique em **Mais informações**.
3. Clique em **Executar mesmo assim**.
4. Anote o caminho de instalação exibido no pop-up — você vai precisar dele para iniciar a aplicação manualmente, se necessário.

![Imagem 2: Anote o caminho de instalação exibido no pop-up — você vai precisar dele para iniciar a aplicação manualmente, se…](https://ajuda.sankhya.com.br/hc/article_attachments/40271854872343)![Imagem 3: Anote o caminho de instalação exibido no pop-up — você vai precisar dele para iniciar a aplicação manualmente, se…](https://ajuda.sankhya.com.br/hc/article_attachments/40271840858391)

**ℹ️ Permissão de administrador**

Em alguns casos, se o Web Connection foi instalado em uma pasta diferente da pasta do usuário do computador, execute a aplicação como administrador (você precisa ter essa permissão. Entenda com sua equipe de TI:

1. Clique com o botão direito no arquivo **web\_connection.exe**.
2. Selecione **Executar como administrador**.Verificando se está em execução

Após a instalação, o Web Connection já deve estar em execução. Para confirmar:

- Clique na seta para cima na barra de tarefas (**Mostrar ícones ocultos**) ou busque na  barra de tarefas do sistema operacional do computador.
- Verifique se o ícone do Web Connection aparece na bandeja do sistema.

### Iniciando manualmente (se o ícone não aparecer)

O Web Connection não inicia automaticamente com o Windows por padrão. Se o ícone não aparecer na bandeja após reiniciar o computador, inicie a aplicação manualmente seguindo os passos abaixo.

1. Abra o **Explorador de Arquivos** e navegue até o caminho anotado durante a instalação (geralmente: `C:\Usuários\NOME_USUÁRIO\Sankhya web`). Acesse a pasta **Sankhya web ›› Sankhya\_web\_connectionx64 ›› executar**.
2. Clique duas vezes em **web\_connection.exe**.

**⚠️  Atenção — Erro "Porta configurada para WebConnection em uso"**

**Se o navegador Sankhya estiver aberto:** feche-o e execute o Web Connection novamente — o navegador Sankhya usa a mesma porta por ter o Web Connection embutido.

**Se não for o navegador Sankhya:** outro aplicativo está ocupando a porta. Acione o TI da empresa para identificar e encerrar o processo ou configurar uma porta alternativa.

---

## 2. Configuração do navegador

Com o Web Connection instalado e em execução, configure a comunicação entre ele e o navegador. O processo é iniciado pela própria tentativa de impressão — o sistema detecta que a configuração ainda não foi feita e exibe um assistente automático.

**⚠️  Atenção — HTTPS obrigatório**

Para que o Web Connection funcione em navegadores comerciais (Chrome e Edge), a URL de acesso ao Sankhya Om precisa estar configurada com certificado de segurança válido (HTTPS). Em ambientes com HTTP simples, o navegador bloqueia a comunicação com o servidor local antes mesmo de ela acontecer. Consulte o datacenter ou a equipe de TI sobre a migração para HTTPS. Para mais contexto: [Fim do Ciclo de Vida — Navegador Sankhya: Comunicado Oficial](https://ajuda.sankhya.com.br/hc/pt-br/articles/35828384474647).

**ℹ️**Use o usuário SUP ou outro usuário sem restrição de acesso por computadores liberados para realizar a configuração inicial. Após concluir, deslogue e teste com o usuário que possui a restrição.

### Chrome

1. Acesse o Sankhya Om no Chrome e abra **Portal de Vendas** (Comercial ›› Consulta ›› Portal de Vendas). Tente imprimir uma nota.
2. No pop-up que aparecer, clique em **Configurar automaticamente**.
3. No próximo pop-up, clique em **Avançadas**.
4. Clique em **Ir para localhost (não seguro)**.
5. Quando a mensagem de sucesso aparecer, confirme a configuração.
6. O Chrome exibirá um aviso de permissão de acesso à rede local — clique em **Permitir**.
7. Teste a impressão novamente para confirmar que as impressoras aparecem.

### Edge

O processo de configuração no Edge é equivalente ao do Chrome. Siga os mesmos passos da seção anterior.

**💡  Dica**

Usuários que encontraram dificuldades com o Chrome relataram que o Edge apresenta melhor desempenho e menos fricção no processo de configuração inicial com o Web Connection.

---

## 3. Configurações do Web Connection

Acesse as configurações pelo menu da janela do Web Connection: clique na **barra de título** (topo da janela) e selecione **Configurações**.

### Aba Geral

![Interface da aba Geral do Sankhya Web Connection com os campos Porta de comunicação (9096), Chave SSL, Arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/40271854875671)

- **Porta de comunicação** — porta onde a aplicação vai rodar. Deve ser a mesma configurada no parâmetro PORTAPPPRINT em Preferências. Padrão: 9096.
- **Chave SSL** e **Arquivo certificado** — uso interno do sistema. Não modifique esses campos.
- **Memória utilizada** — memória RAM reservada para o Web Connection. Aumente em ambientes com grande volume de dados em cubos.
- **Tipo de cubo** — define como os cubos são carregados: **Banco de dados** suporta cubos maiores com menor performance; **Memória** usa a RAM da máquina, mais rápido para volumes menores.
- **Usa SPED ECF** — marque quando a máquina realiza envio de tabelas dinâmicas para o Repositório de Arquivos do Sankhya Om. Habilita a aba SPED ECF.
- **URL do Sistema** — informe a URL do Sankhya Om para que o Web Connection consiga enviar arquivos para o repositório.
- **Múltiplas Balanças** — marque quando a máquina opera com mais de uma balança. Altera o layout da aba Integração balança.

### Aba Impressão

Lista as impressoras disponíveis na máquina. Use os botões desta aba para imprimir páginas de teste e verificar o funcionamento de cada impressora antes de usar o sistema.

![Aba Impressão do Sankhya Web Connection exibindo a lista de impressoras disponíveis na máquina: OneNote, Microsoft XPS…](https://ajuda.sankhya.com.br/hc/article_attachments/40271854876055)

### Aba Integração balança

Configure aqui a integração com balanças conectadas à máquina. O tipo de integração depende do modelo da balança. Entenda para que serve e como usar cada opção de seleção:

#### Não usa

Selecione quando a máquina não opera com balanças.

![Aba Integração balança do Sankhya Web Connection com o campo Integração com a balança selecionado como Não usa.](https://ajuda.sankhya.com.br/hc/article_attachments/40271854878359)

#### Digitron

Configure:

- **Porta de comunicação** — porta física da balança. Deve ser exatamente a porta em que a balança está instalada.
- **Frequência de transmissão** — a balança e o software precisam estar na mesma frequência para se comunicar corretamente. Padrão: 9600.
- **Tempo de espera captura de peso** — tempo de timeout em segundos. Se ultrapassado, a conexão é encerrada e o sistema exibe uma mensagem de erro.

![Aba Integração balança com Digitron selecionado, exibindo campos Porta de comunicação (COM3), Frequência de transmissão…](https://ajuda.sankhya.com.br/hc/article_attachments/40271854879767)

#### Filizola (IDM)

Além de Porta de comunicação, Frequência de transmissão e Tempo de espera, verifique no manual da balança as informações para os campos **Databits**, **Stopbits** e **Paridade**. Use o botão **Testar (obter peso)** para verificar se a leitura está sendo feita corretamente.

![Aba Integração balança com Outra - serial selecionada no menu suspenso, exibindo todos os tipos disponíveis: Não usa,…](https://ajuda.sankhya.com.br/hc/article_attachments/40271854880279)

#### Toledo (P3)

Ao selecionar a opção **"Toledo (P3)"**, ocorrerá a integração com balanças deste tipo. Os campos apresentados aqui são os mesmos elencados na opção Filizola (IDM).

####

#### Outra - Serial

Para qualquer balança serial não listada. Consulte o manual da balança para os campos Databits, Stopbits e Paridade.

- **Tempo de espera captura de peso** — define o tempo de encerramento da conexão (timeout).
- **Tempo de espera de estabilização** — exclusivo para esta opção. Faz o sistema aguardar o tempo definido (em segundos) para que a balança estabilize fisicamente o peso antes de realizar a pesagem.

![Aba Integração balança com Outra - serial selecionada, exibindo campos de configuração serial incluindo Databits (7),…](https://ajuda.sankhya.com.br/hc/article_attachments/38099944911255)

####

#### TCP/IP

Para balanças com conexão de rede. Configure:

- **IP da balança** e **Porta da balança**
- **Início da string de leitura** e **Fim da string de leitura** — delimitadores do pacote de dados enviado pela balança
- **Casa decimal** — posição da casa decimal no valor lido
- **Expressão para captura de Peso** — expressão regular usada quando "Utiliza expressão para capturar peso?" está ativa. Padrão: `\b(\s+)\b[0-9]+`
- **Ativar log?** — gera arquivo de log das leituras. Útil para diagnóstico quando a integração não está retornando o peso corretamente

  ![Aba Integração balança com TCP/IP selecionado, exibindo campos IP da Balança (localhost), Porta de comunicação (9898),…](https://ajuda.sankhya.com.br/hc/article_attachments/40271854881687)

**ℹ️  Nota**

O campo Porta de comunicação nas integrações seriais se refere à porta física da balança — não confundir com a porta de comunicação do Web Connection na aba Geral.

Com a marcação **Múltiplas Balanças** habilitada na aba Geral, o Web Connection exibe opções adicionais para cadastrar e configurar mais de uma balança:

![GIF animado mostrando a aba Integração balança do Web Connection com Múltiplas Balanças habilitado, demonstrando o…](https://ajuda.sankhya.com.br/hc/article_attachments/40271854882711)

### Aba SPED ECF

Disponível apenas quando **Usa SPED ECF** está marcado na aba Geral. Configure o envio de tabelas dinâmicas para o Repositório de Arquivos do Sankhya Om.

- **Diretório de tabelas** — caminho dos arquivos de tabelas ECF. Padrão: `C:/Arquivos de Programas RFB/Programas SPED/ECF/recursos/tabelas`
- **Tipo de execução** — define quando o envio ocorre:

  - **Ao iniciar o Web Connection** — envia automaticamente toda vez que a aplicação é aberta
  - **Todos os dias** — envia uma vez por dia automaticamente
- **Ano de referência** — selecione o ano das tabelas a enviar. A lista exibe os 6 anos anteriores ao atual.

**Botão Testar** — verifica a conexão com o Sankhya Om pela URL informada e confirma se o diretório existe e contém arquivos.

**Botão Enviar Agora** — compacta e envia todos os arquivos do diretório imediatamente. Nas próximas execuções automáticas, o Web Connection envia apenas os arquivos novos com base no histórico de envios anteriores.

---

## 4. Identificação de computadores

O Web Connection permite identificar a máquina no momento do login, viabilizando o controle de acesso por computadores liberados. Para ativar esse recurso, configure o parâmetro **USAAPPIDENT** em Preferências (Configurações ›› Avançado).

Com o parâmetro ativo, o fluxo de liberação funciona assim:

1. Em [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba **Segurança**, ative a marcação **Acessar apenas por computadores liberados?** para os usuários com essa restrição.
2. Ao tentar fazer login em uma máquina não liberada, o sistema exibe uma mensagem de bloqueio. O usuário preenche **Observação** e clica em **Solicitar liberação**.
3. O administrador acessa [Liberação de Computadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108173), localiza a solicitação e altera o **Status Solicitação** para **Liberado**.
4. Com o Web Connection instalado e em execução nessa máquina, o login passa a funcionar normalmente.

---

## 5. Visualizar/Exportar para cubo

Além da possibilidade de visualização, é possível exportar grades geradas pelos Dashboards e pelas telas no formato HTML5 para o Web Connection por meio da opção **Exportar para cubo**. Ambas as opções estão localizadas no lado superior direito das telas:

![GIF animado mostrando a aba Integração balança do Web Connection com Múltiplas Balanças habilitado, demonstrando o…](https://ajuda.sankhya.com.br/hc/article_attachments/40271854882967)

**⚠️  Atenção**

Mantendo os dois parâmetros **USAAPPIMPRESSAO** e **USAAPPCUBO** desligados, o comportamento do sistema se mantém inalterado.

---

## 6. Cubo — Variáveis de filtros e seleção de campos

Com o parâmetro **USAAPPCUBO** ativo e o Web Connection em execução, você pode visualizar cubos analíticos diretamente pelo Sankhya Om — e ir além da visualização padrão, usando filtros personalizados e seleção de campos para refinar e melhorar o desempenho da análise.

### Variáveis de filtros

Ao criar ou editar um cubo, você pode configurar parâmetros de filtro com duas opções: definir se o campo é obrigatório e vincular o campo a uma tabela do sistema, para que ele se comporte como uma busca de registros — em vez de um campo de digitação livre.

Se o campo for configurado como não requerido, seu preenchimento se torna opcional na hora de visualizar o cubo. Se uma tabela for vinculada, o campo exibe uma lupa que abre a pesquisa de registros dessa tabela — por exemplo, buscar um Parceiro por Nome, Cidade ou E-mail.

#### Sintaxe do filtro

O filtro é criado na Expressão de filtro com a seguinte sintaxe:

```
/*{entity=<Nome do cadastro>;req=<s ou n>}*/
```

Para req, use **"s"** para campo obrigatório e **"n"** para campo opcional. No exemplo abaixo, o filtro está vinculado à tabela Parceiro e é obrigatório:

![Imagem 13: Para req , use "s" para campo obrigatório e "n" para campo opcional. No exemplo abaixo, o filtro está vinculado à…](https://ajuda.sankhya.com.br/hc/article_attachments/40271840873879)

#### Editando variáveis de filtro existentes

Para editar um filtro já criado, selecione com o cursor o parâmetro **"?"** correspondente — o botão **Editar variáveis de filtro** aparece na tela. Ao clicar nele, abre-se o pop-up de edição, onde você pode alterar a obrigatoriedade do campo ou trocar a tabela vinculada. Todo campo é criado por padrão como obrigatório.

#### Visualizando o cubo com filtros

Ao clicar em **Visualizar Cubo**, o Web Connection abre o pop-up de parâmetros. Campos obrigatórios são destacados com **\*** (asterisco vermelho) e precisam ser preenchidos antes de executar:

![Tela de configuração de cubo no Sankhya Om exibindo a aba Seleção de campos com campos disponíveis à esquerda e…](https://ajuda.sankhya.com.br/hc/article_attachments/40271854884375)

Clique na lupa ao lado do campo para abrir a busca na tabela vinculada. Você pode digitar diretamente o código ou pesquisar pelo nome:

![Pop-up de Pesquisa de Parceiro exibindo lista de registros com colunas Nome Parceiro e Razão social, com campo de busca…](https://ajuda.sankhya.com.br/hc/article_attachments/40271840875799)

Com todos os campos obrigatórios preenchidos, clique em **Executar** para visualizar o cubo com os registros filtrados.

### Seleção de campos

Na aba **Seleção de campos** do pop-up de visualização, você escolhe quais campos do cubo quer ver — sem precisar carregar todos os dados disponíveis. Isso reduz o tráfego com o servidor e melhora o desempenho, especialmente em cubos com grande volume de registros.

Campos de data podem ser agrupados por **dia, semana, mês, trimestre ou ano** — use o campo **Agrupar por** após selecionar um campo de data na lista de Campos de dimensão. Para selecionar um campo como **Campo de valor**, ele precisa ser do tipo numérico (como o valor de um desdobramento financeiro).

Você pode salvar a seleção para reutilizar depois:

- Com **[Padrão]** selecionado, clique em **Salvar seleção** e dê um nome — isso cria uma nova seleção.
- Com uma seleção já criada ativa, **Salvar seleção** atualiza a existente.
- O botão **Excluir** só fica habilitado para seleções criadas por você — a seleção padrão não pode ser excluída.

**ℹ️  Nota**

O tipo de carregamento do cubo afeta o desempenho: **Banco de dados** suporta cubos com grande volume de dados e baixa disponibilidade de memória; **Memória** é mais rápido para volumes menores. Configure essa opção na aba Geral do Web Connection (campo **Tipo de cubo**).

---

## ⚠️ Pontos de atenção

- **A instalação é por máquina, não centralizada.** Cada computador que imprime, usa balança, coletor, PDV Web ou tem login com restrição precisa do Web Connection instalado e em execução.
- **O Web Connection não inicia automaticamente com o Windows.** Se o ícone não aparecer na bandeja após ligar o computador, inicie manualmente (consulte a seção [Iniciando manualmente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#inicio-manual), acima).
- **O navegador Sankhya e o Web Connection externo não podem usar a mesma porta ao mesmo tempo.** Se o navegador Sankhya estiver aberto, feche-o antes de executar o Web Connection separado.
- **HTTPS é obrigatório para uso com Chrome e Edge.** Sem ele, o navegador bloqueia a comunicação com o servidor local. Consulte o TI sobre a migração para HTTPS.
- **A porta de comunicação do Web Connection e o parâmetro PORTAPPPRINT devem ser iguais.** Se a porta for alterada na aplicação, atualize o parâmetro em Preferências.
- **A memória RAM deve ser configurada de acordo com a necessidade** para visualização de cubos (aba Geral, campo **Memória utilizada**).

**💡  Dica**

Erro "Web Connection não encontrado"? Consulte o artigo [Web Connection não encontrado — Erro em impressões ou no login de usuário com acesso apenas por computadores liberados](https://ajuda.sankhya.com.br/hc/pt-br/articles/36452312790423-Web-Connection-n%C3%A3o-encontrado-Erro-em-impress%C3%B5es-ou-no-login-de-usu%C3%A1rio-com-acesso-apenas-por-computadores-liberados) para o diagnóstico passo a passo.

---
